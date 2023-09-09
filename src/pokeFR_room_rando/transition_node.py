from .map_node import MapNode


class TransitionNode(MapNode):
    def __init__(self):
        super().__init__()
        self.entry = None
        self.exit = None
