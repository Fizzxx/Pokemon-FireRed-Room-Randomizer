class ConnecNode:
    def __init__(self, connection: tuple, entry: str, terminus=False):
        self.entry = entry
        self.exit = connection[0]
        # self.node_alias = f'(Direct to {self.exit})'
        self.is_warp = False
        self.is_connec = True
        self.req_items = connection[1]
        self.requires_all = connection[2]
        self.reqs_met = True
        self.is_terminus = terminus

    def add_exit(self, exit_room: dict):
        self.exit = exit_room

    @property
    def node_alias(self):
        if self.is_terminus:
            return f'[Direct to {self.exit}]'
        else:
            return f'(Direct to {self.exit})'
