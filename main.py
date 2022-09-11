import random
from map_state import MapState
from rooms import ROOMS as ROOMS
from backup_rooms import BACKUPS
from roomsOld import ROOMS as ROOMSOLD
from treelib import Tree
from rando_utils import link_doors, inject_warp_info, \
    room_quality, is_good_entry, create_room_node, create_warp_node, \
    is_done, room_of_id, create_connec_node, \
    index_of_room, rooms_data_from_alias, build_room, trim_room_tree


def main():
    seed = random.randrange(999999999)
    seed = 30
    orig_seed = seed
    random.seed(a=seed)

    rooms_in_rando = Tree()
    rando_state = MapState()
    rando_state.build_initial_state(ROOMS)
    print('Initial Map state:')
    rando_state.display_state()

    avail_room_indecies = []
    for index, room in enumerate(ROOMS):
        if 'skip' in room:
            continue
        elif MapState.doors_in_room(room) > 0:
            avail_room_indecies.append(index)

    avail_backups_indecies = []
    for index, room in enumerate(BACKUPS):
        if 'skip' in room:
            continue
        elif MapState.doors_in_room(room) > 0:
            avail_backups_indecies.append(index)

    for index, room in enumerate(ROOMS):
        if room['alias'] == 'ViridianCity':
            print('\n----------------------')
            print('Creating initial ROOM:')
            rooms_in_rando = build_room(room)
            rando_state.update_state(room_tree=rooms_in_rando, room=room)
            avail_room_indecies.remove(index)
            break

    creating_tree = True
    while creating_tree:
        print('----------------------\n')
        print('SEED = ', orig_seed)
        print('Current Map State:')
        rando_state.display_state()
        print(f'\n{avail_room_indecies = }')

        print('----------------------')
        print('Start of Tree:\n')

        if rando_state.halt_process():
            print('HALTED')
            break
        if rando_state.doors_not <= 0:
            print('ADDED TOO MANY ROOMS/DOORS')
            break
        rooms_in_rando.show(data_property="node_alias")

        current_leaves = rooms_in_rando.leaves()
        # seed = random.randrange(9999999)
        # random.seed(a=seed)
        # random.shuffle(current_leaves)
        for leaf in current_leaves:
            if rooms_in_rando.depth(leaf) % 2 == 0:  # leaf is a RoomNode
                print('----------------------')
                print('Processing ROOM:', leaf.data.node_alias)
                if leaf.data.is_terminus:
                    print('\tRoom was terminus.')
                    continue
                else:
                    print('WHOOPS!')

            elif rooms_in_rando.depth(leaf) % 2 == 1:  # leaf is a WarpNode or ConnecNode
                if leaf.data.is_warp:  # leaf is a WarpNode
                    print('----------------------')
                    print('Processing WARP:', leaf.data.node_alias)

                    poss_room_choices = list(avail_room_indecies)
                    while len(poss_room_choices) > 0:
                        exit_candidate = random.choice(poss_room_choices)
                        exit_room = ROOMS[exit_candidate]
                        # update the seed after making a choice
                        seed = random.randrange(9999999)
                        random.seed(a=seed)

                        viable_warps = []
                        for warp in exit_room['warps']:
                            if 'pair_id' in warp:
                                viable_warps.append(warp)
                        if len(viable_warps) > 0 and \
                            rando_state.is_good_exit(
                                exit_room=exit_room
                        ):
                            exit_warp = random.choice(viable_warps)
                            print('\tSuccessfully fetched (room, warp):\n\t\t',
                                  exit_room['alias'], ',', exit_warp['dest_map'][4:])

                            leaf.data.add_exit_warp(warp=exit_warp)
                            leaf.data.add_exit_warp_pairs(room=exit_room)

                            room_tree = build_room(room=exit_room)
                            trim_room_tree(
                                room_tree=room_tree, room_parent=leaf,
                                avail_room_indecies=avail_room_indecies,
                            )

                            rando_state.update_state(room_tree=room_tree, room=exit_room)
                            rooms_in_rando.paste(nid=leaf.identifier, new_tree=room_tree)

                            avail_room_indecies.remove(exit_candidate)
                            break
                        else:
                            poss_room_choices.remove(exit_candidate)
                            continue

                    if len(poss_room_choices) == 0:
                        backup_choices = list(avail_backups_indecies)
                        while len(backup_choices) > 0:
                            exit_candidate = random.choice(backup_choices)
                            exit_room = ROOMS[exit_candidate]
                            # update the seed after making a choice
                            seed = random.randrange(9999999)
                            random.seed(a=seed)

                            viable_warps = []
                            for warp in exit_room['warps']:
                                if 'pair_id' in warp:
                                    viable_warps.append(warp)
                            if len(viable_warps) > 0 and \
                                    rando_state.is_good_exit(
                                        exit_room=exit_room
                                    ):
                                exit_warp = random.choice(viable_warps)
                                print('\tSuccessfully fetched (room, warp):\n\t\t',
                                      exit_room['alias'], ',', exit_warp['dest_map'][4:])

                                leaf.data.add_exit_warp(warp=exit_warp)
                                leaf.data.add_exit_warp_pairs(room=exit_room)

                                room_tree = build_room(room=exit_room)
                                trim_room_tree(
                                    room_tree=room_tree, room_parent=leaf,
                                    avail_room_indecies=avail_room_indecies,
                                )

                                rando_state.update_state(room_tree=room_tree, room=exit_room)
                                rooms_in_rando.paste(nid=leaf.identifier, new_tree=room_tree)

                                avail_backups_indecies.remove(exit_candidate)
                                break
                            else:
                                backup_choices.remove(exit_candidate)
                                continue

                elif leaf.data.is_connec:  # leaf is a ConnecNode
                    print('----------------------')
                    print('Processing CONNEC:', leaf.data.entry, '->', leaf.data.exit)
                    if is_good_entry(leaf, rando_state.acc_key_items):
                        if leaf.data.is_terminus:
                            print('\tConnection was terminus.')
                            continue

                        index, exit_room = rooms_data_from_alias(leaf.data.exit, give_index=True, give_room=True)
                        if index in avail_room_indecies:
                            room_tree = build_room(room=exit_room)
                            trim_room_tree(
                                room_tree=room_tree, room_parent=leaf,
                                avail_room_indecies=avail_room_indecies,
                            )

                            rando_state.update_state(room_tree=room_tree, room=exit_room)
                            rooms_in_rando.paste(nid=leaf.identifier, new_tree=room_tree)

                            rando_state.open_connections -= 1

                            avail_room_indecies.remove(index)
                        else:
                            leaf.data.is_terminus = True
                            print(f'\tConnection destination, {exit_room["alias"]}, not found in available rooms. Creating terminus.')
                    else:
                        print('\tUnable to finish processing. missing key_item(s):\n\t\t', leaf.data.req_items)
                        continue
                else:
                    print('*** Found a room node in a warp/connec position')
                    print(f'\tBad Node: {leaf.data.node_alias} {leaf.data.is_terminus}')
                    print(f'\tCame from: {rooms_in_rando.parent(leaf.identifier).data.node_alias}')
            else:
                print('\nWTF?\n')
                creating_tree = False
                break
        if is_done(rooms_in_rando):
            print('FINISHED!')
            creating_tree = False
    print(f'\nSEED = {orig_seed}')
    rooms_in_rando.show(data_property="node_alias")


if __name__ == "__main__":
    main()
