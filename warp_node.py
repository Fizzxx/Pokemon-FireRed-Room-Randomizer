class WarpNode:
    def __init__(
            self,
            entry_warp: dict = None,
            entry_warp_pairs: tuple = (),
            exit_warp_pairs: tuple = ()
    ):
        self.entry = entry_warp
        self.exit = None
        self.entry_warp_pairs = entry_warp_pairs
        self.exit_warp_pairs = exit_warp_pairs
        # self.node_alias = f'({self.entry["dest_map"][4:]} -> {self.exit["dest_map"][4:]})'
        self.is_warp = True
        self.is_connec = False
        # self.requires_all = True
        # self.reqs_met = True
        # if 'req_items' in entry_warp:
        #     self.req_items = entry_warp['req_items']
        #     self.requires_all = entry_warp['requires_all']
        # else:
        #     self.req_items = None

    @property
    def node_alias(self):
        if self.exit is None:
            return f'({self.entry["dest_map"][4:]} -> )'
        return f'({self.entry["dest_map"][4:]} -> {self.exit["dest_map"][4:]})'

    def add_exit_warp(self, warp: dict):
        self.exit = warp

    def add_entry_warp_pairs(self, room: dict):
        warp_pairs = []
        for warp in room['warps']:
            if 'pair_id' in warp:
                if warp['pair_id'] == self.entry['pair_id']:
                    warp_pairs.append(warp)

    def add_exit_warp_pairs(self, room: dict):
        warp_pairs = []
        for warp in room['warps']:
            if warp == self.exit:
                continue
            if 'pair_id' in warp:
                if warp['pair_id'] == self.exit['pair_id']:
                    warp_pairs.append(warp)

