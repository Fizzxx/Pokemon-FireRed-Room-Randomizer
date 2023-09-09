from .map_node import MapNode


class RoomNode(MapNode):
    def __init__(self, room: dict):
        super().__init__()
        self.room = room
        self.is_terminus = self.is_room_terminus()
    
    @property
    def room_id(self):
        return self.room['id']
    @property
    def node_alias(self):
        return self.room['alias']
    @property
    def room_filename(self):
        return self.room['file_name']
    @property
    def key_items(self):
        return self.room['key_items']
    @property
    def warps(self):
        return self.room['warps']
    @property
    def connections(self):
        return self.room['connections']

    def is_room_terminus(self):
        warp_count = 0
        connec_count = len(self.connections)
        used_ids = []
        for warp in self.warps:
            if 'pair_id' in warp and warp['pair_id'] not in used_ids:
                warp_count += 1
                used_ids.append(warp['pair_id'])
        if warp_count + connec_count == 1:
            return True
        return False