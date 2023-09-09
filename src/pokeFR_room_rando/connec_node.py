from .transition_node import TransitionNode


class ConnecNode(TransitionNode):
    def __init__(self, connection: tuple, entry: str):
        super().__init__()
        self.entry = entry
        self.exit = connection[0]
        self.req_items = connection[1]
        self.requires_all = connection[2]
        self.reqs_met = True

    def add_exit(self, exit_room: dict):
        self.exit = exit_room

    @property
    def node_alias(self):
        if self.is_terminus:
            return f'[Direct to {self.exit}]'
        else:
            return f'(Direct to {self.exit})'
