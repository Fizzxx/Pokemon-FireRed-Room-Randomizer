from map_omits import map_omits
from map_state import MapState
from room_node import RoomNode
from warp_node import WarpNode
from connec_node import ConnecNode
from treelib import Node, Tree
from rooms import ROOMS


DIRECTORY = "M:\Kameron_Scott\Desktop\Modding\pokefirered\data\maps"


class NodeID:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1


node_id = NodeID()


def link_doors(
        parent_node: RoomNode,
        child_node: RoomNode
):
    map_file_path = DIRECTORY + '\\' + parent_node.room_filename + '\\map.json'
    map_file = open(map_file_path, mode='r')
    map_file_contents = map_file.readlines()
    map_file.close()

    if (': "' + parent_node.room_id + '",') in map_file_contents[1]:
        inject_warp_info(map_file_contents, entry_warp, destination_map, destination_warp_id)

        for poss_duplicate in parent_node.warps:
            if 'pair_id' in poss_duplicate and poss_duplicate is not entry_warp:
                if poss_duplicate['pair_id'] == entry_warp['pair_id']:
                    inject_warp_info(map_file_contents, poss_duplicate, destination_map, destination_warp_id)
#                         # randod_warps.append(poss_duplicate)
    # with os.scandir(DIRECTORY) as entries:
    #     for entry in entries:
    #         omit_map_flag = False
    #         for omit in map_omits:
    #             if entry.name.find(omit) > -1:
    #                 omit_map_flag = True
    #         if omit_map_flag:
    #             continue
    #
    #         current_map = DIRECTORY + '\\' + entry.name + '\\map.json'
    #         map_file = open(current_map, mode='r')
    #         map_file_contents = map_file.readlines()
    #         map_file.close()
    #
    #         if (': "' + parent_node.room_id + '",') in map_file_contents[1]:
    #             inject_warp_info(map_file_contents, entry_warp, destination_map, destination_warp_id)
    #
    #             for poss_duplicate in parent_node.warps:
    #                 if 'pair_id' in poss_duplicate and poss_duplicate is not entry_warp:
    #                     if poss_duplicate['pair_id'] == entry_warp['pair_id']:
    #                         inject_warp_info(map_file_contents, poss_duplicate, destination_map, destination_warp_id)
    #                         # randod_warps.append(poss_duplicate)


def inject_warp_info(
        file_lines: list[str],
        target_warp: dict,
        dest_map: str,
        dest_warp_id: int
):
    for line in range(len(file_lines)):
        if file_lines[line].find('\"dest_map\":') > -1:
            if (': ' + str(target_warp['x']) + ',') in file_lines[line - 3]:
                if (': ' + str(target_warp['y']) + ',') in file_lines[line - 2]:
                    file_lines[line] = (
                            file_lines[line][:file_lines[line].find(':') + 1] + ' "' + str(dest_map) + '",\n')
                    file_lines[line + 1] = (
                            file_lines[line + 1][:file_lines[line + 1].find(':') + 1] + ' ' + str(dest_warp_id) + '\n')


def room_quality(exit_room, acc_key_items):
    bad_room = True
    bad_warp = False
    exit_warp = None
    for poss_exit_warp in exit_room['warps']:
        if 'pair_id' in poss_exit_warp:
            if 'req_items' in poss_exit_warp:
                if poss_exit_warp['requires_all']:
                    for req in poss_exit_warp['req_items']:
                        if req not in acc_key_items:
                            bad_warp = True
                else:
                    for req in poss_exit_warp['req_items']:
                        if req in acc_key_items:
                            bad_warp = False
                            break
                        else:
                            bad_warp = True
            elif not bad_warp:
                exit_warp = poss_exit_warp
                bad_room = False
    if bad_room:
        return None
    else:
        return exit_room, exit_warp


def is_good_entry(entry: Node, acc_key_items):
    if entry.data.req_items is not None:
        if entry.data.requires_all:
            for item in entry.data.req_items:
                if item not in acc_key_items:
                    return False
        else:
            have_item = False
            for item in entry.data.req_items:
                if item in acc_key_items:
                    have_item = True
            return have_item
    return True


def create_room_node(tree: Tree, room: dict, parent: Node = None):
    if parent is not None:
        parent_id = parent.identifier
    else:
        parent_id = None
    tree.create_node(
        tag=room['alias'], identifier=node_id.value,
        data=RoomNode(room), parent=parent_id
    )
    node_id.increment()


def build_room(room: dict):
    room_tree = Tree()
    root_node_id = node_id.value
    room_tree.create_node(
        tag=room['alias'], identifier=root_node_id,
        data=RoomNode(room), parent=None
    )
    node_id.increment()

    used_pair_ids = []
    room_root = room_tree.get_node(root_node_id)
    for warp in room['warps']:
        if 'pair_id' not in warp:
            continue

        if warp['pair_id'] not in used_pair_ids:
            create_warp_node(tree=room_tree, parent=room_root, warp=warp)
            used_pair_ids.append(warp['pair_id'])
            print(f'\tAdding warp from: {room["alias"]} -> {warp["dest_map"]}')

    for connection in room['connections']:
        create_connec_node(
            tree=room_tree, parent=room_root,
            connec=connection, terminus=False
        )
        print(f'\tAdding connec from: {room["alias"]} -> (Direct to {connection[0]})')

    return room_tree


def trim_room_tree(room_tree: Tree, room_parent: Node, avail_room_indecies: list):
    for leaf in room_tree.leaves():
        if leaf.data.is_warp and room_parent.data.is_warp:
            if leaf.data.entry['pair_id'] == room_parent.data.exit['pair_id']:
                if room_tree.remove_node(leaf.identifier) > 1:
                    print('*** removed too many nodes!')
                else:
                    print('\tRemoving existing warp:', leaf.data.node_alias)

        elif leaf.data.is_connec and room_parent.data.is_connec:
            if leaf.data.exit == room_parent.data.entry:
                if room_tree.remove_node(leaf.identifier) > 1:
                    print('*** removed too many nodes!')
                else:
                    print('\tRemoving existing connection:', leaf.data.node_alias)
            elif rooms_data_from_alias(leaf.data.exit, give_index=True) \
                    not in avail_room_indecies:
                leaf.data.is_terminus = True

    for leaf in room_tree.leaves():
        if leaf.is_root():
            leaf.data.is_terminus = True


def create_warp_node(tree: Tree, parent: Node, warp: dict = None):
    tree.create_node(
        tag=f'to {warp["dest_map"]}', identifier=node_id.value,
        data=WarpNode(warp), parent=parent.identifier
    )
    tree.get_node(node_id.value).data.add_entry_warp_pairs(parent.data.room)
    node_id.increment()


def create_connec_node(tree: Tree, parent: Node, connec: tuple, terminus: bool = False):
    tree.create_node(
        tag=f'Direct to {connec[0]}', identifier=node_id.value,
        data=ConnecNode(connec, entry=parent.data.node_alias, terminus=terminus),
        parent=parent.identifier
    )
    node_id.increment()


def is_done(tree: Tree):
    terminus_count = 0
    for leaf in tree.leaves():
        if tree.depth(leaf) % 2 == 0:
            if leaf.data.is_terminus:
                terminus_count += 1
        else:
            return False
    if terminus_count == len(tree.leaves()):
        return True
    else:
        return False


def room_of_id(room_id: str):
    for room in ROOMS:
        if room['id'] == room_id:
            return room
    return None


def index_of_room(room: dict):
    for i, r in enumerate(ROOMS):
        if room == r:
            return i


def rooms_data_from_alias(
        room_id: str,
        give_index: bool = False,
        give_room: bool = False
):
    index = None
    room = None
    if give_index or give_room:
        for i, r in enumerate(ROOMS):
            if room_id == r['alias']:
                index = i
                room = r
                break
    if give_index and give_room:
        return index, room
    elif give_index:
        return index
    elif give_room:
        return room
    else:
        return None
