from treelib import Node, Tree

from .node_manager import NodeManager
from .warp_node import WarpNode
from .connec_node import ConnecNode
from .room_node import RoomNode
from .map_state import MapState


class RandoMap():
    def __init__(self):
        self.tree = Tree()
        self.node_manager = NodeManager()
        self.map_state = MapState()


    # -------------------------------------------------------------------------
    def create_warp_node(
            self,
            tree: Tree, 
            parent: Node, 
            warp: dict = None
    ):
        tree.create_node(
            tag=f'to {warp["dest_map"]}', 
            identifier=self.node_manager.assign_id(),
            data=WarpNode(entry_warp=warp, entry_room=parent.data.room), 
            parent=parent.identifier
        )
        # tree.get_node(node_id.value).data.add_entry_warp_pairs(parent.data.room)

    def create_connec_node(
            self,
            tree: Tree, 
            parent: Node, 
            connec: tuple, 
            terminus: bool = False
    ):
        tree.create_node(
            tag=f'Direct to {connec[0]}', 
            identifier=self.node_manager.assign_id(),
            data=ConnecNode(
                connec, 
                entry=parent.data.node_alias, 
                terminus=terminus
            ),
            parent=parent.identifier
        )

    def build_new_room(
            self, 
            room: dict, 
            debug: bool = False
    ):
        room_tree = Tree()
        root_id = self.node_manager.assign_id()
        room_tree.create_node(
            tag=room['alias'], 
            identifier=root_id,
            data=RoomNode(room), 
            parent=None
        )

        used_pair_ids = []
        room_root = room_tree.get_node(root_id)
        for warp in room['warps']:
            if 'pair_id' not in warp:
                continue

            if warp['pair_id'] not in used_pair_ids:
                self.create_warp_node(
                    tree=room_tree, 
                    parent=room_root, 
                    warp=warp
                )
                used_pair_ids.append(warp['pair_id'])
                if debug:
                    print(f'\tAdding warp from: {room["alias"]} \
                          -> {warp["dest_map"]}')

        for connection in room['connections']:
            self.create_connec_node(
                tree=room_tree, parent=room_root,
                connec=connection, terminus=False
            )
            if debug:
                print(f'\tAdding connec from: {room["alias"]} \
                      -> (Direct to {connection[0]})')

        return room_tree
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
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
            self,
            room_tree: Tree, 
            room_parent: Node, 
            avail_room_indecies: list, 
            debug: bool = False
    ):
        for leaf in room_tree.leaves():
            if self.is_trimmable_warp(leaf, room_parent):
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
                            print('\tRemoving existing connection:', 
                                  leaf.data.node_alias)
                elif rooms_data_from_alias(leaf.data.exit, give_index=True) \
                        not in avail_room_indecies:
                    leaf.data.is_terminus = True

        for leaf in room_tree.leaves():  # Can this silently add subverts?
            if leaf.is_root():
                leaf.data.is_terminus = True
    # -------------------------------------------------------------------------
