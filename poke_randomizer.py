import random
from map_state import MapState
from rooms import ROOMS as ROOMS
from backup_rooms import BACKUPS
from treelib import Tree
from rando_utils import link_doors, \
    is_good_entry, is_done, rooms_data_from_alias, \
    build_room, trim_room_tree


def randomize_game(debug: bool = False, rando_seed: int = random.randrange(999999999)):
    random.seed(a=rando_seed)

    rooms_in_rando = Tree()  # Initializes the randomizer's map object.
    rando_state = MapState(debug=False)  # Initializes the map state.
    rando_state.build_initial_state(ROOMS)  # Creates the initial mathematical state of the map.
    if debug:
        print('Initial Map state:')
        rando_state.display_state()  # Displays the initial map state to the console.

    for index, room in enumerate(ROOMS):  # Adds randomizable rooms to the list "avail_room_indecies"
        if 'skip' in room:
            continue
        elif MapState.doors_in_room(room) > 0:
            rando_state.avail_room_indecies.append(index)

    for index, room in enumerate(BACKUPS):  # Adds rooms to the list "avail_backup_indecies.
        if 'skip' in room:
            continue
        elif MapState.doors_in_room(room) > 0:
            rando_state.avail_backups_indecies.append(index)

    for index, room in enumerate(ROOMS):  # Creates initial room for the map "rooms_in_rando".
        if room['alias'] == 'ViridianCity':
            if debug:
                print('\n----------------------')
                print('Creating initial ROOM:')
            rooms_in_rando = build_room(room)
            rando_state.update_state(room_tree=rooms_in_rando, room=room)
            rando_state.avail_room_indecies.remove(index)
            break

    creating_tree = True  # Initializes the flag for the main loop.
    insert_map_data = False

    rando_updated = True
    failed_attempts = 0
    while creating_tree:

        if not rando_updated:
            failed_attempts += 1
        rando_updated = False
        if failed_attempts > 1:
            return True

        if rando_state.halt_process():  # Determines if the process needs to halt prematurely.
            if debug:
                print('\nFINAL STATE AND MAP')
            insert_map_data = True
            break

        # Displays the Current map state
        if debug:
            print('----------------------\n')
            print('SEED = ', orig_seed)
            print('Current Map State:')
            rando_state.display_state()
            print(f'\n{len(rando_state.avail_room_indecies)} {rando_state.avail_room_indecies = }')
            print(f'{len(rando_state.avail_backups_indecies)} {rando_state.avail_backups_indecies = }')
            print('----------------------')
            print('Start of Tree:\n')
            rooms_in_rando.show(data_property="node_alias")  # Displays the map tree to console using the "node_alias" as a node label.

        current_leaves = rooms_in_rando.leaves()  # Creates a list of leaves in the rando tree to loop over.

        for leaf in current_leaves:  # This loop iterates over all current leaves in the tree, identifies which type of node it is, and processes accordingly.
            if debug:
                print(f"{rando_state.connec_subverts=}")
            if rooms_in_rando.depth(leaf) % 2 == 0:  # leaf is a RoomNode; All RoomNodes iterated over should be termini.
                if debug:
                    print('----------------------')
                    print('Processing ROOM:', leaf.data.node_alias)
                if leaf.data.is_terminus:
                    if debug:
                        print('\tRoom was terminus.')
                    continue
                else:
                    raise ValueError

            elif rooms_in_rando.depth(leaf) % 2 == 1:  # leaf is a WarpNode or ConnecNode
                if leaf.data.is_warp:  # leaf is a WarpNode; an exit room is randomly selected, and the tree is extended by a subtree with a room as the root.
                    if debug:
                        print('----------------------')
                        print('Processing WARP:', leaf.data.node_alias)

                    poss_room_choices = list(rando_state.avail_room_indecies)  # Creates a list copy to avoid editing the original list.
                    poss_backup_choices = list(rando_state.avail_backups_indecies)
                    room_choices = (poss_room_choices, poss_backup_choices)
                    available_indecies = (rando_state.avail_room_indecies, rando_state.avail_backups_indecies)
                    using_backups = 0
                    room_chosen = False
                    # Iterates through the available rooms, and determines a viable exit room for the warp.
                    while not room_chosen and (len(poss_room_choices) > 0 or len(poss_backup_choices) > 0):
                        exit_candidate = random.choice(room_choices[using_backups])
                        if using_backups:
                            exit_room = BACKUPS[exit_candidate]
                        else:
                            exit_room = ROOMS[exit_candidate]

                        # update the seed after making a choice
                        rando_seed = random.randrange(9999999)
                        random.seed(a=rando_seed)

                        viable_warps = []  # Creates a list to track viable exit warps in the candidate room.
                        for warp in exit_room['warps']:
                            if 'pair_id' in warp:
                                viable_warps.append(warp)

                        if len(viable_warps) > 0 and rando_state.is_good_exit(exit_room=exit_room):  # the exit was deemed viable, and the tree is extended.
                            exit_warp = random.choice(viable_warps)  # The exit warp is selected from the list of viable warps.
                            if debug:
                                print('\tSuccessfully fetched (room, warp):\n\t\t',
                                      exit_room['alias'], ',', exit_warp['dest_map'][4:])

                            # The leaf is updated with the selected exit room and exit warp
                            leaf.data.add_exit_warp(exit_warp=exit_warp, exit_room=exit_room)
                            leaf.data.add_exit_warp_pairs(room=exit_room)

                            room_tree = build_room(room=exit_room, debug=debug)  # The subtree is built.
                            trim_room_tree(  # The subtree is trimmed to remove pathways that have already been included in the tree
                                room_tree=room_tree, room_parent=leaf,
                                avail_room_indecies=available_indecies[using_backups],
                                debug=debug
                            )

                            # The MapState is updated with the new room info, the subtree is added to the main tree, the room is removed from available indecies
                            rando_state.update_state(room_tree=room_tree, room=exit_room)
                            rooms_in_rando.paste(nid=leaf.identifier, new_tree=room_tree)
                            available_indecies[using_backups].remove(exit_candidate)
                            room_chosen = True
                        elif "low_priority" in exit_room and len(rando_state.avail_room_indecies) == rando_state.lp_rooms_remaining:
                            exit_warp = random.choice(viable_warps)  # The exit warp is selected from the list of viable warps.
                            if debug:
                                print("\nBYPASSING TO CLOSE\n")
                                print('\tSuccessfully fetched (room, warp):\n\t\t',
                                      exit_room['alias'], ',', exit_warp['dest_map'][4:])

                            # The leaf is updated with the selected exit room and exit warp
                            leaf.data.add_exit_warp(exit_warp=exit_warp, exit_room=exit_room)
                            leaf.data.add_exit_warp_pairs(room=exit_room)

                            room_tree = build_room(room=exit_room, debug=debug)  # The subtree is built.
                            trim_room_tree(  # The subtree is trimmed to remove pathways that have already been included in the tree
                                room_tree=room_tree, room_parent=leaf,
                                avail_room_indecies=available_indecies[using_backups],
                                debug=debug
                            )

                            # The MapState is updated with the new room info, the subtree is added to the main tree, the room is removed from available indecies
                            rando_state.update_state(room_tree=room_tree, room=exit_room)
                            rooms_in_rando.paste(nid=leaf.identifier, new_tree=room_tree)
                            available_indecies[using_backups].remove(exit_candidate)
                            room_chosen = True
                        else:
                            room_choices[using_backups].remove(exit_candidate)  # The room was not deemed a viable exit, so it's removed from the list of choices.
                            if len(room_choices[0]) == 0:
                                using_backups = 1
                            continue

                    if room_chosen:
                        rando_updated = True

                elif leaf.data.is_connec:  # leaf is a ConnecNode
                    if debug:
                        print('----------------------')
                        print('Processing CONNEC:', leaf.data.entry, '->', leaf.data.exit)
                    if is_good_entry(leaf, rando_state.acc_key_items):
                        if leaf.data.is_terminus:
                            if debug:
                                print('\tConnection was terminus.')
                            continue

                        rando_updated = True

                        index, exit_room = rooms_data_from_alias(leaf.data.exit, give_index=True, give_room=True)
                        if index in rando_state.avail_room_indecies:
                            room_tree = build_room(room=exit_room, debug=debug)
                            trim_room_tree(
                                room_tree=room_tree, room_parent=leaf,
                                avail_room_indecies=rando_state.avail_room_indecies,
                                debug=debug
                            )

                            rando_state.update_state(room_tree=room_tree, room=exit_room)
                            rooms_in_rando.paste(nid=leaf.identifier, new_tree=room_tree)

                            rando_state.open_connections -= 1  # add this into MapState.update_state()

                            rando_state.avail_room_indecies.remove(index)
                        else:
                            leaf.data.is_terminus = True
                            if debug:
                                print(f'\tConnection destination, {exit_room["alias"]}, not found in available rooms. Creating terminus.')
                    else:
                        if debug:
                            print('\tUnable to finish processing. missing key_item(s):\n\t\t', leaf.data.req_items)
                        continue
                else:
                    if debug:
                        print('*** Found a bad node in a warp/connec position')
                        print(f'\tBad Node: {leaf.data.node_alias} {leaf.data.is_terminus}')
                        print(f'\tCame from: {rooms_in_rando.parent(leaf.identifier).data.node_alias}')
            else:
                if debug:
                    print('\nWTF? Something didn\'t math right.\n')
                creating_tree = False
                break
        if is_done(rooms_in_rando):
            print('FINISHED!')
            creating_tree = False

    if debug:
        print('Start of Tree:\n')
        rooms_in_rando.show(data_property="node_alias")
        print('----------------------\n')
        print('SEED = ', orig_seed)
        print('Current Map State:')
        rando_state.display_state()
        print(f'\n{len(rando_state.avail_room_indecies)} {rando_state.avail_room_indecies = }')
        print(f'{len(rando_state.avail_backups_indecies)} {rando_state.avail_backups_indecies = }')

    if insert_map_data:
        print("Inserting Map Data into Decomp")
        for node in rooms_in_rando.all_nodes():
            if rooms_in_rando.depth(node) % 2 == 1:
                if node.data.is_warp:
                    link_doors(node.data)
        # write final map tree to file named "spoiler_log.txt"
        spoiler_log = open("spoiler_log.txt", "w")
        spoiler_log.close()
        rooms_in_rando.save2file(filename="spoiler_log.txt",
                                 data_property="node_alias")
    return False


if __name__ == "__main__":
    seed = random.randrange(999999999)  # Randomly generates the seed.
    # seed = 31574833  # 22 # 31574833 # 346360342 # 190649677  # Debug use; enter a specified seed.
    orig_seed = seed  # Saves the original seed value; seed value is rerolled per iteration of room selection.
    random.seed(a=seed)  # Loads the seed into the module "random".

    attempt = 1
    print("---------------------")
    print(f"Seed: {orig_seed}")
    print(f"{attempt = }")
    while randomize_game(debug=False):
        attempt += 1
        print(f"{attempt = }")
        seed = random.randrange(999999999)
        random.seed(a=seed)

    print("---------------------")
