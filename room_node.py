class RoomNode:
    def __init__(
            self,
            room: dict
    ):
        self.room = room
        self.room_id = room['id']
        self.node_alias = room['alias']
        self.room_filename = room['file_name']
        self.key_items = room['key_items']
        self.warps = room['warps']
        self.connections = room['connections']
        self.warp_pairs = []
        self.is_terminus = False

        warp_count = 0
        connec_count = 0
        used_ids = []
        for warp in self.warps:
            if 'pair_id' in warp and warp['pair_id'] not in used_ids:
                warp_count += 1
                used_ids.append(warp['pair_id'])
        for connection in self.connections:
            if connection[0] is not None:
                connec_count += 1
        if warp_count + connec_count == 1:
            self.is_terminus = True

    def add_warp_pair(
            self,
            entry_warp: dict,
            exit_warp: dict,
            exit_room_warps: tuple
    ) -> bool:
        for warp_pair in self.warp_pairs:
            if entry_warp['pair_id'] == warp_pair[0]['pair_id']:
                return False

        if entry_warp in self.warps:
            self.warp_pairs.append((entry_warp, exit_warp))
            for warp in self.warps:
                if 'pair_id' in warp and warp != entry_warp:
                    if warp['pair_id'] == entry_warp['pair_id']:
                        self.warp_pairs.append((warp, exit_warp))
            for warp in exit_room_warps:
                if 'pair_id' in warp and warp != exit_warp:
                    if warp['pair_id'] == exit_warp['pair_id']:
                        self.warp_pairs.append((entry_warp, warp))
        else:
            print('\n-!- TRIED TO ADD IMPROPER WARP PAIRING\n')

        return True
