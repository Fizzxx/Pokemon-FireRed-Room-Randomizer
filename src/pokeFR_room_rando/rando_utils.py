import os
from dotenv import load_dotenv

from .room_node import RoomNode
from .warp_node import WarpNode
from .connec_node import ConnecNode
from treelib import Node, Tree
from .rooms import ROOMS


load_dotenv()
DIRECTORY = os.getenv("MAPS_DIRECTORY")


class NodeID:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1


node_id = NodeID()


# ----------------------------------------------------------------------------- 
def edit_entry_room(
        warp_node: WarpNode,
        file_lines: list[str]
):
    inject_warp_info(
            file_lines=file_lines,
            target_warp=warp_node.entry,
            exit_room=warp_node.exit_room,
            dest_warp_id=warp_node.new_entry_dest_id
    )
    for entry_pair in warp_node.entry_warp_pairs:
        inject_warp_info(
            file_lines=file_lines,
            target_warp=entry_pair,
            exit_room=warp_node.exit_room,
            dest_warp_id=warp_node.new_entry_dest_id
        )


def edit_exit_room(
        warp_node: WarpNode,
        file_lines: list[str]
):
    inject_warp_info(
            file_lines=file_lines,
            target_warp=warp_node.exit,
            exit_room=warp_node.entry_room,
            dest_warp_id=warp_node.new_exit_dest_id
    )
    for exit_pair in warp_node.exit_warp_pairs:
        inject_warp_info(
            file_lines=file_lines,
            target_warp=exit_pair,
            exit_room=warp_node.entry_room,
            dest_warp_id=warp_node.new_exit_dest_id
        )


def link_doors(
        warp_node: WarpNode
):
    entry_file_path = DIRECTORY + '\\' + warp_node.entry_room["file_name"] + '\\map.json'
    entry_file = open(entry_file_path, mode='r')
    entry_file_lines = entry_file.readlines()
    entry_file.close()

    if f"{warp_node.entry_room['file_name']}" in entry_file_lines[2]:
        edit_entry_room(warp_node, entry_file_lines)
    else:
        print("FAILED TO FIND ENTRY ROOM FILE!")     

    entry_file = open(entry_file_path, mode='w')
    entry_file.writelines(entry_file_lines)
    entry_file.close()

    exit_file_path = DIRECTORY + '\\' + warp_node.exit_room["file_name"] + '\\map.json'
    exit_file = open(exit_file_path, mode='r')
    exit_file_lines = exit_file.readlines()
    exit_file.close()

    if f"{warp_node.exit_room['file_name']}" in exit_file_lines[2]:
        edit_exit_room(warp_node, exit_file_lines)
    else:
        print("FAILED TO FIND EXIT ROOM FILE!")

    exit_file = open(exit_file_path, mode='w')
    exit_file.writelines(exit_file_lines)
    exit_file.close()


def is_target_warp(
        target_warp: dict,
        file_lines: list[str],
        index: int
) -> bool:
    return (
        f'"x": {target_warp["x"]},' in file_lines[index - 3] and
        f'"y": {target_warp["y"]},' in file_lines[index - 2]
    )


def inject_warp_info(
        file_lines: list[str],
        target_warp: dict,
        exit_room: dict,
        dest_warp_id: int
):
    for index, line in enumerate(file_lines):
        if f'\"dest_map\":' in line and is_target_warp(target_warp, file_lines, index):
            exit_room_value_index = line.find(':') + 1
            file_lines[index] = line[:exit_room_value_index] \
                + f' "{exit_room["id"]}",\n'
            
            dest_warp_id_index = file_lines[index + 1].find(':') + 1
            file_lines[index + 1] = file_lines[index + 1][:dest_warp_id_index] \
                + f' "{str(dest_warp_id)}"\n'
# -----------------------------------------------------------------------------


def is_good_entry(entry: Node, acc_key_items):
    if entry.data.req_items is not None:
        item_check = all if entry.data.requires_all else any
        return item_check(item in acc_key_items for item in entry.data.req_items)
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


def build_room(room: dict, debug: bool = False):
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
            if debug:
                print(f'\tAdding warp from: {room["alias"]} -> {warp["dest_map"]}')

    for connection in room['connections']:
        create_connec_node(
            tree=room_tree, parent=room_root,
            connec=connection, terminus=False
        )
        if debug:
            print(f'\tAdding connec from: {room["alias"]} -> (Direct to {connection[0]})')

    return room_tree


def is_trimmable_warp(
        leaf: Node,
        room_parent: Node
):
    return (
        leaf.data.is_warp and room_parent.data.is_warp and \
        leaf.data.entry['pair_id'] == room_parent.data.exit['pair_id']
    )


def is_trimmable_connec(
        leaf: Node,
        room_parent: Node
):
    return (
        leaf.data.is_connec and room_parent.data.is_connec and \
        leaf.data.exit == room_parent.data.entry
    )


def trim_room_tree(
        room_tree: Tree, 
        room_parent: Node, 
        avail_room_indecies: list, 
        debug: bool = False
):
    for leaf in room_tree.leaves():
        if is_trimmable_warp(leaf, room_parent):
            if room_tree.remove_node(leaf.identifier) > 1:
                if debug:
                    print('*** removed too many nodes!')
            elif debug:
                print('\tRemoving existing warp:', leaf.data.node_alias)

        elif leaf.data.is_connec and room_parent.data.is_connec:
            if leaf.data.exit == room_parent.data.entry:
                if room_tree.remove_node(leaf.identifier) > 1:
                    if debug:
                        print('*** removed too many nodes!')
                else:
                    if debug:
                        print('\tRemoving existing connection:', leaf.data.node_alias)
            elif rooms_data_from_alias(leaf.data.exit, give_index=True) \
                    not in avail_room_indecies:
                leaf.data.is_terminus = True

    for leaf in room_tree.leaves():  # Can this function silently add connection subverts?
        if leaf.is_root():
            leaf.data.is_terminus = True


def create_warp_node(tree: Tree, parent: Node, warp: dict = None):
    tree.create_node(
        tag=f'to {warp["dest_map"]}', identifier=node_id.value,
        data=WarpNode(entry_warp=warp, entry_room=parent.data.room), parent=parent.identifier
    )
    # tree.get_node(node_id.value).data.add_entry_warp_pairs(parent.data.room)
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
