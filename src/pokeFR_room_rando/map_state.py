from treelib import Tree
from .rooms import ROOMS
from .backup_rooms import BACKUPS
from .connec_node import ConnecNode


class MapState:
    def __init__(
            self,
            debug: bool = False,
            rooms: int = 0,
            rooms_not: int = 0,
            doors: int = 0,
            doors_not: int = 0,
            key_item_locks: int = 0,
            open_connections: int = 0
    ):
        self.debug = debug

        self.rooms = rooms
        self.rooms_not = rooms_not

        self.doors = doors
        self.doors_not = doors_not

        self.curr_connecs = []
        self.open_connections = open_connections
        self.key_item_locks = key_item_locks
        self.locked_doors = []
        self.connec_subverts = 0

        self.acc_key_items = []
        self.unacc_key_items = []

        self.lp_rooms_remaining = 0

        self.avail_room_indecies = []
        self.avail_backups_indecies = []

        self.item_prereqs = (
            ("hm01_cut", ("badge2",)), ("hm02_fly", ("badge3",)),
            ("hm03_surf", ("badge5",)), ("hm04_strength", ("badge4", "gold_teeth")),
            ("hm05_flash", ("badge1",)), ("hm06_rocksmash", ("badge6",)),
            ("bike", ("bike_voucher",))
        )

        # self.state_history = []

    @property
    def door_value(self):
        return self.doors - 2 * self.rooms

    @property
    def door_value_not(self):
        return self.doors_not - 2 * self.rooms_not

    @property
    def avail_doors(self):
        return self.door_value + 2 - 2*self.connec_subverts

    @property
    def avail_doors_not(self):
        return self.door_value_not + 2

    @property
    def free_ends(self):
        return self.avail_doors - self.key_item_locks  # - self.open_connections

    def build_initial_state(self, rooms: tuple):
        """
        Creates the initial state of the map based on available rooms in the game.
        All values relevant to MapState are loaded from the provided "rooms" object.

        :param rooms: A tuple containing dictionaries of room data for rooms used in the game.
        :return: None (all values are loaded into the MapState member variables)
        """
        total_rooms_not = 0
        total_doors_not = 0
        for room in rooms:
            doordelta = MapState.doors_in_room(room)
            if doordelta > 0:
                total_rooms_not += 1
                total_doors_not += doordelta
                if 'low_priority' in room:
                    self.lp_rooms_remaining += 1

        self.rooms_not += total_rooms_not
        self.doors_not += total_doors_not

    @staticmethod
    def doors_in_room(room: dict):
        pair_ids = []
        if 'skip' in room:
            return 0
        for warp in room['warps']:
            if 'pair_id' in warp and 'skip' not in warp:
                pair_ids.append(warp['pair_id'])
        for connec in room['connections']:
            if connec[0] is not None:
                pair_ids.append(connec[0])
        return len(set(pair_ids))

    @staticmethod
    def rooms_req_items(room: dict):
        locks = []
        for warp in room['warps']:
            if 'pair_id' in warp and 'skip' not in warp:
                if 'req_items' in warp:
                    for item in warp['req_items']:
                        locks.append(item)
        for connec in room['connections']:
            if connec[0] is not None and connec[1] is not None:
                for item in connec[1]:
                    locks.append(item)
        return locks

    @staticmethod
    def rooms_key_item_locks(room: dict):
        num_locks = 0
        for warp in room['warps']:
            if 'pair_id' in warp and 'skip' not in warp:
                if 'req_items' in warp:
                    num_locks += 1
        for connec in room['connections']:
            if connec[0] is not None and connec[1] is not None:
                num_locks += 1
        return num_locks

    @staticmethod
    def room_doors_data(room: dict):
        unique_doors = []
        locked_doors = []

        if 'skip' not in room:
            for warp in room['warps']:
                if 'pair_id' in warp and 'skip' not in warp:
                    unique_doors.append(warp['pair_id'])

            for connec in room['connections']:
                unique_doors.append(connec[0])
                if connec[1] is not None:
                    locked_doors.append(connec[1])

        return len(set(unique_doors)), locked_doors

    @staticmethod
    def num_warps(room: dict):
        unique_warps = []
        for warp in room['warps']:
            if 'pair_id' in warp and 'skip' not in warp:
                unique_warps.append(warp['pair_id'])
        return len(set(unique_warps))

    def is_connec_locked(self, connec: tuple) -> bool:
        if connec[1] is None:
            return False
        for item in connec[1]:
            if item in self.acc_key_items:
                return False
        return True

    def new_connecs_in_room(self, room: dict) -> list:
        new_connecs = []
        for connec in room['connections']:
            if {room['alias'], connec[0]} not in self.curr_connecs:
                new_connecs.append(connec)
                # self.curr_connecs.append({room['alias'], connec[0]})

        return new_connecs

    def room_data(self, room: dict):
        doors = []
        new_connecs = []
        locked_connecs = []

        for warp in room['warps']:
            if 'pair_id' in warp and warp['pair_id'] not in doors:
                doors.append(warp['pair_id'])
        num_warps = len(doors)

        for connec in room['connections']:
            doors.append(connec[0])
            if {room['alias'], connec[0]} not in self.curr_connecs:
                new_connecs.append(connec)
                if connec[1] is not None:
                    for item in connec[1]:
                        if item not in self.acc_key_items:
                            locked_connecs.append(connec)

        return len(doors), num_warps, new_connecs, locked_connecs

    def update_state(self, room_tree: Tree, room: dict):
        # doors_in_room = MapState.doors_in_room(room)
        doors_in_room, _1, _2, _3 = self.room_data(room)
        self.rooms += 1
        self.rooms_not -= 1
        self.doors += doors_in_room
        self.doors_not -= doors_in_room

        if 'low_priority' in room:
            self.lp_rooms_remaining -= 1

        # if the room has key items
        for key_item in room['key_items']:
            # make it known that the item is accessible
            self.acc_key_items.append(key_item)

            # if the key item was inaccessible,
            #   remove the key item from the inaccessibles list
            if key_item in self.unacc_key_items:
                self.unacc_key_items.remove(key_item)

            # for all locked doors currently listed
            for lock in list(self.locked_doors):
                # if the new key item is required to enter the room,
                #   mark the door as unlocked
                if key_item in lock:
                    self.locked_doors.remove(lock)
                    self.key_item_locks -= 1
                    self.open_connections += 1
            if self.debug:
                print('\t\tAdding new key item:', key_item)

        for leaf in room_tree.leaves():
            # if leaf is root, it's the only piece of the tree, so it's a dead end
            if leaf.is_root():
                continue
            if type(leaf.data) is ConnecNode:
            # if leaf.data.is_connec:
                # the other end of the connec exists somewhere
                if {leaf.data.entry, leaf.data.exit} in self.curr_connecs:
                    leaf.data.is_terminus = True
                    self.connec_subverts += 1
                    if self.debug:
                        print(f"Incrementing subverts; {(leaf.data.entry, leaf.data.exit)}")
                    # self.doors -= 2
                    if leaf.data.req_items is not None:
                        if self.is_connec_locked((leaf.data.exit, leaf.data.req_items)):
                            self.key_item_locks -= 1
                            self.locked_doors.remove(leaf.data.req_items)
                        else:
                            self.open_connections -= 1
                    else:
                        self.open_connections -= 1
                # if this is the first occurrence of this connec
                else:
                    self.curr_connecs.append({leaf.data.entry, leaf.data.exit})
                    # if the connec has req_items to cross
                    if leaf.data.req_items is not None:
                        # if the connec is currently impassable
                        if self.is_connec_locked((leaf.data.exit, leaf.data.req_items)):
                            self.key_item_locks += 1
                            self.locked_doors.append(leaf.data.req_items)
                            for item in leaf.data.req_items:
                                if item not in self.unacc_key_items:
                                    self.unacc_key_items.append(item)
                        # if the conenc IS passable
                        else:
                            self.open_connections += 1
                    # if the connec is open to begin with
                    else:
                        self.open_connections += 1

    def is_good_exit(self, exit_room: dict):
        num_doors, num_warps, new_connecs, new_locks = self.room_data(exit_room)
        room_free_ends = num_warps + len(new_connecs) - len(new_locks)

        if MapState.num_warps(exit_room) == 1 and len(new_connecs) > 0:  # add condition to verify the other end of the connection doesn't already exist (?)
            if not self.good_connec_chain(room=exit_room, chain=[]):
                if self.debug:
                    print('\tBAD CONNEC CHAIN:', exit_room['alias'])
                return False

        if 'low_priority' in exit_room:
            if self.lp_rooms_remaining - 1 < 2*self.connec_subverts:  # This was originally 2*, but i think 1* will work.
                return False
            elif self.avail_doors > self.lp_rooms_remaining - 1:
                return False
            else:
                if self.debug:
                    print("\tAdding low-priority room")

        if exit_room in BACKUPS:
            if self.free_ends + room_free_ends > self.lp_rooms_remaining:  # maybe replace "room_free_ends" with "num_doors" ?
                return False

        # if self.free_ends < 5:  # If the number of available doorways is low, make sure new subverts don't close the map prematurely
        new_subverts = self.new_connec_subverts(room=exit_room, chain=[])
        if self.connec_subverts + new_subverts > 18:  # self.free_ends - 2*new_subverts < 1:
            if self.debug:
                print("\n\ntoo many connec subverts found\n\n", new_subverts)
            return False

        for key_item in exit_room['key_items']:
            for item in self.item_prereqs:
                if key_item == item[0]:
                    for prereq in item[1]:
                        if prereq not in self.acc_key_items:
                            return False
            for door in self.locked_doors:
                if key_item in door:
                    room_free_ends += 1

        # if number of currently accessible doorways in the map
        #   plus the prospective room's accessible doorways
        #   minus the 2 doorways used to make the connection
        #   is more than zero, then the map will not close prematurely
        #   and the exit is good
        if self.free_ends + room_free_ends - 2 > 1:
            return True

        elif len(self.avail_room_indecies) - self.lp_rooms_remaining == self.avail_doors:
            return True

        # if the number of currently accessible doorways in the map
        #   is equal to the number of available doorways NOT in the map
        #   and the number of rooms NOT in the map is 1
        #   then the room is okay to add, and the map will be closed
        # elif self.avail_doors == self.avail_doors_not and self.rooms_not == 1:
        #     return True

        # none of the above are true, so the room in question is no good,
        #   as it will close the map prematurely
        else:
            if self.debug:
                print('\tBAD ROOM CHOICE:', exit_room['alias'])
            return False

    # have this method run in "is_good_exit" if the number of warps in the exit room is 1, and the
    #   number of new connections is not zero.
    # this method should prevent accidental lockouts due to deadends resulting from connections
    #   looping back into existing rooms
    def good_connec_chain(self, room: dict, chain: list, secondary_room: bool = False):
        connecs_in_chain = chain

        if MapState.num_warps(room) > 1 - secondary_room:
            if self.debug:
                print('\t\troom had sufficient warps')
            return True
        else:
            connecs = []
            for connec in room['connections']:
                if {room['alias'], connec[0]} not in self.curr_connecs \
                        and {room['alias'], connec[0]} not in connecs_in_chain:
                    if connec[1] is None or self.have_connec_reqs(req_items=connec[1]):
                        connecs.append((room['alias'], connec[0]))  # can this be simpler (connec[0])?
                        connecs_in_chain.append({room['alias'], connec[0]})

            for connec in connecs:
                next_room = None
                for r in ROOMS:
                    if r['alias'] == connec[1]:
                        next_room = r
                        break
                if next_room is None:
                    for r in BACKUPS:
                        if r['alias'] == connec[1]:
                            next_room = r
                            break
                if self.debug:
                    print(next_room, connec)
                    print('\t\tMoving to next room in chain:', next_room['alias'])
                if self.good_connec_chain(
                        room=next_room, chain=connecs_in_chain, secondary_room=True
                ):
                    return True

        return False

    def new_connec_subverts(self, room: dict, chain: list):
        new_subverts = 0
        connec_chain = chain
        for connec in room["connections"]:
            if {room["alias"], connec[0]} not in connec_chain:
                connec_chain.append({room["alias"], connec[0]})
                if {room["alias"], connec[0]} in self.curr_connecs:
                    new_subverts += 1
                    if self.debug:
                        print(f"\tNew Subvert: {(room['alias'], connec[0])}")
                else:
                    next_room = None
                    for r in ROOMS:
                        if r["alias"] == connec[0]:
                            next_room = r
                            break
                    new_subverts += self.new_connec_subverts(next_room, connec_chain)

        return new_subverts

    def have_connec_reqs(self, req_items: tuple):
        for item in req_items:
            if item in self.acc_key_items:
                return True
        return False

    def halt_process(self):
        if self.avail_doors < 1:
            if self.debug:
                print(f"{self.avail_doors = }")
            return True
        return False

    def display_state(self):
        print(f'\tRooms in rando: {self.rooms}')
        print(f'\tRooms NOT in rando: {self.rooms_not}')
        print(f'\tDoors in rando: {self.doors}')
        print(f'\tDoors NOT in rando: {self.doors_not}')
        print(f'\tDoor Value in rando: {self.door_value}')
        print(f'\tDoor Value NOT in rando: {self.door_value_not}')
        print(f'\tAvailable doorways in map: {self.avail_doors}')
        print(f'\tAvailable doorways NOT in map: {self.avail_doors_not}')
        print('\nKey items:', self.acc_key_items)
        print('Entries locked by key_items:', self.key_item_locks)
        print('Current open connections:', self.open_connections)
        print('\nMissing Items:', self.unacc_key_items)
        print('\nLocked doors:', len(self.locked_doors), self.locked_doors)
        print('\nConnection Subverts:', self.connec_subverts)
        print(f'{self.lp_rooms_remaining = }')
