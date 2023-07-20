from .rooms import ROOMS
from .backup_rooms import BACKUPS


class WarpNode:
    def __init__(
            self,
            entry_warp: dict = None,
            entry_room: dict = None,
    ):
        self.entry = entry_warp
        self.entry_room = entry_room
        self.new_entry_dest_id = 0

        self.exit = None
        self.exit_room = None
        self.new_exit_dest_id = 0

        self.entry_warp_pairs = []
        self.exit_warp_pairs = []
        self.is_warp = True
        self.is_connec = False

        self.add_entry_warp_pairs(entry_room)
        self.find_new_exit_warp_id()

    @property
    def node_alias(self):
        if self.exit is None:
            return f'({self.entry["dest_map"][4:]} -> )'
        return f'({self.entry["dest_map"][4:]} -> {self.exit["dest_map"][4:]})'

    # add loop that checks the dummy room
    def find_new_exit_warp_id(self):
        found_id = False
        for room in ROOMS:
            if found_id:
                break
            if room["id"] == self.entry["dest_map"]:
                for warp in room["warps"]:
                    if "pair_id" in warp:
                        if warp["pair_id"] == self.entry["pair_id"]:
                            self.new_exit_dest_id = warp["dest_warp_id"]
                            found_id = True
                            break
        if not found_id:
            for warp in ROOMS[-1]["warps"]:
                if "pair_id" in warp:
                    if warp["pair_id"] == self.entry["pair_id"]:
                        self.new_exit_dest_id = warp["dest_warp_id"]
                        found_id = True
                        break
        if not found_id:
            for warp in BACKUPS[-1]["warps"]:
                if "pair_id" in warp:
                    if warp["pair_id"] == self.entry["pair_id"]:
                        self.new_exit_dest_id = warp["dest_warp_id"]
                        break

    def add_exit_warp(self, exit_warp: dict, exit_room: dict):
        self.exit = exit_warp
        self.exit_room = exit_room
        self.find_new_entry_warp_id()

    # add loop that checks the dummy room !!!!!!!!!
    def find_new_entry_warp_id(self):
        found_id = False
        for room in ROOMS:
            if found_id:
                break
            if room["id"] == self.exit["dest_map"]:
                for warp in room["warps"]:
                    if "pair_id" in warp:
                        if warp["pair_id"] == self.exit["pair_id"]:
                            self.new_entry_dest_id = warp["dest_warp_id"]
                            found_id = True
                            break
        if not found_id:
            for warp in ROOMS[-1]["warps"]:
                if "pair_id" in warp:
                    if warp["pair_id"] == self.exit["pair_id"]:
                        self.new_entry_dest_id = warp["dest_warp_id"]
                        found_id = True
                        break
        if not found_id:
            for warp in BACKUPS[-1]["warps"]:
                if "pair_id" in warp:
                    if warp["pair_id"] == self.exit["pair_id"]:
                        self.new_entry_dest_id = warp["dest_warp_id"]
                        break

    def add_entry_warp_pairs(self, room: dict):
        warp_pairs = []
        for warp in room['warps']:
            if warp == self.entry:
                continue
            if 'pair_id' in warp:
                if warp['pair_id'] == self.entry['pair_id']:
                    warp_pairs.append(warp)
        self.entry_warp_pairs = warp_pairs

    def add_exit_warp_pairs(self, room: dict):
        warp_pairs = []
        for warp in room['warps']:
            if warp == self.exit:
                continue
            if 'pair_id' in warp:
                if warp['pair_id'] == self.exit['pair_id']:
                    warp_pairs.append(warp)
        self.exit_warp_pairs = warp_pairs
