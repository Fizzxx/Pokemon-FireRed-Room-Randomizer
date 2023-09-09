import treelib

from .connec_node import ConnecNode
from .warp_node import WarpNode
from .room_node import RoomNode


class NodeManager():
    def __init__(self):
        self.node_id = 0

    def increment_id(self):
        self.node_id += 1

    def assign_id(self) -> int:
        self.increment_id()
        return self.node_id