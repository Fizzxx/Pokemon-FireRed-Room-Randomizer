from .transition_node import TransitionNode
from .rooms import ROOMS
from .backup_rooms import BACKUPS


class WarpNode(TransitionNode):
    def __init__(self, entry_warp: dict = None, entry_room: dict = None):
        super().__init__()
        self.entry = entry_warp
        self.entry_room = entry_room
        self.new_entry_dest_id = 0
        self.entry_warp_pairs = self.find_warp_pairs(self.entry_room, self.entry)

        self.exit_room = None
        self.new_exit_dest_id = self.find_new_dest_id(self.entry)
        self.exit_warp_pairs = []

    @property
    def node_alias(self):
        if self.exit is None:
            return f'({self.entry["dest_map"][4:]} -> )'
        return f'({self.entry["dest_map"][4:]} -> {self.exit["dest_map"][4:]})'

    def find_warp_pairs(self, warp_room: dict, warp_to_match: dict):
        warp_pairs = []
        for warp in warp_room['warps']:
            if warp == warp_to_match:
                continue
            if 'pair_id' in warp and warp['pair_id'] == warp_to_match['pair_id']:
                warp_pairs.append(warp)
        return warp_pairs
    
    # -------------------------------------------------------------------------
    def check_room_for_warp_match(
            self,
            warp_to_match: dict,
            room_warps: dict
    ) -> int:
        for warp in room_warps:
            if "pair_id" in warp and warp["pair_id"] == warp_to_match["pair_id"]:
                return warp["dest_warp_id"]
        return -1

    def search_collection_for_new_exit_warp_id(
            self,
            warp_to_match: dict,
            collection: tuple
    ) -> int:
        for room in collection:
            if room["id"] == warp_to_match["dest_map"]:
                new_warp_id = self.check_room_for_warp_match(
                    warp_to_match,
                    room["warps"]
                )
                if new_warp_id > -1:
                    return new_warp_id
                
        dummy_room_warps = collection[-1]["warps"]
        new_warp_id = self.check_room_for_warp_match(
                warp_to_match,
                dummy_room_warps
            )
        if new_warp_id > -1:    
            return new_warp_id
        
        return -1

    # why were we not checking backups as well?
    def find_new_dest_id(self, warp_to_match: dict) -> int:
        for collection in (ROOMS, BACKUPS):
            new_warp_id = self.search_collection_for_new_exit_warp_id(
                    warp_to_match,
                    collection
                )
            if new_warp_id > -1:
                return new_warp_id
        return -1
    # -------------------------------------------------------------------------

    def add_exit_warp(self, exit_warp: dict, exit_room: dict):
        self.exit = exit_warp
        self.exit_room = exit_room
        self.new_entry_dest_id = self.find_new_dest_id(self.exit)
        self.exit_warp_pairs = self.find_warp_pairs(self.exit_room, self.exit)
