# This file contains map data for rooms used in constructing world layout.
# Data was systematically ripped from each curr_room's corresponding json files, and reformatted into a dict
# 	for calculations related to curr_room placement and layout verification.
# - Kameron Scott, 2021

ROOMS = (
	{
		"id": "MAP_CELADON_CITY",
		"alias": "CeladonCity",
		"key_items": (),
		"file_name": "CeladonCity",
		"warps": (
			{
				"x": 34,
				"y": 21,
				"elevation": 0,
				"dest_map": "MAP_CELADON_CITY_GAME_CORNER",
				"dest_warp_id": 0,
				"pair_id": 0
			},
			{
				"x": 11,
				"y": 14,
				"elevation": 0,
				"dest_map": "MAP_CELADON_CITY_DEPARTMENT_STORE_1F",
				"dest_warp_id": 1,
				"pair_id": 1
			},
			{
				"x": 15,
				"y": 14,
				"elevation": 0,
				"dest_map": "MAP_CELADON_CITY_DEPARTMENT_STORE_1F",
				"dest_warp_id": 4,
				"pair_id": 2
			},
			{
				"x": 30,
				"y": 11,
				"elevation": 0,
				"dest_map": "MAP_CELADON_CITY_CONDOMINIUMS_1F",
				"dest_warp_id": 1,
				"pair_id": 3
			},
			{
				"x": 48,
				"y": 11,
				"elevation": 0,
				"dest_map": "MAP_CELADON_CITY_POKEMON_CENTER_1F",
				"dest_warp_id": 1,
				"pair_id": 5
			},
			{
				"x": 39,
				"y": 20,
				"elevation": 0,
				"dest_map": "MAP_CELADON_CITY_GAME_CORNER_PRIZE_ROOM",
				"dest_warp_id": 1,
				"pair_id": 6
			},
			# {
			# 	"x": 11,
			# 	"y": 30,
			# 	"elevation": 0,
			# 	"dest_map": "MAP_CELADON_CITY_GYM",
			# 	"dest_warp_id": 1,
			# 	"req_items": ("hm01_cut",),
			# 	"requires_all": True,
			# 	"pair_id": 7
			# },
			{
				"x": 37,
				"y": 29,
				"elevation": 0,
				"dest_map": "MAP_CELADON_CITY_RESTAURANT",
				"dest_warp_id": 1,
				"pair_id": 8
			},
			{
				"x": 41,
				"y": 29,
				"elevation": 0,
				"dest_map": "MAP_CELADON_CITY_HOUSE1",
				"dest_warp_id": 1,
				"pair_id": 9
			},
			{
				"x": 49,
				"y": 29,
				"elevation": 0,
				"dest_map": "MAP_CELADON_CITY_HOTEL",
				"dest_warp_id": 1,
				"pair_id": 10
			},
			{
				"x": 30,
				"y": 4,
				"elevation": 3,
				"dest_map": "MAP_CELADON_CITY_CONDOMINIUMS_1F",
				"dest_warp_id": 5,
				"pair_id": 4
			},
		),
		"connections": (
			("Route16_SE", None),
			("Route7", None),
			("CeladonCity_Gym_with_girls", ("hm01_cut",)),
		),
	},
	{
		"id": "MAP_CELADON_CITY",
		"alias": "CeladonCity_Gym_with_girls",
		"key_items": (),
		"file_name": "CeladonCity",
		"warps": (
			{
				"x": 11,
				"y": 30,
				"elevation": 0,
				"dest_map": "MAP_CELADON_CITY_GYM",
				"dest_warp_id": 1,
				# "req_items": ("hm01_cut",),
				# "requires_all": True,
				"pair_id": 7
			},
		),
		"connections": (
			("CeladonCity", ("hm01_cut",)),
		),
	},
	{
		"id": "MAP_CELADON_CITY_CONDOMINIUMS_1F",
		"alias": "CeladonCity_Condominiums_1F",
		"key_items": ("tea",),
		"file_name": "CeladonCity_Condominiums_1F",
		"warps": (
			{
				"x": 12,
				"y": 18,
				"elevation": 3,
				"dest_map": "MAP_CELADON_CITY",
				"dest_warp_id": 3,
				"pair_id": 3
			},
			{
				"x": 12,
				"y": 2,
				"elevation": 3,
				"dest_map": "MAP_CELADON_CITY_CONDOMINIUMS_2F",
				"dest_warp_id": 3,
				"pair_id": 12
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_CELADON_CITY_CONDOMINIUMS_1F",
		"alias": "CeladonCity_Condominiums_1F_Stairway",
		"key_items": (),
		"file_name": "CeladonCity_Condominiums_1F",
		"warps": (
			{
				"x": 4,
				"y": 2,
				"elevation": 3,
				"dest_map": "MAP_CELADON_CITY_CONDOMINIUMS_2F",
				"dest_warp_id": 0,
				"pair_id": 11
			},
			{
				"x": 2,
				"y": 1,
				"elevation": 3,
				"dest_map": "MAP_CELADON_CITY",
				"dest_warp_id": 11,
				"pair_id": 4
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_CELADON_CITY_CONDOMINIUMS_2F",
		"alias": "CeladonCity_Condominiums_2F_Stairway",
		"key_items": (),
		"file_name": "CeladonCity_Condominiums_2F",
		"warps": (
			{
				"x": 4,
				"y": 2,
				"elevation": 3,
				"dest_map": "MAP_CELADON_CITY_CONDOMINIUMS_1F",
				"dest_warp_id": 3,
				"pair_id": 11
			},
			{
				"x": 2,
				"y": 2,
				"elevation": 3,
				"dest_map": "MAP_CELADON_CITY_CONDOMINIUMS_3F",
				"dest_warp_id": 0,
				"pair_id": 13
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_CELADON_CITY_CONDOMINIUMS_2F",
		"alias": "CeladonCity_Condominiums_2F",
		"key_items": (),
		"file_name": "CeladonCity_Condominiums_2F",
		"warps": (
			{
				"x": 11,
				"y": 2,
				"elevation": 3,
				"dest_map": "MAP_CELADON_CITY_CONDOMINIUMS_3F",
				"dest_warp_id": 3,
				"pair_id": 14
			},
			{
				"x": 12,
				"y": 2,
				"elevation": 3,
				"dest_map": "MAP_CELADON_CITY_CONDOMINIUMS_1F",
				"dest_warp_id": 4,
				"pair_id": 12
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_CELADON_CITY_CONDOMINIUMS_3F",
		"alias": "CeladonCity_Condominiums_3F_Stairway",
		"key_items": (),
		"file_name": "CeladonCity_Condominiums_3F",
		"warps": (
			{
				"x": 2,
				"y": 2,
				"elevation": 3,
				"dest_map": "MAP_CELADON_CITY_CONDOMINIUMS_2F",
				"dest_warp_id": 1,
				"pair_id": 13
			},
			{
				"x": 4,
				"y": 2,
				"elevation": 3,
				"dest_map": "MAP_CELADON_CITY_CONDOMINIUMS_ROOF",
				"dest_warp_id": 0,
				"pair_id": 15
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_CELADON_CITY_CONDOMINIUMS_3F",
		"alias": "CeladonCity_Condominiums_3F",
		"key_items": (),
		"file_name": "CeladonCity_Condominiums_3F",
		"warps": (
			{
				"x": 12,
				"y": 2,
				"elevation": 3,
				"dest_map": "MAP_CELADON_CITY_CONDOMINIUMS_ROOF",
				"dest_warp_id": 1,
				"pair_id": 16
			},
			{
				"x": 11,
				"y": 2,
				"elevation": 3,
				"dest_map": "MAP_CELADON_CITY_CONDOMINIUMS_2F",
				"dest_warp_id": 2,
				"pair_id": 14
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_CELADON_CITY_CONDOMINIUMS_ROOF",
		"alias": "CeladonCity_Condominiums_Roof_Left",
		"key_items": (),
		"file_name": "CeladonCity_Condominiums_Roof",
		"warps": (
			{
				"x": 4,
				"y": 2,
				"elevation": 3,
				"dest_map": "MAP_CELADON_CITY_CONDOMINIUMS_3F",
				"dest_warp_id": 1,
				"pair_id": 15
			},
			{
				"x": 2,
				"y": 12,
				"elevation": 3,
				"dest_map": "MAP_CELADON_CITY_CONDOMINIUMS_ROOF_ROOM",
				"dest_warp_id": 1,
				"pair_id": 17
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_CELADON_CITY_CONDOMINIUMS_ROOF",
		"alias": "CeladonCity_Condominiums_Roof_Right",
		"key_items": (),
		"file_name": "CeladonCity_Condominiums_Roof",
		"warps": (
			{
				"x": 10,
				"y": 2,
				"elevation": 3,
				"dest_map": "MAP_CELADON_CITY_CONDOMINIUMS_3F",
				"dest_warp_id": 2,
				"pair_id": 16
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_CELADON_CITY_CONDOMINIUMS_ROOF_ROOM",
		"alias": "CeladonCity_Condominiums_RoofRoom",
		"key_items": (),
		"file_name": "CeladonCity_Condominiums_RoofRoom",
		"warps": (
			{
				"x": 4,
				"y": 7,
				"elevation": 3,
				"dest_map": "MAP_CELADON_CITY_CONDOMINIUMS_ROOF",
				"dest_warp_id": 2,
				"pair_id": 17
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_CELADON_CITY_DEPARTMENT_STORE_1F",
		"alias": "CeladonCity_DepartmentStore_1F",
		"key_items": (),
		"file_name": "CeladonCity_DepartmentStore_1F",
		"warps": (
			{
				"x": 2,
				"y": 14,
				"elevation": 3,
				"dest_map": "MAP_CELADON_CITY",
				"dest_warp_id": 1,
				"pair_id": 1
			},
			{
				"x": 10,
				"y": 14,
				"elevation": 3,
				"dest_map": "MAP_CELADON_CITY",
				"dest_warp_id": 2,
				"pair_id": 2
			},
			{
				"x": 4,
				"y": 2,
				"elevation": 3,
				"dest_map": "MAP_CELADON_CITY_DEPARTMENT_STORE_2F",
				"dest_warp_id": 1,
				"pair_id": 18
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_CELADON_CITY_DEPARTMENT_STORE_2F",
		"alias": "CeladonCity_DepartmentStore_2F",
		"key_items": (),
		"file_name": "CeladonCity_DepartmentStore_2F",
		"warps": (
			{
				"x": 3,
				"y": 2,
				"elevation": 3,
				"dest_map": "MAP_CELADON_CITY_DEPARTMENT_STORE_1F",
				"dest_warp_id": 7,
				"pair_id": 18
			},
			{
				"x": 9,
				"y": 2,
				"elevation": 3,
				"dest_map": "MAP_CELADON_CITY_DEPARTMENT_STORE_3F",
				"dest_warp_id": 1,
				"pair_id": 19
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_CELADON_CITY_DEPARTMENT_STORE_3F",
		"alias": "CeladonCity_DepartmentStore_3F",
		"key_items": (),
		"file_name": "CeladonCity_DepartmentStore_3F",
		"warps": (
			{
				"x": 9,
				"y": 2,
				"elevation": 0,
				"dest_map": "MAP_CELADON_CITY_DEPARTMENT_STORE_2F",
				"dest_warp_id": 2,
				"pair_id": 19
			},
			{
				"x": 3,
				"y": 2,
				"elevation": 0,
				"dest_map": "MAP_CELADON_CITY_DEPARTMENT_STORE_4F",
				"dest_warp_id": 1,
				"pair_id": 20
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_CELADON_CITY_DEPARTMENT_STORE_4F",
		"alias": "CeladonCity_DepartmentStore_4F",
		"key_items": (),
		"file_name": "CeladonCity_DepartmentStore_4F",
		"warps": (
			{
				"x": 3,
				"y": 2,
				"elevation": 0,
				"dest_map": "MAP_CELADON_CITY_DEPARTMENT_STORE_3F",
				"dest_warp_id": 2,
				"pair_id": 20
			},
			{
				"x": 9,
				"y": 2,
				"elevation": 0,
				"dest_map": "MAP_CELADON_CITY_DEPARTMENT_STORE_5F",
				"dest_warp_id": 1,
				"pair_id": 21
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_CELADON_CITY_DEPARTMENT_STORE_5F",
		"alias": "CeladonCity_DepartmentStore_5F",
		"key_items": (),
		"file_name": "CeladonCity_DepartmentStore_5F",
		"warps": (
			{
				"x": 9,
				"y": 2,
				"elevation": 3,
				"dest_map": "MAP_CELADON_CITY_DEPARTMENT_STORE_4F",
				"dest_warp_id": 2,
				"pair_id": 21
			},
			{
				"x": 3,
				"y": 2,
				"elevation": 3,
				"dest_map": "MAP_CELADON_CITY_DEPARTMENT_STORE_ROOF",
				"dest_warp_id": 0,
				"pair_id": 22
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_CELADON_CITY_DEPARTMENT_STORE_ELEVATOR",
		"alias": "CeladonCity_DepartmentStore_Elevator",
		"key_items": (),
		"file_name": "CeladonCity_DepartmentStore_Elevator",
		"warps": (
			{
				"x": 2,
				"y": 5,
				"elevation": 3,
				"dest_map": "MAP_NONE",
				"dest_warp_id": 127
			},
			{
				"x": 2,
				"y": 6,
				"elevation": 0,
				"dest_map": "MAP_NONE",
				"dest_warp_id": 127
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_CELADON_CITY_DEPARTMENT_STORE_ROOF",
		"alias": "CeladonCity_DepartmentStore_Roof",
		"key_items": (),
		"file_name": "CeladonCity_DepartmentStore_Roof",
		"warps": (
			{
				"x": 15,
				"y": 6,
				"elevation": 3,
				"dest_map": "MAP_CELADON_CITY_DEPARTMENT_STORE_5F",
				"dest_warp_id": 2,
				"pair_id": 22
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_CELADON_CITY_GAME_CORNER",
		"alias": "CeladonCity_GameCorner",
		"key_items": (),
		"file_name": "CeladonCity_GameCorner",
		"warps": (
			{
				"x": 9,
				"y": 13,
				"elevation": 0,
				"dest_map": "MAP_CELADON_CITY",
				"dest_warp_id": 0,
				"pair_id": 0
			},
			{
				"x": 15,
				"y": 2,
				"elevation": 3,
				"dest_map": "MAP_ROCKET_HIDEOUT_B1F",
				"dest_warp_id": 0,
				"pair_id": 23
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_CELADON_CITY_GAME_CORNER_PRIZE_ROOM",
		"alias": "CeladonCity_GameCorner_PrizeRoom",
		"key_items": (),
		"file_name": "CeladonCity_GameCorner_PrizeRoom",
		"warps": (
			{
				"x": 4,
				"y": 8,
				"elevation": 3,
				"dest_map": "MAP_CELADON_CITY",
				"dest_warp_id": 5,
				"pair_id": 6
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_CELADON_CITY_GYM",
		"alias": "CeladonCity_Gym",
		"key_items": ("badge4",),
		"file_name": "CeladonCity_Gym",
		"warps": (
			{
				"x": 6,
				"y": 18,
				"elevation": 3,
				"dest_map": "MAP_CELADON_CITY",
				"dest_warp_id": 6,
				"pair_id": 7
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_CELADON_CITY_HOTEL",
		"alias": "CeladonCity_Hotel",
		"key_items": (),
		"file_name": "CeladonCity_Hotel",
		"warps": (
			{
				"x": 4,
				"y": 9,
				"elevation": 0,
				"dest_map": "MAP_CELADON_CITY",
				"dest_warp_id": 9,
				"pair_id": 10
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_CELADON_CITY_HOUSE1",
		"alias": "CeladonCity_House1",
		"key_items": (),
		"file_name": "CeladonCity_House1",
		"warps": (
			{
				"x": 4,
				"y": 7,
				"elevation": 3,
				"dest_map": "MAP_CELADON_CITY",
				"dest_warp_id": 8,
				"pair_id": 9
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_CELADON_CITY_POKEMON_CENTER_1F",
		"alias": "CeladonCity_PokemonCenter_1F",
		"key_items": (),
		"file_name": "CeladonCity_PokemonCenter_1F",
		"warps": (
			{
				"x": 7,
				"y": 8,
				"elevation": 3,
				"dest_map": "MAP_CELADON_CITY",
				"dest_warp_id": 4,
				"pair_id": 5
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_CELADON_CITY_RESTAURANT",
		"alias": "CeladonCity_Restaurant",
		"key_items": (),
		"file_name": "CeladonCity_Restaurant",
		"warps": (
			{
				"x": 6,
				"y": 9,
				"elevation": 0,
				"dest_map": "MAP_CELADON_CITY",
				"dest_warp_id": 7,
				"pair_id": 8
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_CERULEAN_CITY",
		"alias": "CeruleanCity",
		"key_items": (),
		"file_name": "CeruleanCity",
		"warps": (
			{
				"x": 10,
				"y": 11,
				"elevation": 0,
				"dest_map": "MAP_CERULEAN_CITY_HOUSE1",
				"dest_warp_id": 1,
				"pair_id": 24
			},
			# {
			# 	"x": 30,
			# 	"y": 11,
			# 	"elevation": 0,
			# 	"dest_map": "MAP_CERULEAN_CITY_HOUSE2",
			# 	"dest_warp_id": 1,
			# 	"req_items": ("ssanne_ticket",),
			# 	"requires_all": True,
			# 	"pair_id": 26
			# },
			{
				"x": 15,
				"y": 17,
				"elevation": 0,
				"dest_map": "MAP_CERULEAN_CITY_HOUSE3",
				"dest_warp_id": 1,
				"pair_id": 31
			},
			{
				"x": 22,
				"y": 19,
				"elevation": 0,
				"dest_map": "MAP_CERULEAN_CITY_POKEMON_CENTER_1F",
				"dest_warp_id": 1,
				"pair_id": 32
			},
			{
				"x": 31,
				"y": 21,
				"elevation": 0,
				"dest_map": "MAP_CERULEAN_CITY_GYM",
				"dest_warp_id": 1,
				"pair_id": 33
			},
			{
				"x": 13,
				"y": 28,
				"elevation": 3,
				"dest_map": "MAP_CERULEAN_CITY_BIKE_SHOP",
				"dest_warp_id": 1,
				"pair_id": 28
			},
			{
				"x": 29,
				"y": 28,
				"elevation": 0,
				"dest_map": "MAP_CERULEAN_CITY_MART",
				"dest_warp_id": 1,
				"pair_id": 34
			},
			# {
			# 	"x": 1,
			# 	"y": 12,
			# 	"elevation": 0,
			# 	"dest_map": "MAP_CERULEAN_CAVE_1F",
			# 	"dest_warp_id": 0,
			# 	"req_items": ("hm03_surf",),
			# 	"requires_all": True,
			# 	"pair_id": 200
			# },
			{
				"x": 14,
				"y": 28,
				"elevation": 3,
				"dest_map": "MAP_CERULEAN_CITY_BIKE_SHOP",
				"dest_warp_id": 1,
				"pair_id": 28
			},
			{
				"x": 23,
				"y": 28,
				"elevation": 0,
				"dest_map": "MAP_CERULEAN_CITY_HOUSE4",
				"dest_warp_id": 0,
				"pair_id": 29
			},
			{
				"x": 17,
				"y": 11,
				"elevation": 0,
				"dest_map": "MAP_CERULEAN_CITY_HOUSE5",
				"dest_warp_id": 0,
				"pair_id": 30
			},
		),
		"connections": (
			("Route24", None),
			("Route4_E", None),
			("CeruleanCity_Exterior", ("hm01_cut",)),
			("CeruleanCity_cop_block", ("ssanne_ticket",)),
		),
	},
	{
		"id": "MAP_CERULEAN_CITY",
		"alias": "CeruleanCity_cop_block",
		"key_items": (),
		"file_name": "CeruleanCity",
		"warps": (
			{
				"x": 30,
				"y": 11,
				"elevation": 0,
				"dest_map": "MAP_CERULEAN_CITY_HOUSE2",
				"dest_warp_id": 1,
				# "req_items": ("ssanne_ticket",),
				# "requires_all": True,
				"pair_id": 26
			},
		),
		"connections": (
			("CeruleanCity", ("ssanne_ticket",)),
		),
	},
	{
		"id": "MAP_CERULEAN_CITY",
		"alias": "CeruleanCity_Cave",
		"key_items": (),
		"file_name": "CeruleanCity",
		"warps": (
			{
				"x": 1,
				"y": 12,
				"elevation": 0,
				"dest_map": "MAP_CERULEAN_CAVE_1F",
				"dest_warp_id": 0,
				# "req_items": ("hm03_surf",),
				# "requires_all": True,
				"pair_id": 200
			},
		),
		"connections": (
			("Route24", ("hm03_surf",)),
			# ("Route4_E", ("hm03_surf",)),
		),
	},
	{
		"id": "MAP_CERULEAN_CITY",
		"alias": "CeruleanCity_Backroom",
		"key_items": (),
		"file_name": "CeruleanCity",
		"warps": (
			{
				"x": 10,
				"y": 8,
				"elevation": 3,
				"dest_map": "MAP_CERULEAN_CITY_HOUSE1",
				"dest_warp_id": 3,
				"pair_id": 25
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_CERULEAN_CITY",
		"alias": "CeruleanCity_Exterior",
		"key_items": (),
		"file_name": "CeruleanCity",
		"warps": (
			{
				"x": 31,
				"y": 8,
				"elevation": 3,
				"dest_map": "MAP_CERULEAN_CITY_HOUSE2",
				"dest_warp_id": 3,
				"pair_id": 27
			},
		),
		"connections": (
			("Route9", ("hm01_cut",)),
			("Route5", None),
			("CeruleanCity", ("hm01_cut",)),
		),
	},
	{
		"id": "MAP_CERULEAN_CITY_BIKE_SHOP",
		"alias": "CeruleanCity_BikeShop",
		"key_items": ("bike",),
		"file_name": "CeruleanCity_BikeShop",
		"warps": (
			{
				"x": 5,
				"y": 8,
				"elevation": 3,
				"dest_map": "MAP_CERULEAN_CITY",
				"dest_warp_id": 5,
				# "req_items": ("bike_voucher",),
				# "requires_all": True,
				"pair_id": 28
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_CERULEAN_CITY_GYM",
		"alias": "CeruleanCity_Gym",
		"key_items": ("badge2",),
		"file_name": "CeruleanCity_Gym",
		"warps": (
			{
				"x": 8,
				"y": 18,
				"elevation": 3,
				"dest_map": "MAP_CERULEAN_CITY",
				"dest_warp_id": 4,
				"pair_id": 33
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_CERULEAN_CITY_HOUSE1",
		"alias": "CeruleanCity_House1",
		"key_items": (),
		"file_name": "CeruleanCity_House1",
		"warps": (
			{
				"x": 3,
				"y": 8,
				"elevation": 3,
				"dest_map": "MAP_CERULEAN_CITY",
				"dest_warp_id": 0,
				"pair_id": 24
			},
			{
				"x": 3,
				"y": 1,
				"elevation": 3,
				"dest_map": "MAP_CERULEAN_CITY",
				"dest_warp_id": 8,
				"pair_id": 25
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_CERULEAN_CITY_HOUSE2",
		"alias": "CeruleanCity_House2",
		"key_items": (),
		"file_name": "CeruleanCity_House2",
		"warps": (
			{
				"x": 3,
				"y": 7,
				"elevation": 0,
				"dest_map": "MAP_CERULEAN_CITY",
				"dest_warp_id": 1,
				# "req_items": ("ssanne_ticket",),
				# "requires_all": True,
				"pair_id": 26
			},
			{
				"x": 4,
				"y": 1,
				"elevation": 0,
				"dest_map": "MAP_CERULEAN_CITY",
				"dest_warp_id": 9,
				"pair_id": 27
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_CERULEAN_CITY_HOUSE3",
		"alias": "CeruleanCity_House3",
		"key_items": (),
		"file_name": "CeruleanCity_House3",
		"warps": (
			{
				"x": 4,
				"y": 7,
				"elevation": 0,
				"dest_map": "MAP_CERULEAN_CITY",
				"dest_warp_id": 2,
				"pair_id": 31
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_CERULEAN_CITY_HOUSE4",
		"alias": "CeruleanCity_House4",
		"key_items": (),
		"file_name": "CeruleanCity_House4",
		"warps": (
			{
				"x": 4,
				"y": 7,
				"elevation": 3,
				"dest_map": "MAP_CERULEAN_CITY",
				"dest_warp_id": 12,
				"pair_id": 29
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_CERULEAN_CITY_HOUSE5",
		"alias": "CeruleanCity_House5",
		"key_items": (),
		"file_name": "CeruleanCity_House5",
		"warps": (
			{
				"x": 4,
				"y": 7,
				"elevation": 3,
				"dest_map": "MAP_CERULEAN_CITY",
				"dest_warp_id": 13,
				"pair_id": 30
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_CERULEAN_CITY_MART",
		"alias": "CeruleanCity_Mart",
		"key_items": (),
		"file_name": "CeruleanCity_Mart",
		"warps": (
			{
				"x": 4,
				"y": 7,
				"elevation": 3,
				"dest_map": "MAP_CERULEAN_CITY",
				"dest_warp_id": 6,
				"pair_id": 34
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_CERULEAN_CITY_POKEMON_CENTER_1F",
		"alias": "CeruleanCity_PokemonCenter_1F",
		"key_items": (),
		"file_name": "CeruleanCity_PokemonCenter_1F",
		"warps": (
			{
				"x": 7,
				"y": 8,
				"elevation": 0,
				"dest_map": "MAP_CERULEAN_CITY",
				"dest_warp_id": 3,
				"pair_id": 32
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_CINNABAR_ISLAND",
		"alias": "CinnabarIsland",
		"key_items": (),
		"file_name": "CinnabarIsland",
		"warps": (
			{
				"x": 8,
				"y": 3,
				"elevation": 0,
				"dest_map": "MAP_POKEMON_MANSION_1F",
				"dest_warp_id": 1,
				"pair_id": 35
			},
			# {
			# 	"x": 20,
			# 	"y": 4,
			# 	"elevation": 0,
			# 	"dest_map": "MAP_CINNABAR_ISLAND_GYM",
			# 	"dest_warp_id": 1,
			# 	"req_items": ("secret_key",),
			# 	"requires_all": True,
			# 	"pair_id": 36
			# },
			{
				"x": 8,
				"y": 9,
				"elevation": 0,
				"dest_map": "MAP_CINNABAR_ISLAND_POKEMON_LAB_ENTRANCE",
				"dest_warp_id": 1,
				"pair_id": 37
			},
			{
				"x": 14,
				"y": 11,
				"elevation": 0,
				"dest_map": "MAP_CINNABAR_ISLAND_POKEMON_CENTER_1F",
				"dest_warp_id": 0,
				"pair_id": 38
			},
			{
				"x": 19,
				"y": 11,
				"elevation": 0,
				"dest_map": "MAP_CINNABAR_ISLAND_MART",
				"dest_warp_id": 1,
				"pair_id": 39
			},
		),
		"connections": (
			("Route21_South", ("hm03_surf",)),
			("Route20_W", ("hm03_surf",)),
			("CinnabarIsland_Old_Fire_Guy", ("secret_key",)),
		),
	},
	{
		"id": "MAP_CINNABAR_ISLAND",
		"alias": "CinnabarIsland_Old_Fire_Guy",
		"key_items": (),
		"file_name": "CinnabarIsland",
		"warps": (
			{
				"x": 20,
				"y": 4,
				"elevation": 0,
				"dest_map": "MAP_CINNABAR_ISLAND_GYM",
				"dest_warp_id": 1,
				# "req_items": ("secret_key",),
				# "requires_all": True,
				"pair_id": 36
			},
		),
		"connections": (
			("CinnabarIsland", ("secret_key",)),
		),
	},
	{
		"id": "MAP_CINNABAR_ISLAND_GYM",
		"alias": "CinnabarIsland_Gym",
		"key_items": ("badge7",),
		"file_name": "CinnabarIsland_Gym",
		"warps": (
			{
				"x": 25,
				"y": 23,
				"elevation": 3,
				"dest_map": "MAP_CINNABAR_ISLAND",
				"dest_warp_id": 1,
				"pair_id": 36
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_CINNABAR_ISLAND_MART",
		"alias": "CinnabarIsland_Mart",
		"key_items": (),
		"file_name": "CinnabarIsland_Mart",
		"warps": (
			{
				"x": 4,
				"y": 7,
				"elevation": 3,
				"dest_map": "MAP_CINNABAR_ISLAND",
				"dest_warp_id": 4,
				"pair_id": 39
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_CINNABAR_ISLAND_POKEMON_CENTER_1F",
		"alias": "CinnabarIsland_PokemonCenter_1F",
		"key_items": (),
		"file_name": "CinnabarIsland_PokemonCenter_1F",
		"warps": (
			{
				"x": 7,
				"y": 8,
				"elevation": 0,
				"dest_map": "MAP_CINNABAR_ISLAND",
				"dest_warp_id": 3,
				"pair_id": 38
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_CINNABAR_ISLAND_POKEMON_LAB_ENTRANCE",
		"alias": "CinnabarIsland_PokemonLab_Entrance",
		"key_items": (),
		"file_name": "CinnabarIsland_PokemonLab_Entrance",
		"warps": (
			{
				"x": 4,
				"y": 9,
				"elevation": 3,
				"dest_map": "MAP_CINNABAR_ISLAND",
				"dest_warp_id": 2,
				"pair_id": 37
			},
			{
				"x": 13,
				"y": 5,
				"elevation": 0,
				"dest_map": "MAP_CINNABAR_ISLAND_POKEMON_LAB_LOUNGE",
				"dest_warp_id": 0,
				"pair_id": 40
			},
			{
				"x": 19,
				"y": 5,
				"elevation": 0,
				"dest_map": "MAP_CINNABAR_ISLAND_POKEMON_LAB_RESEARCH_ROOM",
				"dest_warp_id": 0,
				"pair_id": 41
			},
			{
				"x": 25,
				"y": 5,
				"elevation": 0,
				"dest_map": "MAP_CINNABAR_ISLAND_POKEMON_LAB_EXPERIMENT_ROOM",
				"dest_warp_id": 0,
				"pair_id": 42
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_CINNABAR_ISLAND_POKEMON_LAB_EXPERIMENT_ROOM",
		"alias": "CinnabarIsland_PokemonLab_ExperimentRoom",
		"key_items": (),
		"file_name": "CinnabarIsland_PokemonLab_ExperimentRoom",
		"warps": (
			{
				"x": 7,
				"y": 9,
				"elevation": 3,
				"dest_map": "MAP_CINNABAR_ISLAND_POKEMON_LAB_ENTRANCE",
				"dest_warp_id": 5,
				"pair_id": 42
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_CINNABAR_ISLAND_POKEMON_LAB_LOUNGE",
		"alias": "CinnabarIsland_PokemonLab_Lounge",
		"key_items": (),
		"file_name": "CinnabarIsland_PokemonLab_Lounge",
		"warps": (
			{
				"x": 7,
				"y": 9,
				"elevation": 3,
				"dest_map": "MAP_CINNABAR_ISLAND_POKEMON_LAB_ENTRANCE",
				"dest_warp_id": 3,
				"pair_id": 40
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_CINNABAR_ISLAND_POKEMON_LAB_RESEARCH_ROOM",
		"alias": "CinnabarIsland_PokemonLab_ResearchRoom",
		"key_items": (),
		"file_name": "CinnabarIsland_PokemonLab_ResearchRoom",
		"warps": (
			{
				"x": 7,
				"y": 9,
				"elevation": 3,
				"dest_map": "MAP_CINNABAR_ISLAND_POKEMON_LAB_ENTRANCE",
				"dest_warp_id": 4,
				"pair_id": 41
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_DIGLETTS_CAVE_B1F",
		"alias": "DiglettsCave_B1F",
		"key_items": (),
		"file_name": "DiglettsCave_B1F",
		"warps": (
			{
				"x": 3,
				"y": 3,
				"elevation": 3,
				"dest_map": "MAP_DIGLETTS_CAVE_NORTH_ENTRANCE",
				"dest_warp_id": 0,
				"pair_id": 43
			},
			{
				"x": 82,
				"y": 71,
				"elevation": 3,
				"dest_map": "MAP_DIGLETTS_CAVE_SOUTH_ENTRANCE",
				"dest_warp_id": 1,
				"pair_id": 44
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_DIGLETTS_CAVE_NORTH_ENTRANCE",
		"alias": "DiglettsCave_NorthEntrance",
		"key_items": (),
		"file_name": "DiglettsCave_NorthEntrance",
		"warps": (
			{
				"x": 6,
				"y": 4,
				"elevation": 3,
				"dest_map": "MAP_DIGLETTS_CAVE_B1F",
				"dest_warp_id": 0,
				"pair_id": 43
			},
			{
				"x": 4,
				"y": 6,
				"elevation": 3,
				"dest_map": "MAP_ROUTE2",
				"dest_warp_id": 3,
				"pair_id": 45
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_DIGLETTS_CAVE_SOUTH_ENTRANCE",
		"alias": "DiglettsCave_SouthEntrance",
		"key_items": (),
		"file_name": "DiglettsCave_SouthEntrance",
		"warps": (
			{
				"x": 4,
				"y": 6,
				"elevation": 3,
				"dest_map": "MAP_ROUTE11",
				"dest_warp_id": 0,
				"pair_id": 46
			},
			{
				"x": 6,
				"y": 4,
				"elevation": 3,
				"dest_map": "MAP_DIGLETTS_CAVE_B1F",
				"dest_warp_id": 1,
				"pair_id": 44
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_FUCHSIA_CITY",
		"alias": "FuchsiaCity",
		"key_items": (),
		"file_name": "FuchsiaCity",
		"warps": (
			{
				"x": 24,
				"y": 5,
				"elevation": 0,
				"dest_map": "MAP_FUCHSIA_CITY_SAFARI_ZONE_ENTRANCE",
				"dest_warp_id": 2,
				"pair_id": 47
			},
			{
				"x": 33,
				"y": 31,
				"elevation": 0,
				"dest_map": "MAP_FUCHSIA_CITY_WARDENS_HOUSE",
				"dest_warp_id": 1,
				"pair_id": 48
			},
			{
				"x": 11,
				"y": 15,
				"elevation": 0,
				"dest_map": "MAP_FUCHSIA_CITY_MART",
				"dest_warp_id": 1,
				"pair_id": 49
			},
			{
				"x": 28,
				"y": 16,
				"elevation": 0,
				"dest_map": "MAP_FUCHSIA_CITY_SAFARI_ZONE_OFFICE",
				"dest_warp_id": 1,
				"pair_id": 50
			},
			{
				"x": 9,
				"y": 32,
				"elevation": 0,
				"dest_map": "MAP_FUCHSIA_CITY_GYM",
				"dest_warp_id": 1,
				"pair_id": 51
			},
			{
				"x": 14,
				"y": 31,
				"elevation": 0,
				"dest_map": "MAP_FUCHSIA_CITY_HOUSE1",
				"dest_warp_id": 1,
				"pair_id": 52
			},
			{
				"x": 25,
				"y": 31,
				"elevation": 3,
				"dest_map": "MAP_FUCHSIA_CITY_POKEMON_CENTER_1F",
				"dest_warp_id": 1,
				"pair_id": 53
			},
			{
				"x": 38,
				"y": 31,
				"elevation": 0,
				"dest_map": "MAP_FUCHSIA_CITY_HOUSE2",
				"dest_warp_id": 1,
				"pair_id": 54
			},
			{
				"x": 19,
				"y": 31,
				"elevation": 0,
				"dest_map": "MAP_FUCHSIA_CITY_HOUSE3",
				"dest_warp_id": 0,
				"pair_id": 56
			},
		),
		"connections": (
			("Route19", ("hm03_surf",)),
			("Route18_E", None),
			("Route15_W", None),
		),
	},
	{
		"id": "MAP_FUCHSIA_CITY",
		"alias": "FuchsiaCity_Backroom",
		"key_items": (),
		"file_name": "FuchsiaCity",
		"warps": (
			{
				"x": 39,
				"y": 28,
				"elevation": 3,
				"dest_map": "MAP_FUCHSIA_CITY_HOUSE2",
				"dest_warp_id": 3,
				"pair_id": 55
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_FUCHSIA_CITY_GYM",
		"alias": "FuchsiaCity_Gym",
		"key_items": ("badge5",),
		"file_name": "FuchsiaCity_Gym",
		"warps": (
			{
				"x": 7,
				"y": 21,
				"elevation": 3,
				"dest_map": "MAP_FUCHSIA_CITY",
				"dest_warp_id": 4,
				"pair_id": 51
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_FUCHSIA_CITY_HOUSE1",
		"alias": "FuchsiaCity_House1",
		"key_items": (),
		"file_name": "FuchsiaCity_House1",
		"warps": (
			{
				"x": 4,
				"y": 7,
				"elevation": 3,
				"dest_map": "MAP_FUCHSIA_CITY",
				"dest_warp_id": 5,
				"pair_id": 52,
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_FUCHSIA_CITY_HOUSE2",
		"alias": "FuchsiaCity_House2",
		"key_items": (),
		"file_name": "FuchsiaCity_House2",
		"warps": (
			{
				"x": 3,
				"y": 8,
				"elevation": 3,
				"dest_map": "MAP_FUCHSIA_CITY",
				"dest_warp_id": 7,
				"pair_id": 54
			},
			{
				"x": 3,
				"y": 1,
				"elevation": 3,
				"dest_map": "MAP_FUCHSIA_CITY",
				"dest_warp_id": 8,
				"pair_id": 55
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_FUCHSIA_CITY_HOUSE3",
		"alias": "FuchsiaCity_House3",
		"key_items": (),
		"file_name": "FuchsiaCity_House3",
		"warps": (
			{
				"x": 4,
				"y": 7,
				"elevation": 3,
				"dest_map": "MAP_FUCHSIA_CITY",
				"dest_warp_id": 10,
				"pair_id": 56
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_FUCHSIA_CITY_MART",
		"alias": "FuchsiaCity_Mart",
		"key_items": (),
		"file_name": "FuchsiaCity_Mart",
		"warps": (
			{
				"x": 4,
				"y": 7,
				"elevation": 3,
				"dest_map": "MAP_FUCHSIA_CITY",
				"dest_warp_id": 2,
				"pair_id": 49
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_FUCHSIA_CITY_POKEMON_CENTER_1F",
		"alias": "FuchsiaCity_PokemonCenter_1F",
		"key_items": (),
		"file_name": "FuchsiaCity_PokemonCenter_1F",
		"warps": (
			{
				"x": 7,
				"y": 8,
				"elevation": 3,
				"dest_map": "MAP_FUCHSIA_CITY",
				"dest_warp_id": 6,
				"pair_id": 53
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_FUCHSIA_CITY_SAFARI_ZONE_ENTRANCE",
		"alias": "FuchsiaCity_SafariZone_Entrance",
		"key_items": ("hm03_surf", "gold_teeth",),
		"file_name": "FuchsiaCity_SafariZone_Entrance",
		"warps": (
			{
				"x": 4,
				"y": 1,
				"elevation": 3,
				"dest_map": "MAP_SAFARI_ZONE_CENTER",
				"dest_warp_id": 1
				# "exclude": True,
				# "pair_id": 305  # --------------------------------------------------------------
			},
			{
				"x": 4,
				"y": 7,
				"elevation": 3,
				"dest_map": "MAP_FUCHSIA_CITY",
				"dest_warp_id": 0,
				# "req_items": ("badge5",),
				# "requires_all": True,
				"pair_id": 47
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_FUCHSIA_CITY_SAFARI_ZONE_OFFICE",
		"alias": "FuchsiaCity_SafariZone_Office",
		"key_items": (),
		"file_name": "FuchsiaCity_SafariZone_Office",
		"warps": (
			{
				"x": 6,
				"y": 9,
				"elevation": 0,
				"dest_map": "MAP_FUCHSIA_CITY",
				"dest_warp_id": 3,
				"pair_id": 50
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_FUCHSIA_CITY_WARDENS_HOUSE",
		"alias": "FuchsiaCity_WardensHouse",
		"key_items": ("hm04_strength",),
		"file_name": "FuchsiaCity_WardensHouse",
		"warps": (
			{
				"x": 6,
				"y": 9,
				"elevation": 3,
				"dest_map": "MAP_FUCHSIA_CITY",
				"dest_warp_id": 1,
				# "req_items": ("gold_teeth", "badge4",),
				# "requires_all": True,
				"pair_id": 48
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_LAVENDER_TOWN",
		"alias": "LavenderTown",
		"key_items": (),
		"file_name": "LavenderTown",
		"warps": (
			{
				"x": 18,
				"y": 6,
				"elevation": 0,
				"dest_map": "MAP_POKEMON_TOWER_1F",
				"dest_warp_id": 1,
				"pair_id": 57
			},
			{
				"x": 6,
				"y": 5,
				"elevation": 0,
				"dest_map": "MAP_LAVENDER_TOWN_POKEMON_CENTER_1F",
				"dest_warp_id": 1,
				"pair_id": 58
			},
			{
				"x": 10,
				"y": 11,
				"elevation": 0,
				"dest_map": "MAP_LAVENDER_TOWN_VOLUNTEER_POKEMON_HOUSE",
				"dest_warp_id": 1,
				"pair_id": 59
			},
			{
				"x": 5,
				"y": 16,
				"elevation": 0,
				"dest_map": "MAP_LAVENDER_TOWN_HOUSE1",
				"dest_warp_id": 1,
				"pair_id": 60
			},
			{
				"x": 10,
				"y": 16,
				"elevation": 0,
				"dest_map": "MAP_LAVENDER_TOWN_HOUSE2",
				"dest_warp_id": 1,
				"pair_id": 61
			},
			{
				"x": 20,
				"y": 15,
				"elevation": 0,
				"dest_map": "MAP_LAVENDER_TOWN_MART",
				"dest_warp_id": 1,
				"pair_id": 62
			},
		),
		"connections": (
			("Route10_S", None),
			("Route12_N", None),
			("Route8", None),
		),
	},
	{
		"id": "MAP_LAVENDER_TOWN_HOUSE1",
		"alias": "LavenderTown_House1",
		"key_items": (),
		"file_name": "LavenderTown_House1",
		"warps": (
			{
				"x": 4,
				"y": 7,
				"elevation": 3,
				"dest_map": "MAP_LAVENDER_TOWN",
				"dest_warp_id": 3,
				"pair_id": 60
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_LAVENDER_TOWN_HOUSE2",
		"alias": "LavenderTown_House2",
		"key_items": (),
		"file_name": "LavenderTown_House2",
		"warps": (
			{
				"x": 4,
				"y": 7,
				"elevation": 3,
				"dest_map": "MAP_LAVENDER_TOWN",
				"dest_warp_id": 4,
				"pair_id": 61
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_LAVENDER_TOWN_MART",
		"alias": "LavenderTown_Mart",
		"key_items": (),
		"file_name": "LavenderTown_Mart",
		"warps": (
			{
				"x": 4,
				"y": 7,
				"elevation": 3,
				"dest_map": "MAP_LAVENDER_TOWN",
				"dest_warp_id": 5,
				"pair_id": 62
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_LAVENDER_TOWN_POKEMON_CENTER_1F",
		"alias": "LavenderTown_PokemonCenter_1F",
		"key_items": (),
		"file_name": "LavenderTown_PokemonCenter_1F",
		"warps": (
			{
				"x": 7,
				"y": 8,
				"elevation": 3,
				"dest_map": "MAP_LAVENDER_TOWN",
				"dest_warp_id": 1,
				"pair_id": 58
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_LAVENDER_TOWN_VOLUNTEER_POKEMON_HOUSE",
		"alias": "LavenderTown_VolunteerPokemonHouse",
		"key_items": (),
		"file_name": "LavenderTown_VolunteerPokemonHouse",
		"warps": (
			{
				"x": 4,
				"y": 7,
				"elevation": 3,
				"dest_map": "MAP_LAVENDER_TOWN",
				"dest_warp_id": 2,
				"pair_id": 59
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_MT_MOON_1F",
		"alias": "MtMoon_1F",
		"key_items": (),
		"file_name": "MtMoon_1F",
		"warps": (
			{
				"x": 5,
				"y": 6,
				"elevation": 3,
				"dest_map": "MAP_MT_MOON_B1F",
				"dest_warp_id": 0,
				"pair_id": 187  # --------------------------------------------------------------
			},
			{
				"x": 19,
				"y": 14,
				"elevation": 3,
				"dest_map": "MAP_MT_MOON_B1F",
				"dest_warp_id": 1,
				"pair_id": 188  # --------------------------------------------------------------
			},
			{
				"x": 31,
				"y": 16,
				"elevation": 3,
				"dest_map": "MAP_MT_MOON_B1F",
				"dest_warp_id": 2,
				"pair_id": 189  # --------------------------------------------------------------
			},
			{
				"x": 18,
				"y": 37,
				"elevation": 3,
				"dest_map": "MAP_ROUTE4",
				"dest_warp_id": 0,
				"pair_id": 63
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_MT_MOON_B1F",
		"alias": "MtMoon_B1F_S",
		"key_items": (),
		"file_name": "MtMoon_B1F",
		"warps": (
			{
				"x": 43,
				"y": 21,
				"elevation": 3,
				"dest_map": "MAP_MT_MOON_1F",
				"dest_warp_id": 2,
				"pair_id": 189  # --------------------------------------------------------------
			},
			{
				"x": 26,
				"y": 36,
				"elevation": 3,
				"dest_map": "MAP_MT_MOON_B2F",
				"dest_warp_id": 2,
				"pair_id": 192  # --------------------------------------------------------------
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_MT_MOON_B1F",
		"alias": "MtMoon_B1F_W",
		"key_items": (),
		"file_name": "MtMoon_B1F",
		"warps": (
			{
				"x": 3,
				"y": 3,
				"elevation": 3,
				"dest_map": "MAP_MT_MOON_1F",
				"dest_warp_id": 0,
				"pair_id": 187  # --------------------------------------------------------------
			},
			{
				"x": 22,
				"y": 18,
				"elevation": 3,
				"dest_map": "MAP_MT_MOON_B2F",
				"dest_warp_id": 0,
				"pair_id": 190  # --------------------------------------------------------------
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_MT_MOON_B1F",
		"alias": "MtMoon_B1F_N",
		"key_items": (),
		"file_name": "MtMoon_B1F",
		"warps": (
			{
				"x": 25,
				"y": 4,
				"elevation": 3,
				"dest_map": "MAP_MT_MOON_1F",
				"dest_warp_id": 1,
				"pair_id": 188  # --------------------------------------------------------------
			},
			{
				"x": 17,
				"y": 5,
				"elevation": 3,
				"dest_map": "MAP_MT_MOON_B2F",
				"dest_warp_id": 1,
				"pair_id": 191  # --------------------------------------------------------------
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_MT_MOON_B1F",
		"alias": "MtMoon_B1F_E",
		"key_items": (),
		"file_name": "MtMoon_B1F",
		"warps": (
			{
				"x": 39,
				"y": 4,
				"elevation": 3,
				"dest_map": "MAP_MT_MOON_B2F",
				"dest_warp_id": 3,
				"pair_id": 193  # --------------------------------------------------------------
			},
			{
				"x": 45,
				"y": 4,
				"elevation": 3,
				"dest_map": "MAP_ROUTE4",
				"dest_warp_id": 1,
				"pair_id": 118  # --------------------------------------------------------------
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_MT_MOON_B2F",
		"alias": "MtMoon_B2F_StarPiece",
		"key_items": (),
		"file_name": "MtMoon_B2F",
		"warps": (
			{
				"x": 17,
				"y": 31,
				"elevation": 3,
				"dest_map": "MAP_MT_MOON_B1F",
				"dest_warp_id": 5,
				"pair_id": 192  # --------------------------------------------------------------
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_MT_MOON_B2F",
		"alias": "MtMoon_B2F_Main",
		"key_items": (),
		"file_name": "MtMoon_B2F",
		"warps": (
			{
				"x": 25,
				"y": 21,
				"elevation": 3,
				"dest_map": "MAP_MT_MOON_B1F",
				"dest_warp_id": 3,
				"pair_id": 190  # --------------------------------------------------------------
			},
			{
				"x": 5,
				"y": 10,
				"elevation": 3,
				"dest_map": "MAP_MT_MOON_B1F",
				"dest_warp_id": 6,
				"pair_id": 193  # --------------------------------------------------------------
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_MT_MOON_B2F",
		"alias": "MtMoon_B2F_TM46",
		"key_items": (),
		"file_name": "MtMoon_B2F",
		"warps": (
			{
				"x": 31,
				"y": 11,
				"elevation": 3,
				"dest_map": "MAP_MT_MOON_B1F",
				"dest_warp_id": 4,
				"pair_id": 191  # --------------------------------------------------------------
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_PEWTER_CITY",
		"alias": "PewterCity",
		"key_items": (),
		"file_name": "PewterCity",
		"warps": (
			{
				"x": 17,
				"y": 6,
				"elevation": 0,
				"dest_map": "MAP_PEWTER_CITY_MUSEUM_1F",
				"dest_warp_id": 1,
				"pair_id": 64
			},
			# {
			# 	"x": 25,
			# 	"y": 4,
			# 	"elevation": 0,
			# 	"dest_map": "MAP_PEWTER_CITY_MUSEUM_1F",
			# 	"dest_warp_id": 3,
			# 	"req_items": ("hm01_cut",),
			# 	"requires_all": True,
			# 	"pair_id": 65
			# },
			{
				"x": 15,
				"y": 16,
				"elevation": 0,
				"dest_map": "MAP_PEWTER_CITY_GYM",
				"dest_warp_id": 1,
				"pair_id": 66
			},
			{
				"x": 28,
				"y": 18,
				"elevation": 0,
				"dest_map": "MAP_PEWTER_CITY_MART",
				"dest_warp_id": 1,
				"pair_id": 67
			},
			{
				"x": 33,
				"y": 11,
				"elevation": 0,
				"dest_map": "MAP_PEWTER_CITY_HOUSE1",
				"dest_warp_id": 1,
				"pair_id": 68
			},
			{
				"x": 17,
				"y": 25,
				"elevation": 0,
				"dest_map": "MAP_PEWTER_CITY_POKEMON_CENTER_1F",
				"dest_warp_id": 1,
				"pair_id": 69  # nice-----------------------------------------------------------
			},
			{
				"x": 9,
				"y": 30,
				"elevation": 0,
				"dest_map": "MAP_PEWTER_CITY_HOUSE2",
				"dest_warp_id": 1,
				"pair_id": 70
			},
		),
		"connections": (
			("Route2_NW", None),
			("Route3", None),
			("PewterCity_Fake_Fence", ("hm01_cut",)),
		),
	},
	{
		"id": "MAP_PEWTER_CITY",
		"alias": "PewterCity_Fake_Fence",
		"key_items": (),
		"file_name": "PewterCity",
		"warps": (
			{
				"x": 25,
				"y": 4,
				"elevation": 0,
				"dest_map": "MAP_PEWTER_CITY_MUSEUM_1F",
				"dest_warp_id": 3,
				# "req_items": ("hm01_cut",),
				# "requires_all": True,
				"pair_id": 65
			},
		),
		"connections": (
			("PewterCity", ("hm01_cut",)),
		),
	},
	{
		"id": "MAP_PEWTER_CITY_GYM",
		"alias": "PewterCity_Gym",
		"key_items": ("badge1",),
		"file_name": "PewterCity_Gym",
		"warps": (
			{
				"x": 6,
				"y": 14,
				"elevation": 3,
				"dest_map": "MAP_PEWTER_CITY",
				"dest_warp_id": 2,
				"pair_id": 66
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_PEWTER_CITY_HOUSE1",
		"alias": "PewterCity_House1",
		"key_items": (),
		"file_name": "PewterCity_House1",
		"warps": (
			{
				"x": 4,
				"y": 7,
				"elevation": 0,
				"dest_map": "MAP_PEWTER_CITY",
				"dest_warp_id": 4,
				"pair_id": 68
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_PEWTER_CITY_HOUSE2",
		"alias": "PewterCity_House2",
		"key_items": (),
		"file_name": "PewterCity_House2",
		"warps": (
			{
				"x": 4,
				"y": 7,
				"elevation": 0,
				"dest_map": "MAP_PEWTER_CITY",
				"dest_warp_id": 6,
				"pair_id": 70
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_PEWTER_CITY_MART",
		"alias": "PewterCity_Mart",
		"key_items": (),
		"file_name": "PewterCity_Mart",
		"warps": (
			{
				"x": 4,
				"y": 7,
				"elevation": 3,
				"dest_map": "MAP_PEWTER_CITY",
				"dest_warp_id": 3,
				"pair_id": 67
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_PEWTER_CITY_MUSEUM_1F",
		"alias": "PewterCity_Museum_W",
		"key_items": (),
		"file_name": "PewterCity_Museum_1F",
		"warps": (
			{
				"x": 14,
				"y": 9,
				"elevation": 3,
				"dest_map": "MAP_PEWTER_CITY",
				"dest_warp_id": 0,
				"pair_id": 64
			},
			{
				"x": 8,
				"y": 8,
				"elevation": 3,
				"dest_map": "MAP_PEWTER_CITY_MUSEUM_2F",
				"dest_warp_id": 0,
				"pair_id": 71
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_PEWTER_CITY_MUSEUM_1F",
		"alias": "PewterCity_Museum_1F_E",
		"key_items": (),
		"file_name": "PewterCity_Museum_1F",
		"warps": (
			{
				"x": 21,
				"y": 9,
				"elevation": 3,
				"dest_map": "MAP_PEWTER_CITY",
				"dest_warp_id": 1,
				"pair_id": 65
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_PEWTER_CITY_MUSEUM_2F",
		"alias": "PewterCity_Museum_2F",
		"key_items": (),
		"file_name": "PewterCity_Museum_2F",
		"warps": (
			{
				"x": 11,
				"y": 8,
				"elevation": 3,
				"dest_map": "MAP_PEWTER_CITY_MUSEUM_1F",
				"dest_warp_id": 5,
				"pair_id": 71
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_PEWTER_CITY_POKEMON_CENTER_1F",
		"alias": "PewterCity_PokemonCenter_1F",
		"key_items": (),
		"file_name": "PewterCity_PokemonCenter_1F",
		"warps": (
			{
				"x": 7,
				"y": 8,
				"elevation": 3,
				"dest_map": "MAP_PEWTER_CITY",
				"dest_warp_id": 5,
				"pair_id": 69  # nice-----------------------------------------------------------
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_POKEMON_MANSION_1F",
		"alias": "PokemonMansion_1F",
		"key_items": ("secret_key",),
		"file_name": "PokemonMansion_1F",
		"warps": (
			{
				"x": 8,
				"y": 33,
				"elevation": 3,
				"dest_map": "MAP_CINNABAR_ISLAND",
				"dest_warp_id": 0,
				"pair_id": 35
			},
			{
				"x": 34,
				"y": 33,
				"elevation": 3,
				"dest_map": "MAP_CINNABAR_ISLAND",
				"dest_warp_id": 0
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_POKEMON_TOWER_1F",
		"alias": "PokemonTower_1F",
		"key_items": (),
		"file_name": "PokemonTower_1F",
		"warps": (
			{
				"x": 11,
				"y": 18,
				"elevation": 3,
				"dest_map": "MAP_LAVENDER_TOWN",
				"dest_warp_id": 0,
				"pair_id": 57
			},
			{
				"x": 18,
				"y": 9,
				"elevation": 3,
				"dest_map": "MAP_POKEMON_TOWER_2F",
				"dest_warp_id": 1,
				"pair_id": 72
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_POKEMON_TOWER_2F",
		"alias": "PokemonTower_2F",
		"key_items": (),
		"file_name": "PokemonTower_2F",
		"warps": (
			{
				"x": 4,
				"y": 10,
				"elevation": 3,
				"dest_map": "MAP_POKEMON_TOWER_3F",
				"dest_warp_id": 0,
				"pair_id": 73
			},
			{
				"x": 18,
				"y": 10,
				"elevation": 3,
				"dest_map": "MAP_POKEMON_TOWER_1F",
				"dest_warp_id": 3,
				"pair_id": 72
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_POKEMON_TOWER_3F",
		"alias": "PokemonTower_3F",
		"key_items": (),
		"file_name": "PokemonTower_3F",
		"warps": (
			{
				"x": 4,
				"y": 10,
				"elevation": 3,
				"dest_map": "MAP_POKEMON_TOWER_2F",
				"dest_warp_id": 0,
				"pair_id": 73
			},
			{
				"x": 18,
				"y": 10,
				"elevation": 3,
				"dest_map": "MAP_POKEMON_TOWER_4F",
				"dest_warp_id": 1,
				"pair_id": 74
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_POKEMON_TOWER_4F",
		"alias": "PokemonTower_4F",
		"key_items": (),
		"file_name": "PokemonTower_4F",
		"warps": (
			{
				"x": 4,
				"y": 10,
				"elevation": 3,
				"dest_map": "MAP_POKEMON_TOWER_5F",
				"dest_warp_id": 0,
				"pair_id": 75
			},
			{
				"x": 18,
				"y": 10,
				"elevation": 3,
				"dest_map": "MAP_POKEMON_TOWER_3F",
				"dest_warp_id": 1,
				"pair_id": 74
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_POKEMON_TOWER_5F",
		"alias": "PokemonTower_5F",
		"key_items": (),
		"file_name": "PokemonTower_5F",
		"warps": (
			{
				"x": 4,
				"y": 10,
				"elevation": 3,
				"dest_map": "MAP_POKEMON_TOWER_4F",
				"dest_warp_id": 0,
				"pair_id": 75
			},
			{
				"x": 18,
				"y": 10,
				"elevation": 3,
				"dest_map": "MAP_POKEMON_TOWER_6F",
				"dest_warp_id": 1,
				"pair_id": 77
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_POKEMON_TOWER_6F",
		"alias": "PokemonTower_6F",
		"key_items": (),
		"file_name": "PokemonTower_6F",
		"warps": (
			# {
			# 	"x": 11,
			# 	"y": 16,
			# 	"elevation": 3,
			# 	"dest_map": "MAP_POKEMON_TOWER_7F",
			# 	"dest_warp_id": 0,
			# 	"req_item": ("silph_scope",),
			# 	"pair_id": 78
			# },
			{
				"x": 18,
				"y": 10,
				"elevation": 3,
				"dest_map": "MAP_POKEMON_TOWER_5F",
				"dest_warp_id": 1,
				"pair_id": 77
			},
		),
		"connections": (
			("PokemonTower_6F_Stairway_To_Heaven", ("silph_scope",)),
		),
	},
	{
		"id": "MAP_POKEMON_TOWER_6F",
		"alias": "PokemonTower_6F_Stairway_To_Heaven",
		"key_items": (),
		"file_name": "PokemonTower_6F",
		"warps": (
			{
				"x": 11,
				"y": 16,
				"elevation": 3,
				"dest_map": "MAP_POKEMON_TOWER_7F",
				"dest_warp_id": 0,
				"req_item": ("silph_scope",),
				"pair_id": 78
			},
			# {
			# 	"x": 18,
			# 	"y": 10,
			# 	"elevation": 3,
			# 	"dest_map": "MAP_POKEMON_TOWER_5F",
			# 	"dest_warp_id": 1,
			# 	"pair_id": 77
			# },
		),
		"connections": (
			("PokemonTower_6F", ("silph_scope",)),
		),
	},
	{
		"id": "MAP_POKEMON_TOWER_7F",
		"alias": "PokemonTower_7F",
		"key_items": ("poke_flute",),
		"file_name": "PokemonTower_7F",
		"warps": (
			{
				"x": 11,
				"y": 16,
				"elevation": 3,
				"dest_map": "MAP_POKEMON_TOWER_6F",
				"dest_warp_id": 0,
				"pair_id": 78
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_POWER_PLANT",
		"alias": "PowerPlant",
		"key_items": (),
		"file_name": "PowerPlant",
		"warps": (
			{
				"x": 5,
				"y": 38,
				"elevation": 3,
				"dest_map": "MAP_ROUTE10",
				"dest_warp_id": 2,
				"pair_id": 79
			},
			{
				"x": 1,
				"y": 11,
				"elevation": 3,
				"dest_map": "MAP_ROUTE10",
				"dest_warp_id": 4,
				"pair_id": 80
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_ROCKET_HIDEOUT_B1F",
		"alias": "RocketHideout_B1F_Top",
		"key_items": ("silph_scope",),
		"file_name": "RocketHideout_B1F",
		"warps": (
			{
				"x": 12,
				"y": 2,
				"elevation": 3,
				"dest_map": "MAP_CELADON_CITY_GAME_CORNER",
				"dest_warp_id": 3,
				"pair_id": 23
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_ROCKET_HIDEOUT_B1F",
		"alias": "RocketHideout_B1F_Bottom",
		"key_items": (),
		"file_name": "RocketHideout_B1F",
		"skip": True,
		"warps": (
			{
				"x": 17,
				"y": 2,
				"elevation": 3,
				"dest_map": "MAP_ROCKET_HIDEOUT_B2F",
				"dest_warp_id": 1,
				"pair_id": 81
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_ROCKET_HIDEOUT_B2F",
		"alias": "RocketHideout_B2F",
		"key_items": (),
		"file_name": "RocketHideout_B2F",
		"skip": True,
		"warps": (
			{
				"x": 21,
				"y": 2,
				"elevation": 3,
				"dest_map": "MAP_ROCKET_HIDEOUT_B3F",
				"dest_warp_id": 0,
				"pair_id": 83
			},
			{
				"x": 28,
				"y": 2,
				"elevation": 3,
				"dest_map": "MAP_ROCKET_HIDEOUT_B1F",
				"dest_warp_id": 1,
				"pair_id": 81
			},
			{
				"x": 23,
				"y": 12,
				"elevation": 3,
				"dest_map": "MAP_ROCKET_HIDEOUT_B1F",
				"dest_warp_id": 2,
				"pair_id": 82
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_ROCKET_HIDEOUT_B3F",
		"alias": "RocketHideout_B3F",
		"key_items": (),
		"file_name": "RocketHideout_B3F",
		"skip": True,
		"warps": (
			{
				"x": 18,
				"y": 2,
				"elevation": 3,
				"dest_map": "MAP_ROCKET_HIDEOUT_B2F",
				"dest_warp_id": 0,
				"pair_id": 83
			},
			{
				"x": 15,
				"y": 18,
				"elevation": 3,
				"dest_map": "MAP_ROCKET_HIDEOUT_B4F",
				"dest_warp_id": 0,
				"pair_id": 84
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_ROCKET_HIDEOUT_B4F",
		"alias": "RocketHideout_B4F_North",
		"key_items": ("silph_scope",),
		"file_name": "RocketHideout_B4F",
		"skip": True,
		"warps": (
			{
				"x": 11,
				"y": 15,
				"elevation": 3,
				"dest_map": "MAP_ROCKET_HIDEOUT_B3F",
				"dest_warp_id": 1,
				"pair_id": 84
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_ROCK_TUNNEL_1F",
		"alias": "RockTunnel_1F_W",
		"key_items": (),
		"file_name": "RockTunnel_1F",
		"warps": (
			{
				"x": 4,
				"y": 2,
				"elevation": 3,
				"dest_map": "MAP_ROCK_TUNNEL_B1F",
				"dest_warp_id": 1,
				"pair_id": 195  # --------------------------------------------------------------
			},
			{
				"x": 20,
				"y": 13,
				"elevation": 3,
				"dest_map": "MAP_ROCK_TUNNEL_B1F",
				"dest_warp_id": 2,
				"pair_id": 196  # --------------------------------------------------------------
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_ROCK_TUNNEL_1F",
		"alias": "RockTunnel_1F_E",
		"key_items": (),
		"file_name": "RockTunnel_1F",
		"warps": (
			{
				"x": 17,
				"y": 2,
				"elevation": 3,
				"dest_map": "MAP_ROUTE10",
				"dest_warp_id": 0,
				"pair_id": 85
			},
			{
				"x": 45,
				"y": 2,
				"elevation": 3,
				"dest_map": "MAP_ROCK_TUNNEL_B1F",
				"dest_warp_id": 0,
				"pair_id": 194  # --------------------------------------------------------------
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_ROCK_TUNNEL_1F",
		"alias": "RockTunnel_1F_S",
		"key_items": (),
		"file_name": "RockTunnel_1F",
		"warps": (
			{
				"x": 45,
				"y": 21,
				"elevation": 3,
				"dest_map": "MAP_ROCK_TUNNEL_B1F",
				"dest_warp_id": 3,
				"pair_id": 197  # --------------------------------------------------------------
			},
			{
				"x": 18,
				"y": 37,
				"elevation": 3,
				"dest_map": "MAP_ROUTE10",
				"dest_warp_id": 1,
				"pair_id": 86
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_ROCK_TUNNEL_B1F",
		"alias": "RockTunnel_B1F_W",
		"key_items": (),
		"file_name": "RockTunnel_B1F",
		"warps": (
			{
				"x": 27,
				"y": 12,
				"elevation": 3,
				"dest_map": "MAP_ROCK_TUNNEL_1F",
				"dest_warp_id": 3,
				"pair_id": 196  # --------------------------------------------------------------
			},
			{
				"x": 2,
				"y": 3,
				"elevation": 3,
				"dest_map": "MAP_ROCK_TUNNEL_1F",
				"dest_warp_id": 4,
				"pair_id": 197  # --------------------------------------------------------------
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_ROCK_TUNNEL_B1F",
		"alias": "RockTunnel_B1F_E",
		"key_items": (),
		"file_name": "RockTunnel_B1F",
		"warps": (
			{
				"x": 38,
				"y": 28,
				"elevation": 3,
				"dest_map": "MAP_ROCK_TUNNEL_1F",
				"dest_warp_id": 1,
				"pair_id": 194  # --------------------------------------------------------------
			},
			{
				"x": 33,
				"y": 3,
				"elevation": 3,
				"dest_map": "MAP_ROCK_TUNNEL_1F",
				"dest_warp_id": 2,
				"pair_id": 195  # --------------------------------------------------------------
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_ROUTE1",
		"alias": "Route1",
		"key_items": (),
		"file_name": "Route1",
		"warps": (
		),
		"connections": (
		),
	},
	{
		"id": "MAP_ROUTE10",
		"alias": "Route10_S",
		"key_items": (),
		"file_name": "Route10",
		"warps": (
			{
				"x": 8,
				"y": 57,
				"elevation": 3,
				"dest_map": "MAP_ROCK_TUNNEL_1F",
				"dest_warp_id": 5,
				"pair_id": 86
			},
		),
		"connections": (
			("LavenderTown", None),
		),
	},
	{
		"id": "MAP_ROUTE10",
		"alias": "Route10_Center",
		"key_items": (),
		"file_name": "Route10",
		"warps": (
			{
				"x": 7,
				"y": 40,
				"elevation": 3,
				"dest_map": "MAP_POWER_PLANT",
				"dest_warp_id": 1,
				# "req_items": ("hm03_surf",),
				# "requires_all": True,
				"pair_id": 79
			},
		),
		"connections": (
			("Route10_N", ("hm03_surf",)),
		),
	},
	{
		"id": "MAP_ROUTE10",
		"alias": "Route10_N",
		"key_items": (),
		"file_name": "Route10",
		"warps": (
			{
				"x": 8,
				"y": 19,
				"elevation": 3,
				"dest_map": "MAP_ROCK_TUNNEL_1F",
				"dest_warp_id": 0,
				"pair_id": 85
			},
			{
				"x": 13,
				"y": 20,
				"elevation": 0,
				"dest_map": "MAP_ROUTE10_POKEMON_CENTER_1F",
				"dest_warp_id": 1,
				"pair_id": 87
			},
		),
		"connections": (
			("Route9", None),
			("Route10_Center", ("hm03_surf",)),
		),
	},
	{
		"id": "MAP_ROUTE10_POKEMON_CENTER_1F",
		"alias": "Route10_PokemonCenter_1F",
		"key_items": (),
		"file_name": "Route10_PokemonCenter_1F",
		"warps": (
			{
				"x": 7,
				"y": 8,
				"elevation": 3,
				"dest_map": "MAP_ROUTE10",
				"dest_warp_id": 3,
				"pair_id": 87
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_ROUTE11",
		"alias": "Route11_W",
		"key_items": (),
		"file_name": "Route11",
		"warps": (
			{
				"x": 6,
				"y": 7,
				"elevation": 0,
				"dest_map": "MAP_DIGLETTS_CAVE_SOUTH_ENTRANCE",
				"dest_warp_id": 0,
				"pair_id": 46
			},
			{
				"x": 58,
				"y": 10,
				"elevation": 3,
				"dest_map": "MAP_ROUTE11_EAST_ENTRANCE_1F",
				"dest_warp_id": 0,
				"pair_id": 88
			},
		),
		"connections": (
			("VermilionCity", None),
		),
	},
	{
		"id": "MAP_ROUTE11",
		"alias": "Route11_E",
		"key_items": (),
		"file_name": "Route11",
		"warps": (
			{
				"x": 65,
				"y": 10,
				"elevation": 3,
				"dest_map": "MAP_ROUTE11_EAST_ENTRANCE_1F",
				"dest_warp_id": 2,
				# "req_items": ("poke_flute",),
				# "requires_all": True,
				"pair_id": 89
			},
		),
		"connections": (
			("Fucking_Fat_Man", ("poke_flute",)),
		),
	},
	{
		"id": "MAP_ROUTE11_EAST_ENTRANCE_1F",
		"alias": "Route11_EastEntrance_1F",
		"key_items": (),
		"file_name": "Route11_EastEntrance_1F",
		"warps": (
			{
				"x": 1,
				"y": 6,
				"elevation": 3,
				"dest_map": "MAP_ROUTE11",
				"dest_warp_id": 1,
				"pair_id": 88
			},
			{
				"x": 11,
				"y": 6,
				"elevation": 3,
				"dest_map": "MAP_ROUTE11",
				"dest_warp_id": 2,
				"pair_id": 89
			},
			{
				"x": 9,
				"y": 10,
				"elevation": 3,
				"dest_map": "MAP_ROUTE11_EAST_ENTRANCE_2F",
				"dest_warp_id": 0,
				"pair_id": 90
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_ROUTE11_EAST_ENTRANCE_2F",
		"alias": "Route11_EastEntrance_2F",
		"key_items": (),
		"file_name": "Route11_EastEntrance_2F",
		"warps": (
			{
				"x": 10,
				"y": 9,
				"elevation": 3,
				"dest_map": "MAP_ROUTE11_EAST_ENTRANCE_1F",
				"dest_warp_id": 4,
				"pair_id": 90
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_ROUTE12",
		"alias": "Fucking_Fat_Man",
		"key_items": (),
		"file_name": "Route12",
		"warps": (

		),
		"connections": (
			("Route12_Center", ("poke_flute",)),
			("Route12_S", ("poke_flute",)),
			("Route11_E", ("poke_flute",)),
		),
	},
	{
		"id": "MAP_ROUTE12",
		"alias": "Route12_S",
		"key_items": (),
		"file_name": "Route12",
		"warps": (
			{
				"x": 12,
				"y": 86,
				"elevation": 0,
				"dest_map": "MAP_ROUTE12_FISHING_HOUSE",
				"dest_warp_id": 1,
				"pair_id": 91
			},
		),
		"connections": (
			("Fucking_Fat_Man", ("poke_flute",)),
			("Route13", None),
		),
	},
	{
		"id": "MAP_ROUTE12",
		"alias": "Route12_Center",
		"key_items": (),
		"file_name": "Route12",
		"warps": (
			{
				"x": 14,
				"y": 21,
				"elevation": 3,
				"dest_map": "MAP_ROUTE12_NORTH_ENTRANCE_1F",
				"dest_warp_id": 2,
				"pair_id": 93
			},
		),
		"connections": (
			("Fucking_Fat_Man", ("poke_flute",)),
		),
	},
	{
		"id": "MAP_ROUTE12",
		"alias": "Route12_N",
		"key_items": (),
		"file_name": "Route12",
		"warps": (
			{
				"x": 14,
				"y": 15,
				"elevation": 3,
				"dest_map": "MAP_ROUTE12_NORTH_ENTRANCE_1F",
				"dest_warp_id": 0,
				"pair_id": 92
			},
		),
		"connections": (
			("LavenderTown", None),
		),
	},
	{
		"id": "MAP_ROUTE12_FISHING_HOUSE",
		"alias": "Route12_FishingHouse",
		"key_items": (),
		"file_name": "Route12_FishingHouse",
		"warps": (
			{
				"x": 3,
				"y": 7,
				"elevation": 3,
				"dest_map": "MAP_ROUTE12",
				"dest_warp_id": 0,
				"pair_id": 91
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_ROUTE12_NORTH_ENTRANCE_1F",
		"alias": "Route12_NorthEntrance_1F",
		"key_items": (),
		"file_name": "Route12_NorthEntrance_1F",
		"warps": (
			{
				"x": 5,
				"y": 1,
				"elevation": 3,
				"dest_map": "MAP_ROUTE12",
				"dest_warp_id": 1,
				"pair_id": 92
			},
			{
				"x": 5,
				"y": 11,
				"elevation": 3,
				"dest_map": "MAP_ROUTE12",
				"dest_warp_id": 3,
				"pair_id": 93
			},
			{
				"x": 8,
				"y": 10,
				"elevation": 3,
				"dest_map": "MAP_ROUTE12_NORTH_ENTRANCE_2F",
				"dest_warp_id": 0,
				"pair_id": 94
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_ROUTE12_NORTH_ENTRANCE_2F",
		"alias": "Route12_NorthEntrance_2F",
		"key_items": (),
		"file_name": "Route12_NorthEntrance_2F",
		"warps": (
			{
				"x": 10,
				"y": 9,
				"elevation": 3,
				"dest_map": "MAP_ROUTE12_NORTH_ENTRANCE_1F",
				"dest_warp_id": 4,
				"pair_id": 94
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_ROUTE13",
		"alias": "Route13",
		"key_items": (),
		"file_name": "Route13",
		"warps": (
		),
		"connections": (
			("Route12_S", None),
			("Route14", None),
		),
	},
	{
		"id": "MAP_ROUTE14",
		"alias": "Route14",
		"key_items": (),
		"file_name": "Route14",
		"warps": (
		),
		"connections": (
			("Route15_E", None),
			("Route13", None),
		),
	},
	{
		"id": "MAP_ROUTE15",
		"alias": "Route15_E",
		"key_items": (),
		"file_name": "Route15",
		"warps": (
			{
				"x": 16,
				"y": 11,
				"elevation": 3,
				"dest_map": "MAP_ROUTE15_WEST_ENTRANCE_1F",
				"dest_warp_id": 2,
				"pair_id": 96
			},
		),
		"connections": (
			("Route14", None),
		),
	},
	{
		"id": "MAP_ROUTE15",
		"alias": "Route15_W",
		"key_items": (),
		"file_name": "Route15",
		"warps": (
			{
				"x": 9,
				"y": 11,
				"elevation": 3,
				"dest_map": "MAP_ROUTE15_WEST_ENTRANCE_1F",
				"dest_warp_id": 0,
				"pair_id": 95
			},
		),
		"connections": (
			("FuchsiaCity", None),
		),
	},
	{
		"id": "MAP_ROUTE15_WEST_ENTRANCE_1F",
		"alias": "Route15_WestEntrance_1F",
		"key_items": (),
		"file_name": "Route15_WestEntrance_1F",
		"warps": (
			{
				"x": 1,
				"y": 6,
				"elevation": 3,
				"dest_map": "MAP_ROUTE15",
				"dest_warp_id": 0,
				"pair_id": 95
			},
			{
				"x": 11,
				"y": 6,
				"elevation": 3,
				"dest_map": "MAP_ROUTE15",
				"dest_warp_id": 1,
				"pair_id": 96
			},
			{
				"x": 9,
				"y": 10,
				"elevation": 3,
				"dest_map": "MAP_ROUTE15_WEST_ENTRANCE_2F",
				"dest_warp_id": 0,
				"pair_id": 97
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_ROUTE15_WEST_ENTRANCE_2F",
		"alias": "Route15_WestEntrance_2F",
		"key_items": (),
		"file_name": "Route15_WestEntrance_2F",
		"warps": (
			{
				"x": 10,
				"y": 9,
				"elevation": 3,
				"dest_map": "MAP_ROUTE15_WEST_ENTRANCE_1F",
				"dest_warp_id": 4,
				"pair_id": 97
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_ROUTE16",
		"alias": "Route16_SW",
		"key_items": (),
		"file_name": "Route16",
		"warps": (
			{
				"x": 20,
				"y": 13,
				"elevation": 3,
				"dest_map": "MAP_ROUTE16_NORTH_ENTRANCE_1F",
				"dest_warp_id": 2,
				"pair_id": 101  # --------------------------------------------------------------
			},
		),
		"connections": (
			("Route17", None),
		),
	},
	{
		"id": "MAP_ROUTE16",
		"alias": "Route16_NW",
		"key_items": (),
		"file_name": "Route16",
		"warps": (
			{
				"x": 10,
				"y": 5,
				"elevation": 0,
				"dest_map": "MAP_ROUTE16_HOUSE",
				"dest_warp_id": 1,
				"pair_id": 98
			},
			{
				"x": 20,
				"y": 6,
				"elevation": 3,
				"dest_map": "MAP_ROUTE16_NORTH_ENTRANCE_1F",
				"dest_warp_id": 0,
				"pair_id": 99
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_ROUTE16",
		"alias": "Behind_Fat_Bastard",
		"key_items": (),
		"file_name": "Route16",
		"warps": (
			{
				"x": 27,
				"y": 13,
				"elevation": 3,
				"dest_map": "MAP_ROUTE16_NORTH_ENTRANCE_1F",
				"dest_warp_id": 3,
				"pair_id": 102  # --------------------------------------------------------------
			},
		),
		"connections": (
			("Route16_SE", ("poke_flute",)),
		)
	},
	{
		"id": "MAP_ROUTE16",
		"alias": "Route16_SE",
		"key_items": (),
		"file_name": "Route16",
		"warps": (
			# {
			# 	"x": 27,
			# 	"y": 13,
			# 	"elevation": 3,
			# 	"dest_map": "MAP_ROUTE16_NORTH_ENTRANCE_1F",
			# 	"dest_warp_id": 3,
			# 	"req_items": ("poke_flute",),
			# 	"requires_all": True,
			# 	"pair_id": 102  # --------------------------------------------------------------
			# },
		),
		"connections": (
			("CeladonCity", None),
			("Route16_NE", ("hm01_cut",)),
			("Behind_Fat_Bastard", ("poke_flute",))
		),
	},
	{
		"id": "MAP_ROUTE16",
		"alias": "Route16_NE",
		"key_items": (),
		"file_name": "Route16",
		"warps": (
			{
				"x": 27,
				"y": 6,
				"elevation": 3,
				"dest_map": "MAP_ROUTE16_NORTH_ENTRANCE_1F",
				"dest_warp_id": 1,
				"pair_id": 100  # --------------------------------------------------------------
			},
		),
		"connections": (
			("Route16_SE", ("hm01_cut",)),
		)
	},
	{
		"id": "MAP_ROUTE16_HOUSE",
		"alias": "Route16_House",
		"key_items": ("hm02_fly",),
		"file_name": "Route16_House",
		"warps": (
			{
				"x": 4,
				"y": 7,
				"elevation": 3,
				"dest_map": "MAP_ROUTE16",
				"dest_warp_id": 0,
				# "req_items": ("badge3",),
				# "requires_all": True,
				"pair_id": 98
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_ROUTE16_NORTH_ENTRANCE_1F",
		"alias": "Route16_NorthEntrance_1F_Top",
		"key_items": (),
		"file_name": "Route16_NorthEntrance_1F",
		"warps": (
			{
				"x": 1,
				"y": 3,
				"elevation": 3,
				"dest_map": "MAP_ROUTE16",
				"dest_warp_id": 1,
				"pair_id": 99
			},
			{
				"x": 11,
				"y": 3,
				"elevation": 3,
				"dest_map": "MAP_ROUTE16",
				"dest_warp_id": 2,
				"pair_id": 100  # --------------------------------------------------------------
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_ROUTE16_NORTH_ENTRANCE_1F",
		"alias": "Route16_NorthEntrance_1F_Bot_Left",
		"key_items": (),
		"file_name": "Route16_NorthEntrance_1F",
		"warps": (
			{
				"x": 1,
				"y": 12,
				"elevation": 3,
				"dest_map": "MAP_ROUTE16",
				"dest_warp_id": 3,
				# "req_items": ("bike",),
				# "requires_all": True,
				"pair_id": 101  # --------------------------------------------------------------
			},
		),
		"connections": (
			("Route16_NorthEntrance_1F_Bot_Right", ("bike",)),
		),
	},
	{
		"id": "MAP_ROUTE16_NORTH_ENTRANCE_1F",
		"alias": "Route16_NorthEntrance_1F_Bot_Right",
		"key_items": (),
		"file_name": "Route16_NorthEntrance_1F",
		"warps": (
			{
				"x": 11,
				"y": 12,
				"elevation": 3,
				"dest_map": "MAP_ROUTE16",
				"dest_warp_id": 4,
				# "req_items": ("bike",),
				# "requires_all": True,
				"pair_id": 102  # --------------------------------------------------------------
			},
			{
				"x": 9,
				"y": 16,
				"elevation": 3,
				"dest_map": "MAP_ROUTE16_NORTH_ENTRANCE_2F",
				"dest_warp_id": 0,
				"pair_id": 103  # --------------------------------------------------------------
			},
		),
		"connections": (
			("Route16_NorthEntrance_1F_Bot_Left", ("bike",)),
		),
	},
	{
		"id": "MAP_ROUTE16_NORTH_ENTRANCE_2F",
		"alias": "Route16_NorthEntrance_2F",
		"key_items": (),
		"file_name": "Route16_NorthEntrance_2F",
		"warps": (
			{
				"x": 10,
				"y": 9,
				"elevation": 3,
				"dest_map": "MAP_ROUTE16_NORTH_ENTRANCE_1F",
				"dest_warp_id": 4,
				"pair_id": 103  # --------------------------------------------------------------
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_ROUTE17",
		"alias": "Route17",
		"key_items": (),
		"file_name": "Route17",
		"warps": (
		),
		"connections": (
			("Route16_SW", None),
			("Route18_W", None),
		),
	},
	{
		"id": "MAP_ROUTE18",
		"alias": "Route18_W",
		"key_items": (),
		"file_name": "Route18",
		"warps": (
			{
				"x": 41,
				"y": 9,
				"elevation": 3,
				"dest_map": "MAP_ROUTE18_EAST_ENTRANCE_1F",
				"dest_warp_id": 0,
				"pair_id": 104  # --------------------------------------------------------------
			},
		),
		"connections": (
			("Route17", None),
		),
	},
	{
		"id": "MAP_ROUTE18",
		"alias": "Route18_E",
		"key_items": (),
		"file_name": "Route18",
		"warps": (
			{
				"x": 48,
				"y": 9,
				"elevation": 3,
				"dest_map": "MAP_ROUTE18_EAST_ENTRANCE_1F",
				"dest_warp_id": 1,
				"pair_id": 105  # --------------------------------------------------------------
			},
		),
		"connections": (
			("FuchsiaCity", None),
		),
	},
	{
		"id": "MAP_ROUTE18_EAST_ENTRANCE_1F",
		"alias": "Route18_EastEntrance_1F_Left",
		"key_items": (),
		"file_name": "Route18_EastEntrance_1F",
		"warps": (
			{
				"x": 1,
				"y": 6,
				"elevation": 3,
				"dest_map": "MAP_ROUTE18",
				"dest_warp_id": 0,
				# "req_items": ("bike",),
				# "requires_all": True,
				"pair_id": 104  # --------------------------------------------------------------
			},
		),
		"connections": (
			("Route18_EastEntrance_1F_Right", ("bike",)),
		),
	},
	{
		"id": "MAP_ROUTE18_EAST_ENTRANCE_1F",
		"alias": "Route18_EastEntrance_1F_Right",
		"key_items": (),
		"file_name": "Route18_EastEntrance_1F",
		"warps": (
			{
				"x": 11,
				"y": 6,
				"elevation": 3,
				"dest_map": "MAP_ROUTE18",
				"dest_warp_id": 1,
				# "req_items": ("bike",),
				# "requires_all": True,
				"pair_id": 105  # --------------------------------------------------------------
			},
			{
				"x": 9,
				"y": 10,
				"elevation": 3,
				"dest_map": "MAP_ROUTE18_EAST_ENTRANCE_2F",
				"dest_warp_id": 0,
				"pair_id": 106  # --------------------------------------------------------------
			},
		),
		"connections": (
			("Route18_EastEntrance_1F_Left", ("bike",)),
		),
	},
	{
		"id": "MAP_ROUTE18_EAST_ENTRANCE_2F",
		"alias": "Route18_EastEntrance_2F",
		"key_items": (),
		"file_name": "Route18_EastEntrance_2F",
		"warps": (
			{
				"x": 10,
				"y": 9,
				"elevation": 3,
				"dest_map": "MAP_ROUTE18_EAST_ENTRANCE_1F",
				"dest_warp_id": 2,
				"pair_id": 106  # --------------------------------------------------------------
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_ROUTE19",
		"alias": "Route19",
		"key_items": (),
		"file_name": "Route19",
		"warps": (
		),
		"connections": (
			("FuchsiaCity", ("hm03_surf",)),
			("Route20_E", ("hm03_surf",),),
		),
	},
	{
		"id": "MAP_ROUTE2",
		"alias": "Route2_NW",
		"key_items": (),
		"file_name": "Route2",
		"warps": (
			{
				"x": 5,
				"y": 13,
				"elevation": 3,
				"dest_map": "MAP_ROUTE2_VIRIDIAN_FOREST_NORTH_ENTRANCE",
				"dest_warp_id": 3,
				"pair_id": 107  # --------------------------------------------------------------
			},
			{
				"x": 6,
				"y": 13,
				"elevation": 3,
				"dest_map": "MAP_ROUTE2_VIRIDIAN_FOREST_NORTH_ENTRANCE",
				"dest_warp_id": 3,
				"pair_id": 107  # --------------------------------------------------------------
			},
		),
		"connections": (
			("PewterCity", None),
			("Route2_NE", ("hm01_cut",)),
		),
	},
	{
		"id": "MAP_ROUTE2",
		"alias": "Route2_NE",
		"key_items": (),
		"file_name": "Route2",
		"warps": (
			{
				"x": 17,
				"y": 11,
				"elevation": 3,
				"dest_map": "MAP_DIGLETTS_CAVE_NORTH_ENTRANCE",
				"dest_warp_id": 1,
				"pair_id": 45
			},
			{
				"x": 17,
				"y": 22,
				"elevation": 0,
				"dest_map": "MAP_ROUTE2_HOUSE",
				"dest_warp_id": 1,
				"pair_id": 109  # --------------------------------------------------------------
			},
		),
		"connections": (
			("Route2_NW", ("hm01_cut",)),
			("Route2_Center", ("hm01_cut",)),
		)
	},
	{
		"id": "MAP_ROUTE2",
		"alias": "Route2_Center",
		"key_items": (),
		"file_name": "Route2",
		"warps": (
			{
				"x": 18,
				"y": 41,
				"elevation": 3,
				"dest_map": "MAP_ROUTE2_EAST_BUILDING",
				"dest_warp_id": 3,
				"pair_id": 111  # --------------------------------------------------------------
			},
			{
				"x": 19,
				"y": 41,
				"elevation": 3,
				"dest_map": "MAP_ROUTE2_EAST_BUILDING",
				"dest_warp_id": 3,
				"pair_id": 111  # --------------------------------------------------------------
			},
		),
		"connections": (
			("Route2_NE", ("hm01_cut",)),
		)
	},
	{
		"id": "MAP_ROUTE2",
		"alias": "Route2_SW",
		"key_items": (),
		"file_name": "Route2",
		"warps": (
			{
				"x": 5,
				"y": 51,
				"elevation": 3,
				"dest_map": "MAP_ROUTE2_VIRIDIAN_FOREST_SOUTH_ENTRANCE",
				"dest_warp_id": 1,
				"pair_id": 108  # --------------------------------------------------------------
			},
			{
				"x": 6,
				"y": 51,
				"elevation": 3,
				"dest_map": "MAP_ROUTE2_VIRIDIAN_FOREST_SOUTH_ENTRANCE",
				"dest_warp_id": 1,
				"pair_id": 108  # --------------------------------------------------------------
			},
		),
		"connections": (
			("ViridianCity_N", None),
			("Route2_SE", ("hm01_cut",)),
		),
	},
	{
		"id": "MAP_ROUTE2",
		"alias": "Route2_SE",
		"key_items": (),
		"file_name": "Route2",
		"warps": (
			{
				"x": 18,
				"y": 46,
				"elevation": 3,
				"dest_map": "MAP_ROUTE2_EAST_BUILDING",
				"dest_warp_id": 1,
				"pair_id": 110  # --------------------------------------------------------------
			},
			{
				"x": 19,
				"y": 46,
				"elevation": 3,
				"dest_map": "MAP_ROUTE2_EAST_BUILDING",
				"dest_warp_id": 1,
				"pair_id": 110  # --------------------------------------------------------------
			},
		),
		"connections": (
			("Route2_SW", ("hm01_cut",)),
		)
	},
	{
		"id": "MAP_ROUTE20",
		"alias": "Route20_E",
		"key_items": (),
		"file_name": "Route20",
		"warps": (
			{
				"x": 60,
				"y": 8,
				"elevation": 3,
				"dest_map": "MAP_SEAFOAM_ISLANDS_1F",
				"dest_warp_id": 3,
				"pair_id": 112  # --------------------------------------------------------------
			},
		),
		"connections": (
			("Route19", ("hm03_surf",)),
		),
	},
	{
		"id": "MAP_ROUTE20",
		"alias": "Route20_W",
		"key_items": (),
		"file_name": "Route20",
		"warps": (
			{
				"x": 72,
				"y": 14,
				"elevation": 3,
				"dest_map": "MAP_SEAFOAM_ISLANDS_1F",
				"dest_warp_id": 4,
				# "req_items": ("hm03_surf",),
				# "requires_all": True,
				"pair_id": 113  # --------------------------------------------------------------
			},
		),
		"connections": (
			("CinnabarIsland", ("hm03_surf",)),
		),
	},
	{
		"id": "MAP_ROUTE21_NORTH",
		"alias": "Route21_North",
		"key_items": (),
		"file_name": "Route21_North",
		"warps": (
		),
		"connections": (
			("Route21_South", ("hm03_surf",)),
		),
	},
	{
		"id": "MAP_ROUTE21_SOUTH",
		"alias": "Route21_South",
		"key_items": (),
		"file_name": "Route21_South",
		"warps": (
		),
		"connections": (
			("Route21_North", ("hm03_surf",)),
			("CinnabarIsland", ("hm03_surf",)),
		),
	},
	{
		"id": "MAP_ROUTE22",
		"alias": "Route22",
		"key_items": (),
		"file_name": "Route22",
		"warps": (
			{
				"x": 8,
				"y": 5,
				"elevation": 0,
				"dest_map": "MAP_ROUTE22_NORTH_ENTRANCE",
				"dest_warp_id": 2,
				"pair_id": 114  # --------------------------------------------------------------
			},
		),
		"connections": (
			("ViridianCity", None),
		),
	},
	{
		"id": "MAP_ROUTE22_NORTH_ENTRANCE",
		"alias": "Route22_NorthEntrance",
		"key_items": (),
		"file_name": "Route22_NorthEntrance",
		"warps": (
			{
				"x": 7,
				"y": 10,
				"elevation": 3,
				"dest_map": "MAP_ROUTE22",
				"dest_warp_id": 0,
				"pair_id": 114  # --------------------------------------------------------------
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_ROUTE23",
		"alias": "Route23",
		"key_items": (),
		"file_name": "Route23",
		"skip": True,
		"warps": (
			{
				"x": 5,
				"y": 28,
				"elevation": 3,
				"dest_map": "MAP_VICTORY_ROAD_1F",
				"dest_warp_id": 1,
				# "req_items": ("hm03_surf", "hm04_strength",),
				# "requires_all": True,
				"pair_id": 180  # --------------------------------------------------------------
			},
			{
				"x": 18,
				"y": 28,
				"elevation": 3,
				"dest_map": "MAP_VICTORY_ROAD_2F",
				"dest_warp_id": 6,
				# "req_items": ("hm03_surf", "hm04_strength",),
				# "requires_all": True,
				"pair_id": 181  # --------------------------------------------------------------
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_ROUTE24",
		"alias": "Route24",
		"key_items": (),
		"file_name": "Route24",
		"warps": (
		),
		"connections": (
			("CeruleanCity", None),
			("Route25", None),
			("CeruleanCity_Cave", ("hm03_surf",)),
		),
	},
	{
		"id": "MAP_ROUTE25",
		"alias": "Route25",
		"key_items": (),
		"file_name": "Route25",
		"warps": (
			{
				"x": 51,
				"y": 4,
				"elevation": 0,
				"dest_map": "MAP_ROUTE25_SEA_COTTAGE",
				"dest_warp_id": 1,
				"pair_id": 115  # --------------------------------------------------------------
			},
		),
		"connections": (
			("Route24", None),
		),
	},
	{
		"id": "MAP_ROUTE25_SEA_COTTAGE",
		"alias": "Route25_SeaCottage",
		"key_items": ("ssanne_ticket",),
		"file_name": "Route25_SeaCottage",
		"warps": (
			{
				"x": 7,
				"y": 9,
				"elevation": 3,
				"dest_map": "MAP_ROUTE25",
				"dest_warp_id": 0,
				"pair_id": 115  # --------------------------------------------------------------
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_ROUTE2_EAST_BUILDING",
		"alias": "Route2_EastBuilding",
		"key_items": ("hm05_flash",),
		"file_name": "Route2_EastBuilding",
		"warps": (
			{
				"x": 7,
				"y": 10,
				"elevation": 3,
				"dest_map": "MAP_ROUTE2",
				"dest_warp_id": 5,
				# "req_items": ("badge1",),
				# "requires_all": True,
				"pair_id": 110  # --------------------------------------------------------------
			},
			{
				"x": 7,
				"y": 1,
				"elevation": 3,
				"dest_map": "MAP_ROUTE2",
				"dest_warp_id": 6,
				"pair_id": 111  # --------------------------------------------------------------
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_ROUTE2_HOUSE",
		"alias": "Route2_House",
		"key_items": (),
		"file_name": "Route2_House",
		"warps": (
			{
				"x": 4,
				"y": 7,
				"elevation": 0,
				"dest_map": "MAP_ROUTE2",
				"dest_warp_id": 4,
				"pair_id": 109  # --------------------------------------------------------------
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_ROUTE2_VIRIDIAN_FOREST_NORTH_ENTRANCE",
		"alias": "Route2_ViridianForest_NorthEntrance",
		"key_items": (),
		"file_name": "Route2_ViridianForest_NorthEntrance",
		"warps": (
			{
				"x": 7,
				"y": 10,
				"elevation": 3,
				"dest_map": "MAP_VIRIDIAN_FOREST",
				"dest_warp_id": 2,
				"pair_id": 117  # --------------------------------------------------------------
			},
			{
				"x": 7,
				"y": 1,
				"elevation": 3,
				"dest_map": "MAP_ROUTE2",
				"dest_warp_id": 0,
				"pair_id": 107  # --------------------------------------------------------------
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_ROUTE2_VIRIDIAN_FOREST_SOUTH_ENTRANCE",
		"alias": "Route2_ViridianForest_SouthEntrance",
		"key_items": (),
		"file_name": "Route2_ViridianForest_SouthEntrance",
		"warps": (
			{
				"x": 7,
				"y": 10,
				"elevation": 3,
				"dest_map": "MAP_ROUTE2",
				"dest_warp_id": 2,
				"pair_id": 108  # --------------------------------------------------------------
			},
			{
				"x": 7,
				"y": 1,
				"elevation": 3,
				"dest_map": "MAP_VIRIDIAN_FOREST",
				"dest_warp_id": 0,
				"pair_id": 116  # --------------------------------------------------------------
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_ROUTE3",
		"alias": "Route3",
		"key_items": (),
		"file_name": "Route3",
		"warps": (
		),
		"connections": (
			("Route4_W", None),
			("PewterCity", None),
		),
	},
	{
		"id": "MAP_ROUTE4",
		"alias": "Route4_W",
		"key_items": (),
		"file_name": "Route4",
		"warps": (
			{
				"x": 19,
				"y": 5,
				"elevation": 3,
				"dest_map": "MAP_MT_MOON_1F",
				"dest_warp_id": 3,
				"pair_id": 63
			},
			{
				"x": 12,
				"y": 5,
				"elevation": 0,
				"dest_map": "MAP_ROUTE4_POKEMON_CENTER_1F",
				"dest_warp_id": 1,
				"pair_id": 119  # --------------------------------------------------------------
			},
		),
		"connections": (
			("Route3", None),
		),
	},
	{
		"id": "MAP_ROUTE4",
		"alias": "Route4_E",
		"key_items": (),
		"file_name": "Route4",
		"warps": (
			{
				"x": 32,
				"y": 5,
				"elevation": 0,
				"dest_map": "MAP_MT_MOON_B1F",
				"dest_warp_id": 7,
				# "req_items": ("hm03_surf",),
				# "requires_all": True,
				"pair_id": 118  # --------------------------------------------------------------
			},
		),
		"connections": (
			("CeruleanCity", None),
			# ("CeruleanCity_Cave", ("hm03_surf",)),
		),
	},
	{
		"id": "MAP_ROUTE4_POKEMON_CENTER_1F",
		"alias": "Route4_PokemonCenter_1F",
		"key_items": (),
		"file_name": "Route4_PokemonCenter_1F",
		"warps": (
			{
				"x": 7,
				"y": 8,
				"elevation": 3,
				"dest_map": "MAP_ROUTE4",
				"dest_warp_id": 2,
				"pair_id": 119  # --------------------------------------------------------------
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_ROUTE5",
		"alias": "Route5",
		"key_items": (),
		"file_name": "Route5",
		"warps": (
			{
				"x": 31,
				"y": 31,
				"elevation": 0,
				"dest_map": "MAP_UNDERGROUND_PATH_NORTH_ENTRANCE",
				"dest_warp_id": 1,
				"pair_id": 120  # --------------------------------------------------------------
			},
			{
				"x": 23,
				"y": 25,
				"elevation": 0,
				"dest_map": "MAP_ROUTE5_POKEMON_DAY_CARE",
				"dest_warp_id": 1,
				"pair_id": 121  # --------------------------------------------------------------
			},
			{
				"x": 24,
				"y": 32,
				"elevation": 3,
				"dest_map": "MAP_ROUTE5_SOUTH_ENTRANCE",
				"dest_warp_id": 1,
				"pair_id": 122  # --------------------------------------------------------------
			},
			{
				"x": 25,
				"y": 32,
				"elevation": 3,
				"dest_map": "MAP_ROUTE5_SOUTH_ENTRANCE",
				"dest_warp_id": 1,
				"pair_id": 122  # --------------------------------------------------------------
			},
		),
		"connections": (
			("CeruleanCity_Exterior", ("hm01_cut",),),
		),
	},
	{
		"id": "MAP_ROUTE5_POKEMON_DAY_CARE",
		"alias": "Route5_PokemonDayCare",
		"key_items": (),
		"file_name": "Route5_PokemonDayCare",
		"warps": (
			{
				"x": 4,
				"y": 7,
				"elevation": 0,
				"dest_map": "MAP_ROUTE5",
				"dest_warp_id": 1,
				"pair_id": 121  # --------------------------------------------------------------
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_ROUTE5_SOUTH_ENTRANCE",
		"alias": "Route5_SouthEntrance_Top",
		"key_items": (),
		"file_name": "Route5_SouthEntrance",
		"warps": (
			{
				"x": 4,
				"y": 1,
				"elevation": 3,
				"dest_map": "MAP_ROUTE5",
				"dest_warp_id": 2,
				# "req_items": ("tea",),
				# "requires_all": True,
				"pair_id": 122  # --------------------------------------------------------------
			},
		),
		"connections": (
			("Route5_SouthEntrance_Bot", ("tea",)),
		),
	},
	{
		"id": "MAP_ROUTE5_SOUTH_ENTRANCE",
		"alias": "Route5_SouthEntrance_Bot",
		"key_items": (),
		"file_name": "Route5_SouthEntrance",
		"warps": (
			{
				"x": 4,
				"y": 9,
				"elevation": 3,
				"dest_map": "MAP_SAFFRON_CITY",
				"dest_warp_id": 9,
				# "req_items": ("tea",),
				# "requires_all": True,
				"pair_id": 123  # --------------------------------------------------------------
			},
		),
		"connections": (
			("Route5_SouthEntrance_Top", ("tea",)),
		),
	},
	{
		"id": "MAP_ROUTE6",
		"alias": "Route6",
		"key_items": (),
		"file_name": "Route6",
		"warps": (
			{
				"x": 19,
				"y": 13,
				"elevation": 0,
				"dest_map": "MAP_UNDERGROUND_PATH_SOUTH_ENTRANCE",
				"dest_warp_id": 1,
				"pair_id": 124  # --------------------------------------------------------------
			},
			{
				"x": 12,
				"y": 5,
				"elevation": 3,
				"dest_map": "MAP_ROUTE6_NORTH_ENTRANCE",
				"dest_warp_id": 2,
				"pair_id": 125  # --------------------------------------------------------------
			},
			{
				"x": 13,
				"y": 5,
				"elevation": 3,
				"dest_map": "MAP_ROUTE6_NORTH_ENTRANCE",
				"dest_warp_id": 2,
				"pair_id": 125  # --------------------------------------------------------------
			},
		),
		"connections": (
			("VermilionCity", None),
		),
	},
	{
		"id": "MAP_ROUTE6_NORTH_ENTRANCE",
		"alias": "Route6_NorthEntrance_Top",
		"key_items": (),
		"file_name": "Route6_NorthEntrance",
		"warps": (
			{
				"x": 4,
				"y": 1,
				"elevation": 0,
				"dest_map": "MAP_SAFFRON_CITY",
				"dest_warp_id": 11,
				# "req_items": ("tea",),
				# "requires_all": True,
				"pair_id": 126  # --------------------------------------------------------------
			},
		),
		"connections": (
			("Route6_NorthEntrance_Bot", ("tea",)),
		),
	},
	{
		"id": "MAP_ROUTE6_NORTH_ENTRANCE",
		"alias": "Route6_NorthEntrance_Bot",
		"key_items": (),
		"file_name": "Route6_NorthEntrance",
		"warps": (
			{
				"x": 4,
				"y": 9,
				"elevation": 3,
				"dest_map": "MAP_ROUTE6",
				"dest_warp_id": 1,
				# "req_items": ("tea",),
				# "requires_all": True,
				"pair_id": 125  # --------------------------------------------------------------
			},
		),
		"connections": (
			("Route6_NorthEntrance_Top", ("tea",)),
		),
	},
	{
		"id": "MAP_ROUTE7",
		"alias": "Route7",
		"key_items": (),
		"file_name": "Route7",
		"warps": (
			{
				"x": 7,
				"y": 14,
				"elevation": 0,
				"dest_map": "MAP_UNDERGROUND_PATH_WEST_ENTRANCE",
				"dest_warp_id": 1,
				"pair_id": 127  # --------------------------------------------------------------
			},
			{
				"x": 15,
				"y": 10,
				"elevation": 3,
				"dest_map": "MAP_ROUTE7_EAST_ENTRANCE",
				"dest_warp_id": 0,
				"pair_id": 128  # --------------------------------------------------------------
			},
		),
		"connections": (
			("CeladonCity", None),
		),
	},
	{
		"id": "MAP_ROUTE7_EAST_ENTRANCE",
		"alias": "Route7_EastEntrance_Left",
		"key_items": (),
		"file_name": "Route7_EastEntrance",
		"warps": (
			{
				"x": 1,
				"y": 5,
				"elevation": 3,
				"dest_map": "MAP_ROUTE7",
				"dest_warp_id": 1,
				# "req_items": ("tea",),
				# "requires_all": True,
				"pair_id": 128  # --------------------------------------------------------------
			},
		),
		"connections": (
			("Route7_EastEntrance_Right", ("tea",)),
		),
	},
	{
		"id": "MAP_ROUTE7_EAST_ENTRANCE",
		"alias": "Route7_EastEntrance_Right",
		"key_items": (),
		"file_name": "Route7_EastEntrance",
		"warps": (
			{
				"x": 11,
				"y": 5,
				"elevation": 3,
				"dest_map": "MAP_SAFFRON_CITY",
				"dest_warp_id": 8,
				# "req_items": ("tea",),
				# "requires_all": True,
				"pair_id": 129  # --------------------------------------------------------------
			},
		),
		"connections": (
			("Route7_EastEntrance_Left", ("tea",)),
		),
	},
	{
		"id": "MAP_ROUTE8",
		"alias": "Route8",
		"key_items": (),
		"file_name": "Route8",
		"warps": (
			{
				"x": 13,
				"y": 4,
				"elevation": 0,
				"dest_map": "MAP_UNDERGROUND_PATH_EAST_ENTRANCE",
				"dest_warp_id": 1,
				"pair_id": 130  # --------------------------------------------------------------
			},
			{
				"x": 7,
				"y": 10,
				"elevation": 3,
				"dest_map": "MAP_ROUTE8_WEST_ENTRANCE",
				"dest_warp_id": 2,
				"pair_id": 131  # --------------------------------------------------------------
			},
		),
		"connections": (
			("LavenderTown", None),
		),
	},
	{
		"id": "MAP_ROUTE8_WEST_ENTRANCE",
		"alias": "Route8_WestEntrance_Left",
		"key_items": (),
		"file_name": "Route8_WestEntrance",
		"warps": (
			{
				"x": 1,
				"y": 5,
				"elevation": 3,
				"dest_map": "MAP_SAFFRON_CITY",
				"dest_warp_id": 10,
				# "req_items": ("tea",),
				# "requires_all": True,
				"pair_id": 132  # --------------------------------------------------------------
			},
		),
		"connections": (
			("Route8_WestEntrance_Right", ("tea",)),
		),
	},
	{
		"id": "MAP_ROUTE8_WEST_ENTRANCE",
		"alias": "Route8_WestEntrance_Right",
		"key_items": (),
		"file_name": "Route8_WestEntrance",
		"warps": (
			{
				"x": 11,
				"y": 5,
				"elevation": 3,
				"dest_map": "MAP_ROUTE8",
				"dest_warp_id": 1,
				# "req_items": ("tea",),
				# "requires_all": True,
				"pair_id": 131  # --------------------------------------------------------------
			},
		),
		"connections": (
			("Route8_WestEntrance_Left", ("tea",)),
		),
	},
	{
		"id": "MAP_ROUTE9",
		"alias": "Route9",
		"key_items": (),
		"file_name": "Route9",
		"warps": (
		),
		"connections": (
			("CeruleanCity_Exterior", ("hm01_cut",)),
			("Route10_N", None),
		),
	},
	{
		"id": "MAP_SAFARI_ZONE_CENTER",
		"alias": "SafariZone_Center",
		"key_items": ("gold_teeth",),
		"file_name": "SafariZone_Center",
		"warps": (
			{
				"x": 25,
				"y": 30,
				"elevation": 3,
				"dest_map": "MAP_FUCHSIA_CITY_SAFARI_ZONE_ENTRANCE",
				"dest_warp_id": 0
				# "pair_id": 305  # --------------------------------------------------------------
			},
			{
				"x": 26,
				"y": 30,
				"elevation": 3,
				"dest_map": "MAP_FUCHSIA_CITY_SAFARI_ZONE_ENTRANCE",
				"dest_warp_id": 0
				# "pair_id": 305  # --------------------------------------------------------------
			},
			{
				"x": 27,
				"y": 30,
				"elevation": 3,
				"dest_map": "MAP_FUCHSIA_CITY_SAFARI_ZONE_ENTRANCE",
				"dest_warp_id": 0
			},
			{
				"x": 25,
				"y": 5,
				"elevation": 3,
				"dest_map": "MAP_SAFARI_ZONE_NORTH",
				"dest_warp_id": 9
			},
			{
				"x": 26,
				"y": 5,
				"elevation": 3,
				"dest_map": "MAP_SAFARI_ZONE_NORTH",
				"dest_warp_id": 10
			},
			{
				"x": 27,
				"y": 5,
				"elevation": 0,
				"dest_map": "MAP_SAFARI_ZONE_NORTH",
				"dest_warp_id": 11
			},
			{
				"x": 8,
				"y": 17,
				"elevation": 3,
				"dest_map": "MAP_SAFARI_ZONE_WEST",
				"dest_warp_id": 6
			},
			{
				"x": 8,
				"y": 18,
				"elevation": 3,
				"dest_map": "MAP_SAFARI_ZONE_WEST",
				"dest_warp_id": 7
			},
			{
				"x": 8,
				"y": 19,
				"elevation": 0,
				"dest_map": "MAP_SAFARI_ZONE_WEST",
				"dest_warp_id": 8
			},
			{
				"x": 43,
				"y": 15,
				"elevation": 3,
				"dest_map": "MAP_SAFARI_ZONE_EAST",
				"dest_warp_id": 3
			},
			{
				"x": 43,
				"y": 16,
				"elevation": 3,
				"dest_map": "MAP_SAFARI_ZONE_EAST",
				"dest_warp_id": 4
			},
			{
				"x": 43,
				"y": 17,
				"elevation": 0,
				"dest_map": "MAP_SAFARI_ZONE_EAST",
				"dest_warp_id": 5
			},
			{
				"x": 29,
				"y": 25,
				"elevation": 0,
				"dest_map": "MAP_SAFARI_ZONE_CENTER_REST_HOUSE",
				"dest_warp_id": 1
				# "entrance_only": True,
				# "exclude": True,
				# "pair_id": 300  # --------------------------------------------------------------
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_SAFARI_ZONE_CENTER_REST_HOUSE",
		"alias": "SafariZone_Center_RestHouse",
		"key_items": (),
		"file_name": "SafariZone_Center_RestHouse",
		"warps": (
			{
				"x": 3,
				"y": 9,
				"elevation": 3,
				"dest_map": "MAP_SAFARI_ZONE_CENTER",
				"dest_warp_id": 12
			},
			{
				"x": 4,
				"y": 9,
				"elevation": 3,
				"dest_map": "MAP_SAFARI_ZONE_CENTER",
				"dest_warp_id": 12,

			},
			{
				"x": 5,
				"y": 9,
				"elevation": 3,
				"dest_map": "MAP_SAFARI_ZONE_CENTER",
				"dest_warp_id": 12
				# "pair_id": 300  # --------------------------------------------------------------
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_SAFARI_ZONE_EAST",
		"alias": "SafariZone_East",
		"key_items": (),
		"file_name": "SafariZone_East",
		"warps": (
			{
				"x": 8,
				"y": 9,
				"elevation": 3,
				"dest_map": "MAP_SAFARI_ZONE_NORTH",
				"dest_warp_id": 6
			},
			{
				"x": 8,
				"y": 10,
				"elevation": 3,
				"dest_map": "MAP_SAFARI_ZONE_NORTH",
				"dest_warp_id": 7
			},
			{
				"x": 8,
				"y": 11,
				"elevation": 0,
				"dest_map": "MAP_SAFARI_ZONE_NORTH",
				"dest_warp_id": 8
			},
			{
				"x": 8,
				"y": 26,
				"elevation": 3,
				"dest_map": "MAP_SAFARI_ZONE_CENTER",
				"dest_warp_id": 9
			},
			{
				"x": 8,
				"y": 27,
				"elevation": 3,
				"dest_map": "MAP_SAFARI_ZONE_CENTER",
				"dest_warp_id": 10
			},
			{
				"x": 8,
				"y": 28,
				"elevation": 0,
				"dest_map": "MAP_SAFARI_ZONE_CENTER",
				"dest_warp_id": 11
			},
			{
				"x": 40,
				"y": 14,
				"elevation": 0,
				"dest_map": "MAP_SAFARI_ZONE_EAST_REST_HOUSE",
				"dest_warp_id": 1
				# "entrance_only": True,
				# "exclude": True,
				# "pair_id": 301  # --------------------------------------------------------------
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_SAFARI_ZONE_EAST_REST_HOUSE",
		"alias": "SafariZone_East_RestHouse",
		"key_items": (),
		"file_name": "SafariZone_East_RestHouse",
		"warps": (
			{
				"x": 3,
				"y": 9,
				"elevation": 3,
				"dest_map": "MAP_SAFARI_ZONE_EAST",
				"dest_warp_id": 6
			},
			{
				"x": 4,
				"y": 9,
				"elevation": 3,
				"dest_map": "MAP_SAFARI_ZONE_EAST",
				"dest_warp_id": 6
				# "pair_id": 301  # --------------------------------------------------------------
			},
			{
				"x": 5,
				"y": 9,
				"elevation": 3,
				"dest_map": "MAP_SAFARI_ZONE_EAST",
				"dest_warp_id": 6
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_SAFARI_ZONE_NORTH",
		"alias": "SafariZone_North",
		"key_items": (),
		"file_name": "SafariZone_North",
		"warps": (
			{
				"x": 10,
				"y": 34,
				"elevation": 3,
				"dest_map": "MAP_SAFARI_ZONE_WEST",
				"dest_warp_id": 0
			},
			{
				"x": 11,
				"y": 34,
				"elevation": 3,
				"dest_map": "MAP_SAFARI_ZONE_WEST",
				"dest_warp_id": 1
			},
			{
				"x": 12,
				"y": 34,
				"elevation": 0,
				"dest_map": "MAP_SAFARI_ZONE_WEST",
				"dest_warp_id": 2
			},
			{
				"x": 20,
				"y": 34,
				"elevation": 3,
				"dest_map": "MAP_SAFARI_ZONE_WEST",
				"dest_warp_id": 3
			},
			{
				"x": 21,
				"y": 34,
				"elevation": 3,
				"dest_map": "MAP_SAFARI_ZONE_WEST",
				"dest_warp_id": 4
			},
			{
				"x": 22,
				"y": 34,
				"elevation": 0,
				"dest_map": "MAP_SAFARI_ZONE_WEST",
				"dest_warp_id": 5
			},
			{
				"x": 48,
				"y": 31,
				"elevation": 3,
				"dest_map": "MAP_SAFARI_ZONE_EAST",
				"dest_warp_id": 0
			},
			{
				"x": 48,
				"y": 32,
				"elevation": 3,
				"dest_map": "MAP_SAFARI_ZONE_EAST",
				"dest_warp_id": 1
			},
			{
				"x": 48,
				"y": 33,
				"elevation": 0,
				"dest_map": "MAP_SAFARI_ZONE_EAST",
				"dest_warp_id": 2
			},
			{
				"x": 30,
				"y": 34,
				"elevation": 3,
				"dest_map": "MAP_SAFARI_ZONE_CENTER",
				"dest_warp_id": 3
			},
			{
				"x": 31,
				"y": 34,
				"elevation": 3,
				"dest_map": "MAP_SAFARI_ZONE_CENTER",
				"dest_warp_id": 4
			},
			{
				"x": 32,
				"y": 34,
				"elevation": 0,
				"dest_map": "MAP_SAFARI_ZONE_CENTER",
				"dest_warp_id": 5
			},
			{
				"x": 43,
				"y": 8,
				"elevation": 0,
				"dest_map": "MAP_SAFARI_ZONE_NORTH_REST_HOUSE",
				"dest_warp_id": 1
				# "entrance_only": True,
				# "exclude": True,
				# "pair_id": 302  # --------------------------------------------------------------
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_SAFARI_ZONE_NORTH_REST_HOUSE",
		"alias": "SafariZone_North_RestHouse",
		"key_items": (),
		"file_name": "SafariZone_North_RestHouse",
		"warps": (
			{
				"x": 3,
				"y": 9,
				"elevation": 3,
				"dest_map": "MAP_SAFARI_ZONE_NORTH",
				"dest_warp_id": 12
			},
			{
				"x": 4,
				"y": 9,
				"elevation": 3,
				"dest_map": "MAP_SAFARI_ZONE_NORTH",
				"dest_warp_id": 12
				# "pair_id": 302  # --------------------------------------------------------------
			},
			{
				"x": 5,
				"y": 9,
				"elevation": 3,
				"dest_map": "MAP_SAFARI_ZONE_NORTH",
				"dest_warp_id": 12
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_SAFARI_ZONE_SECRET_HOUSE",
		"alias": "SafariZone_SecretHouse",
		"key_items": ("hm03_surf",),
		"file_name": "SafariZone_SecretHouse",
		"warps": (
			{
				"x": 3,
				"y": 9,
				"elevation": 3,
				"dest_map": "MAP_SAFARI_ZONE_WEST",
				"dest_warp_id": 9
			},
			{
				"x": 4,
				"y": 9,
				"elevation": 3,
				"dest_map": "MAP_SAFARI_ZONE_WEST",
				"dest_warp_id": 9
				# "req_items": ("badge5",),
				# "pair_id": 303  # --------------------------------------------------------------
			},
			{
				"x": 5,
				"y": 9,
				"elevation": 3,
				"dest_map": "MAP_SAFARI_ZONE_WEST",
				"dest_warp_id": 9
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_SAFARI_ZONE_WEST",
		"alias": "SafariZone_West",
		"key_items": ("gold_teeth",),
		"file_name": "SafariZone_West",
		"warps": (
			{
				"x": 30,
				"y": 5,
				"elevation": 3,
				"dest_map": "MAP_SAFARI_ZONE_NORTH",
				"dest_warp_id": 0
			},
			{
				"x": 31,
				"y": 5,
				"elevation": 3,
				"dest_map": "MAP_SAFARI_ZONE_NORTH",
				"dest_warp_id": 1
			},
			{
				"x": 32,
				"y": 5,
				"elevation": 0,
				"dest_map": "MAP_SAFARI_ZONE_NORTH",
				"dest_warp_id": 2
			},
			{
				"x": 37,
				"y": 5,
				"elevation": 3,
				"dest_map": "MAP_SAFARI_ZONE_NORTH",
				"dest_warp_id": 3
			},
			{
				"x": 38,
				"y": 5,
				"elevation": 3,
				"dest_map": "MAP_SAFARI_ZONE_NORTH",
				"dest_warp_id": 4
			},
			{
				"x": 39,
				"y": 5,
				"elevation": 0,
				"dest_map": "MAP_SAFARI_ZONE_NORTH",
				"dest_warp_id": 5
			},
			{
				"x": 40,
				"y": 26,
				"elevation": 3,
				"dest_map": "MAP_SAFARI_ZONE_CENTER",
				"dest_warp_id": 6
			},
			{
				"x": 40,
				"y": 27,
				"elevation": 3,
				"dest_map": "MAP_SAFARI_ZONE_CENTER",
				"dest_warp_id": 7
			},
			{
				"x": 40,
				"y": 28,
				"elevation": 0,
				"dest_map": "MAP_SAFARI_ZONE_CENTER",
				"dest_warp_id": 8
			},
			{
				"x": 12,
				"y": 7,
				"elevation": 0,
				"dest_map": "MAP_SAFARI_ZONE_SECRET_HOUSE",
				"dest_warp_id": 1
				# "entrance_only": True,
				# "exclude": True,
				# "pair_id": 303  # --------------------------------------------------------------
			},
			{
				"x": 19,
				"y": 18,
				"elevation": 0,
				"dest_map": "MAP_SAFARI_ZONE_WEST_REST_HOUSE",
				"dest_warp_id": 1
				# "entrance_only": True,
				# "exclude": True,
				# "pair_id": 304  # --------------------------------------------------------------
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_SAFARI_ZONE_WEST_REST_HOUSE",
		"alias": "SafariZone_West_RestHouse",
		"key_items": (),
		"file_name": "SafariZone_West_RestHouse",
		"warps": (
			{
				"x": 3,
				"y": 9,
				"elevation": 3,
				"dest_map": "MAP_SAFARI_ZONE_WEST",
				"dest_warp_id": 10
			},
			{
				"x": 4,
				"y": 9,
				"elevation": 3,
				"dest_map": "MAP_SAFARI_ZONE_WEST",
				"dest_warp_id": 10
				# "pair_id": 304  # --------------------------------------------------------------
			},
			{
				"x": 5,
				"y": 9,
				"elevation": 3,
				"dest_map": "MAP_SAFARI_ZONE_WEST",
				"dest_warp_id": 10
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_SAFFRON_CITY",
		"alias": "SaffronCity",
		"key_items": (),
		"file_name": "SaffronCity",
		"warps": (
			# {
			# 	"x": 33,
			# 	"y": 30,
			# 	"elevation": 0,
			# 	"dest_map": "MAP_SILPH_CO_1F",
			# 	"dest_warp_id": 1,
			# 	"req_items": ("poke_flute",),
			# 	"requires_all": True,
			# 	"pair_id": 133  # --------------------------------------------------------------
			# },
			# {
			# 	"x": 22,
			# 	"y": 14,
			# 	"elevation": 0,
			# 	"dest_map": "MAP_SAFFRON_CITY_COPYCATS_HOUSE_1F",
			# 	"dest_warp_id": 1,
			# 	"req_items": ("master_ball",),
			# 	"requires_all": True,
			# 	"pair_id": 134  # --------------------------------------------------------------
			# },
			{
				"x": 40,
				"y": 12,
				"elevation": 0,
				"dest_map": "MAP_SAFFRON_CITY_DOJO",
				"dest_warp_id": 1,
				"pair_id": 135  # --------------------------------------------------------------
			},
			# {
			# 	"x": 46,
			# 	"y": 12,
			# 	"elevation": 0,
			# 	"dest_map": "MAP_SAFFRON_CITY_GYM",
			# 	"dest_warp_id": 1,
			# 	"req_items": ("master_ball",),
			# 	"requires_all": True,
			# 	"pair_id": 136  # --------------------------------------------------------------
			# },
			# {
			# 	"x": 27,
			# 	"y": 21,
			# 	"elevation": 0,
			# 	"dest_map": "MAP_SAFFRON_CITY_HOUSE",
			# 	"dest_warp_id": 1,
			# 	"req_items": ("master_ball",),
			# 	"requires_all": True,
			# 	"pair_id": 137  # --------------------------------------------------------------
			# },
			{
				"x": 40,
				"y": 21,
				"elevation": 0,
				"dest_map": "MAP_SAFFRON_CITY_MART",
				"dest_warp_id": 1,
				"pair_id": 138  # --------------------------------------------------------------
			},
			{
				"x": 24,
				"y": 38,
				"elevation": 0,
				"dest_map": "MAP_SAFFRON_CITY_POKEMON_CENTER_1F",
				"dest_warp_id": 1,
				"pair_id": 139  # --------------------------------------------------------------
			},
			{
				"x": 43,
				"y": 38,
				"elevation": 0,
				"dest_map": "MAP_SAFFRON_CITY_MR_PSYCHICS_HOUSE",
				"dest_warp_id": 1,
				"pair_id": 140  # --------------------------------------------------------------
			},
			{
				"x": 8,
				"y": 27,
				"elevation": 3,
				"dest_map": "MAP_ROUTE7_EAST_ENTRANCE",
				"dest_warp_id": 2,
				"pair_id": 129  # --------------------------------------------------------------
			},
			{
				"x": 34,
				"y": 5,
				"elevation": 3,
				"dest_map": "MAP_ROUTE5_SOUTH_ENTRANCE",
				"dest_warp_id": 2,
				"pair_id": 123  # --------------------------------------------------------------
			},
			{
				"x": 58,
				"y": 27,
				"elevation": 3,
				"dest_map": "MAP_ROUTE8_WEST_ENTRANCE",
				"dest_warp_id": 1,
				"pair_id": 132  # --------------------------------------------------------------
			},
			{
				"x": 34,
				"y": 46,
				"elevation": 3,
				"dest_map": "MAP_ROUTE6_NORTH_ENTRANCE",
				"dest_warp_id": 0,
				"pair_id": 126  # --------------------------------------------------------------
			},
			{
				"x": 35,
				"y": 46,
				"elevation": 3,
				"dest_map": "MAP_ROUTE6_NORTH_ENTRANCE",
				"dest_warp_id": 0,
				"pair_id": 126  # --------------------------------------------------------------
			},
			{
				"x": 35,
				"y": 5,
				"elevation": 3,
				"dest_map": "MAP_ROUTE5_SOUTH_ENTRANCE",
				"dest_warp_id": 2,
				"pair_id": 123  # --------------------------------------------------------------
			},
			{
				"x": 47,
				"y": 21,
				"elevation": 0,
				"dest_map": "MAP_SAFFRON_CITY_POKEMON_TRAINER_FAN_CLUB",
				"dest_warp_id": 0,
				"pair_id": 141  # --------------------------------------------------------------
			},
		),
		"connections": (
			("SaffronCity_Tower", ("poke_flute",)),
			("SaffronCity_Crime", ("master_ball",)),
		),
	},
	{
		"id": "MAP_SAFFRON_CITY",
		"alias": "SaffronCity_Tower",
		"key_items": (),
		"file_name": "SaffronCity",
		"warps": (
			{
				"x": 33,
				"y": 30,
				"elevation": 0,
				"dest_map": "MAP_SILPH_CO_1F",
				"dest_warp_id": 1,
				# "req_items": ("poke_flute",),
				# "requires_all": True,
				"pair_id": 133  # --------------------------------------------------------------
			},
		),
		"connections": (
			("SaffronCity", ("poke_flute",)),
		),
	},
	{
		"id": "MAP_SAFFRON_CITY",
		"alias": "SaffronCity_Crime",
		"key_items": (),
		"file_name": "SaffronCity",
		"warps": (
			{
				"x": 22,
				"y": 14,
				"elevation": 0,
				"dest_map": "MAP_SAFFRON_CITY_COPYCATS_HOUSE_1F",
				"dest_warp_id": 1,
				# "req_items": ("master_ball",),
				# "requires_all": True,
				"pair_id": 134  # --------------------------------------------------------------
			},
			{
				"x": 46,
				"y": 12,
				"elevation": 0,
				"dest_map": "MAP_SAFFRON_CITY_GYM",
				"dest_warp_id": 1,
				# "req_items": ("master_ball",),
				# "requires_all": True,
				"pair_id": 136  # --------------------------------------------------------------
			},
			{
				"x": 27,
				"y": 21,
				"elevation": 0,
				"dest_map": "MAP_SAFFRON_CITY_HOUSE",
				"dest_warp_id": 1,
				# "req_items": ("master_ball",),
				# "requires_all": True,
				"pair_id": 137  # --------------------------------------------------------------
			},
		),
		"connections": (
			("SaffronCity", ("master_ball",)),
		),
	},
	{
		"id": "MAP_SAFFRON_CITY_COPYCATS_HOUSE_1F",
		"alias": "SaffronCity_CopycatsHouse_1F",
		"key_items": (),
		"file_name": "SaffronCity_CopycatsHouse_1F",
		"warps": (
			{
				"x": 4,
				"y": 8,
				"elevation": 3,
				"dest_map": "MAP_SAFFRON_CITY",
				"dest_warp_id": 1,
				"pair_id": 134  # --------------------------------------------------------------
			},
			{
				"x": 10,
				"y": 2,
				"elevation": 3,
				"dest_map": "MAP_SAFFRON_CITY_COPYCATS_HOUSE_2F",
				"dest_warp_id": 0,
				"pair_id": 142  # --------------------------------------------------------------
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_SAFFRON_CITY_COPYCATS_HOUSE_2F",
		"alias": "SaffronCity_CopycatsHouse_2F",
		"key_items": (),
		"file_name": "SaffronCity_CopycatsHouse_2F",
		"warps": (
			{
				"x": 10,
				"y": 2,
				"elevation": 3,
				"dest_map": "MAP_SAFFRON_CITY_COPYCATS_HOUSE_1F",
				"dest_warp_id": 3,
				"pair_id": 142  # --------------------------------------------------------------
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_SAFFRON_CITY_DOJO",
		"alias": "SaffronCity_Dojo",
		"key_items": (),
		"file_name": "SaffronCity_Dojo",
		"warps": (
			{
				"x": 6,
				"y": 14,
				"elevation": 3,
				"dest_map": "MAP_SAFFRON_CITY",
				"dest_warp_id": 2,
				"pair_id": 135  # --------------------------------------------------------------
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_SAFFRON_CITY_GYM",
		"alias": "SaffronCity_Gym",
		"key_items": ("badge6",),
		"file_name": "SaffronCity_Gym",
		"warps": (
			{
				"x": 13,
				"y": 23,
				"elevation": 3,
				"dest_map": "MAP_SAFFRON_CITY",
				"dest_warp_id": 3
			},
			{
				"x": 14,
				"y": 23,
				"elevation": 3,
				"dest_map": "MAP_SAFFRON_CITY",
				"dest_warp_id": 3,
				"pair_id": 136  # --------------------------------------------------------------
			},
			{
				"x": 15,
				"y": 23,
				"elevation": 3,
				"dest_map": "MAP_SAFFRON_CITY",
				"dest_warp_id": 3
			},
			{
				"x": 18,
				"y": 20,
				"elevation": 3,
				"dest_map": "MAP_SAFFRON_CITY_GYM",
				"dest_warp_id": 32
			},
			{
				"x": 0,
				"y": 4,
				"elevation": 3,
				"dest_map": "MAP_SAFFRON_CITY_GYM",
				"dest_warp_id": 22
			},
			{
				"x": 0,
				"y": 7,
				"elevation": 3,
				"dest_map": "MAP_SAFFRON_CITY_GYM",
				"dest_warp_id": 20
			},
			{
				"x": 0,
				"y": 12,
				"elevation": 3,
				"dest_map": "MAP_SAFFRON_CITY_GYM",
				"dest_warp_id": 30
			},
			{
				"x": 0,
				"y": 15,
				"elevation": 3,
				"dest_map": "MAP_SAFFRON_CITY_GYM",
				"dest_warp_id": 11
			},
			{
				"x": 0,
				"y": 20,
				"elevation": 3,
				"dest_map": "MAP_SAFFRON_CITY_GYM",
				"dest_warp_id": 28
			},
			{
				"x": 0,
				"y": 23,
				"elevation": 3,
				"dest_map": "MAP_SAFFRON_CITY_GYM",
				"dest_warp_id": 19
			},
			{
				"x": 8,
				"y": 4,
				"elevation": 3,
				"dest_map": "MAP_SAFFRON_CITY_GYM",
				"dest_warp_id": 18
			},
			{
				"x": 8,
				"y": 7,
				"elevation": 3,
				"dest_map": "MAP_SAFFRON_CITY_GYM",
				"dest_warp_id": 7
			},
			{
				"x": 8,
				"y": 12,
				"elevation": 3,
				"dest_map": "MAP_SAFFRON_CITY_GYM",
				"dest_warp_id": 17
			},
			{
				"x": 8,
				"y": 15,
				"elevation": 3,
				"dest_map": "MAP_SAFFRON_CITY_GYM",
				"dest_warp_id": 15
			},
			{
				"x": 8,
				"y": 20,
				"elevation": 3,
				"dest_map": "MAP_SAFFRON_CITY_GYM",
				"dest_warp_id": 26
			},
			{
				"x": 8,
				"y": 23,
				"elevation": 3,
				"dest_map": "MAP_SAFFRON_CITY_GYM",
				"dest_warp_id": 13
			},
			{
				"x": 12,
				"y": 4,
				"elevation": 3,
				"dest_map": "MAP_SAFFRON_CITY_GYM",
				"dest_warp_id": 24
			},
			{
				"x": 12,
				"y": 7,
				"elevation": 3,
				"dest_map": "MAP_SAFFRON_CITY_GYM",
				"dest_warp_id": 12
			},
			{
				"x": 16,
				"y": 4,
				"elevation": 3,
				"dest_map": "MAP_SAFFRON_CITY_GYM",
				"dest_warp_id": 10
			},
			{
				"x": 16,
				"y": 7,
				"elevation": 3,
				"dest_map": "MAP_SAFFRON_CITY_GYM",
				"dest_warp_id": 9
			},
			{
				"x": 18,
				"y": 15,
				"elevation": 3,
				"dest_map": "MAP_SAFFRON_CITY_GYM",
				"dest_warp_id": 5
			},
			{
				"x": 20,
				"y": 4,
				"elevation": 3,
				"dest_map": "MAP_SAFFRON_CITY_GYM",
				"dest_warp_id": 23
			},
			{
				"x": 20,
				"y": 7,
				"elevation": 3,
				"dest_map": "MAP_SAFFRON_CITY_GYM",
				"dest_warp_id": 4
			},
			{
				"x": 20,
				"y": 12,
				"elevation": 3,
				"dest_map": "MAP_SAFFRON_CITY_GYM",
				"dest_warp_id": 21
			},
			{
				"x": 20,
				"y": 15,
				"elevation": 3,
				"dest_map": "MAP_SAFFRON_CITY_GYM",
				"dest_warp_id": 16
			},
			{
				"x": 20,
				"y": 20,
				"elevation": 3,
				"dest_map": "MAP_SAFFRON_CITY_GYM",
				"dest_warp_id": 27
			},
			{
				"x": 20,
				"y": 23,
				"elevation": 3,
				"dest_map": "MAP_SAFFRON_CITY_GYM",
				"dest_warp_id": 14
			},
			{
				"x": 28,
				"y": 4,
				"elevation": 3,
				"dest_map": "MAP_SAFFRON_CITY_GYM",
				"dest_warp_id": 25
			},
			{
				"x": 28,
				"y": 7,
				"elevation": 3,
				"dest_map": "MAP_SAFFRON_CITY_GYM",
				"dest_warp_id": 8
			},
			{
				"x": 28,
				"y": 12,
				"elevation": 3,
				"dest_map": "MAP_SAFFRON_CITY_GYM",
				"dest_warp_id": 31
			},
			{
				"x": 28,
				"y": 15,
				"elevation": 3,
				"dest_map": "MAP_SAFFRON_CITY_GYM",
				"dest_warp_id": 6
			},
			{
				"x": 28,
				"y": 20,
				"elevation": 3,
				"dest_map": "MAP_SAFFRON_CITY_GYM",
				"dest_warp_id": 29
			},
			{
				"x": 28,
				"y": 23,
				"elevation": 3,
				"dest_map": "MAP_SAFFRON_CITY_GYM",
				"dest_warp_id": 3
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_SAFFRON_CITY_HOUSE",
		"alias": "SaffronCity_House",
		"key_items": (),
		"file_name": "SaffronCity_House",
		"warps": (
			{
				"x": 4,
				"y": 7,
				"elevation": 3,
				"dest_map": "MAP_SAFFRON_CITY",
				"dest_warp_id": 4,
				"pair_id": 137  # --------------------------------------------------------------
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_SAFFRON_CITY_MART",
		"alias": "SaffronCity_Mart",
		"key_items": (),
		"file_name": "SaffronCity_Mart",
		"warps": (
			{
				"x": 4,
				"y": 7,
				"elevation": 3,
				"dest_map": "MAP_SAFFRON_CITY",
				"dest_warp_id": 5,
				"pair_id": 138  # --------------------------------------------------------------
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_SAFFRON_CITY_MR_PSYCHICS_HOUSE",
		"alias": "SaffronCity_MrPsychicsHouse",
		"key_items": (),
		"file_name": "SaffronCity_MrPsychicsHouse",
		"warps": (
			{
				"x": 4,
				"y": 7,
				"elevation": 3,
				"dest_map": "MAP_SAFFRON_CITY",
				"dest_warp_id": 7,
				"pair_id": 140  # --------------------------------------------------------------
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_SAFFRON_CITY_POKEMON_CENTER_1F",
		"alias": "SaffronCity_PokemonCenter_1F",
		"key_items": (),
		"file_name": "SaffronCity_PokemonCenter_1F",
		"warps": (
			{
				"x": 7,
				"y": 8,
				"elevation": 3,
				"dest_map": "MAP_SAFFRON_CITY",
				"dest_warp_id": 6,
				"pair_id": 139  # --------------------------------------------------------------
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_SAFFRON_CITY_POKEMON_TRAINER_FAN_CLUB",
		"alias": "SaffronCity_PokemonTrainerFanClub",
		"key_items": (),
		"file_name": "SaffronCity_PokemonTrainerFanClub",
		"warps": (
			{
				"x": 5,
				"y": 15,
				"elevation": 3,
				"dest_map": "MAP_SAFFRON_CITY",
				"dest_warp_id": 14,
				"pair_id": 141  # --------------------------------------------------------------
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_SEAFOAM_ISLANDS_1F",
		"alias": "SeafoamIslands_1F",
		"key_items": (),
		"file_name": "SeafoamIslands_1F",
		"warps": (
			{
				"x": 10,
				"y": 6,
				"elevation": 3,
				"dest_map": "MAP_SEAFOAM_ISLANDS_B1F",
				"dest_warp_id": 0
			},
			{
				"x": 31,
				"y": 4,
				"elevation": 3,
				"dest_map": "MAP_SEAFOAM_ISLANDS_B1F",
				"dest_warp_id": 1
			},
			{
				"x": 28,
				"y": 19,
				"elevation": 3,
				"dest_map": "MAP_SEAFOAM_ISLANDS_B1F",
				"dest_warp_id": 2
			},
			{
				"x": 6,
				"y": 21,
				"elevation": 3,
				"dest_map": "MAP_ROUTE20",
				"dest_warp_id": 0,
				"pair_id": 112  # --------------------------------------------------------------
			},
			{
				"x": 32,
				"y": 21,
				"elevation": 3,
				"dest_map": "MAP_ROUTE20",
				"dest_warp_id": 1,
				"pair_id": 113  # --------------------------------------------------------------
			},
			{
				"x": 21,
				"y": 8,
				"elevation": 3,
				"dest_map": "MAP_SEAFOAM_ISLANDS_B1F",
				"dest_warp_id": 9
			},
			{
				"x": 30,
				"y": 8,
				"elevation": 3,
				"dest_map": "MAP_SEAFOAM_ISLANDS_B1F",
				"dest_warp_id": 10
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_SEAFOAM_ISLANDS_B1F",
		"alias": "SeafoamIslands_B1F",
		"key_items": (),
		"file_name": "SeafoamIslands_B1F",
		"warps": (
			{
				"x": 10,
				"y": 6,
				"elevation": 4,
				"dest_map": "MAP_SEAFOAM_ISLANDS_1F",
				"dest_warp_id": 0
			},
			{
				"x": 31,
				"y": 4,
				"elevation": 3,
				"dest_map": "MAP_SEAFOAM_ISLANDS_1F",
				"dest_warp_id": 1
			},
			{
				"x": 28,
				"y": 19,
				"elevation": 3,
				"dest_map": "MAP_SEAFOAM_ISLANDS_1F",
				"dest_warp_id": 2
			},
			{
				"x": 7,
				"y": 3,
				"elevation": 3,
				"dest_map": "MAP_SEAFOAM_ISLANDS_B2F",
				"dest_warp_id": 3
			},
			{
				"x": 17,
				"y": 9,
				"elevation": 4,
				"dest_map": "MAP_SEAFOAM_ISLANDS_B2F",
				"dest_warp_id": 4
			},
			{
				"x": 25,
				"y": 19,
				"elevation": 3,
				"dest_map": "MAP_SEAFOAM_ISLANDS_B2F",
				"dest_warp_id": 5
			},
			{
				"x": 32,
				"y": 14,
				"elevation": 3,
				"dest_map": "MAP_SEAFOAM_ISLANDS_B2F",
				"dest_warp_id": 6
			},
			{
				"x": 23,
				"y": 8,
				"elevation": 3,
				"dest_map": "MAP_SEAFOAM_ISLANDS_B2F",
				"dest_warp_id": 7
			},
			{
				"x": 28,
				"y": 8,
				"elevation": 3,
				"dest_map": "MAP_SEAFOAM_ISLANDS_B2F",
				"dest_warp_id": 8
			},
			{
				"x": 21,
				"y": 8,
				"elevation": 3,
				"dest_map": "MAP_SEAFOAM_ISLANDS_1F",
				"dest_warp_id": 5
			},
			{
				"x": 29,
				"y": 8,
				"elevation": 3,
				"dest_map": "MAP_SEAFOAM_ISLANDS_1F",
				"dest_warp_id": 6
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_SEAFOAM_ISLANDS_B2F",
		"alias": "SeafoamIslands_B2F",
		"key_items": (),
		"file_name": "SeafoamIslands_B2F",
		"warps": (
			{
				"x": 7,
				"y": 17,
				"elevation": 3,
				"dest_map": "MAP_SEAFOAM_ISLANDS_B3F",
				"dest_warp_id": 0
			},
			{
				"x": 32,
				"y": 4,
				"elevation": 3,
				"dest_map": "MAP_SEAFOAM_ISLANDS_B3F",
				"dest_warp_id": 1
			},
			{
				"x": 31,
				"y": 17,
				"elevation": 4,
				"dest_map": "MAP_SEAFOAM_ISLANDS_B3F",
				"dest_warp_id": 2
			},
			{
				"x": 7,
				"y": 4,
				"elevation": 3,
				"dest_map": "MAP_SEAFOAM_ISLANDS_B1F",
				"dest_warp_id": 3
			},
			{
				"x": 17,
				"y": 9,
				"elevation": 4,
				"dest_map": "MAP_SEAFOAM_ISLANDS_B1F",
				"dest_warp_id": 4
			},
			{
				"x": 25,
				"y": 19,
				"elevation": 3,
				"dest_map": "MAP_SEAFOAM_ISLANDS_B1F",
				"dest_warp_id": 5
			},
			{
				"x": 32,
				"y": 14,
				"elevation": 4,
				"dest_map": "MAP_SEAFOAM_ISLANDS_B1F",
				"dest_warp_id": 6
			},
			{
				"x": 22,
				"y": 7,
				"elevation": 3,
				"dest_map": "MAP_SEAFOAM_ISLANDS_B1F",
				"dest_warp_id": 7
			},
			{
				"x": 29,
				"y": 8,
				"elevation": 3,
				"dest_map": "MAP_SEAFOAM_ISLANDS_B1F",
				"dest_warp_id": 8
			},
			{
				"x": 24,
				"y": 8,
				"elevation": 3,
				"dest_map": "MAP_SEAFOAM_ISLANDS_B3F",
				"dest_warp_id": 5
			},
			{
				"x": 27,
				"y": 8,
				"elevation": 3,
				"dest_map": "MAP_SEAFOAM_ISLANDS_B3F",
				"dest_warp_id": 6
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_SEAFOAM_ISLANDS_B3F",
		"alias": "SeafoamIslands_B3F",
		"key_items": (),
		"file_name": "SeafoamIslands_B3F",
		"warps": (
			{
				"x": 8,
				"y": 14,
				"elevation": 4,
				"dest_map": "MAP_SEAFOAM_ISLANDS_B2F",
				"dest_warp_id": 0
			},
			{
				"x": 31,
				"y": 4,
				"elevation": 3,
				"dest_map": "MAP_SEAFOAM_ISLANDS_B2F",
				"dest_warp_id": 1
			},
			{
				"x": 31,
				"y": 16,
				"elevation": 4,
				"dest_map": "MAP_SEAFOAM_ISLANDS_B2F",
				"dest_warp_id": 2
			},
			{
				"x": 12,
				"y": 9,
				"elevation": 3,
				"dest_map": "MAP_SEAFOAM_ISLANDS_B4F",
				"dest_warp_id": 0
			},
			{
				"x": 29,
				"y": 5,
				"elevation": 3,
				"dest_map": "MAP_SEAFOAM_ISLANDS_B4F",
				"dest_warp_id": 1
			},
			{
				"x": 23,
				"y": 9,
				"elevation": 1,
				"dest_map": "MAP_SEAFOAM_ISLANDS_B2F",
				"dest_warp_id": 7
			},
			{
				"x": 24,
				"y": 9,
				"elevation": 1,
				"dest_map": "MAP_SEAFOAM_ISLANDS_B2F",
				"dest_warp_id": 8
			},
			{
				"x": 6,
				"y": 18,
				"elevation": 3,
				"dest_map": "MAP_SEAFOAM_ISLANDS_B4F",
				"dest_warp_id": 2
			},
			{
				"x": 9,
				"y": 18,
				"elevation": 3,
				"dest_map": "MAP_SEAFOAM_ISLANDS_B4F",
				"dest_warp_id": 3
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_SEAFOAM_ISLANDS_B4F",
		"alias": "SeafoamIslands_B4F",
		"key_items": (),
		"file_name": "SeafoamIslands_B4F",
		"warps": (
			{
				"x": 15,
				"y": 9,
				"elevation": 4,
				"dest_map": "MAP_SEAFOAM_ISLANDS_B3F",
				"dest_warp_id": 3
			},
			{
				"x": 32,
				"y": 5,
				"elevation": 4,
				"dest_map": "MAP_SEAFOAM_ISLANDS_B3F",
				"dest_warp_id": 4
			},
			{
				"x": 8,
				"y": 17,
				"elevation": 1,
				"dest_map": "MAP_SEAFOAM_ISLANDS_B3F",
				"dest_warp_id": 7
			},
			{
				"x": 9,
				"y": 17,
				"elevation": 1,
				"dest_map": "MAP_SEAFOAM_ISLANDS_B3F",
				"dest_warp_id": 8
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_SILPH_CO_10F",
		"alias": "SilphCo_10F",
		"key_items": (),
		"file_name": "SilphCo_10F",
		"warps": (
			{
				"x": 6,
				"y": 2,
				"elevation": 3,
				"dest_map": "MAP_SILPH_CO_11F",
				"dest_warp_id": 0
			},
			{
				"x": 10,
				"y": 14,
				"elevation": 3,
				"dest_map": "MAP_SILPH_CO_4F",
				"dest_warp_id": 3
			},
			{
				"x": 14,
				"y": 9,
				"elevation": 3,
				"dest_map": "MAP_SILPH_CO_4F",
				"dest_warp_id": 5
			},
			{
				"x": 8,
				"y": 2,
				"elevation": 3,
				"dest_map": "MAP_SILPH_CO_9F",
				"dest_warp_id": 3
			},
			{
				"x": 14,
				"y": 17,
				"elevation": 3,
				"dest_map": "MAP_SILPH_CO_4F",
				"dest_warp_id": 4
			},
			{
				"x": 13,
				"y": 3,
				"elevation": 0,
				"dest_map": "MAP_SILPH_CO_ELEVATOR",
				"dest_warp_id": 0
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_SILPH_CO_11F",
		"alias": "SilphCo_11F",
		"key_items": (),
		"file_name": "SilphCo_11F",
		"warps": (
			{
				"x": 7,
				"y": 2,
				"elevation": 3,
				"dest_map": "MAP_SILPH_CO_10F",
				"dest_warp_id": 0
			},
			{
				"x": 2,
				"y": 5,
				"elevation": 3,
				"dest_map": "MAP_SILPH_CO_7F",
				"dest_warp_id": 1
			},
			{
				"x": 13,
				"y": 3,
				"elevation": 0,
				"dest_map": "MAP_SILPH_CO_ELEVATOR",
				"dest_warp_id": 0
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_SILPH_CO_1F",
		"alias": "SilphCo_1F",
		"key_items": ("master_ball",),
		"file_name": "SilphCo_1F",
		"warps": (
			{
				"x": 7,
				"y": 21,
				"elevation": 0,
				"dest_map": "MAP_SAFFRON_CITY",
				"dest_warp_id": 0
			},
			{
				"x": 8,
				"y": 20,
				"elevation": 3,
				"dest_map": "MAP_SAFFRON_CITY",
				"dest_warp_id": 0,
				"pair_id": 133  # --------------------------------------------------------------
			},
			{
				"x": 9,
				"y": 20,
				"elevation": 3,
				"dest_map": "MAP_SAFFRON_CITY",
				"dest_warp_id": 0
			},
			{
				"x": 31,
				"y": 2,
				"elevation": 3,
				"dest_map": "MAP_SILPH_CO_2F",
				"dest_warp_id": 3
			},
			{
				"x": 22,
				"y": 3,
				"elevation": 0,
				"dest_map": "MAP_SILPH_CO_ELEVATOR",
				"dest_warp_id": 0
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_SILPH_CO_2F",
		"alias": "SilphCo_2F",
		"key_items": (),
		"file_name": "SilphCo_2F",
		"warps": (
			{
				"x": 28,
				"y": 2,
				"elevation": 3,
				"dest_map": "MAP_SILPH_CO_3F",
				"dest_warp_id": 0
			},
			{
				"x": 2,
				"y": 6,
				"elevation": 3,
				"dest_map": "MAP_SILPH_CO_3F",
				"dest_warp_id": 8
			},
			{
				"x": 15,
				"y": 6,
				"elevation": 3,
				"dest_map": "MAP_SILPH_CO_8F",
				"dest_warp_id": 5
			},
			{
				"x": 30,
				"y": 2,
				"elevation": 3,
				"dest_map": "MAP_SILPH_CO_1F",
				"dest_warp_id": 3
			},
			{
				"x": 7,
				"y": 19,
				"elevation": 3,
				"dest_map": "MAP_SILPH_CO_6F",
				"dest_warp_id": 1
			},
			{
				"x": 33,
				"y": 19,
				"elevation": 3,
				"dest_map": "MAP_SILPH_CO_8F",
				"dest_warp_id": 2
			},
			{
				"x": 22,
				"y": 3,
				"elevation": 0,
				"dest_map": "MAP_SILPH_CO_ELEVATOR",
				"dest_warp_id": 0
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_SILPH_CO_3F",
		"alias": "SilphCo_3F",
		"key_items": (),
		"file_name": "SilphCo_3F",
		"warps": (
			{
				"x": 28,
				"y": 2,
				"elevation": 3,
				"dest_map": "MAP_SILPH_CO_2F",
				"dest_warp_id": 0
			},
			{
				"x": 4,
				"y": 6,
				"elevation": 3,
				"dest_map": "MAP_SILPH_CO_5F",
				"dest_warp_id": 1
			},
			{
				"x": 13,
				"y": 14,
				"elevation": 3,
				"dest_map": "MAP_SILPH_CO_7F",
				"dest_warp_id": 4
			},
			{
				"x": 30,
				"y": 2,
				"elevation": 3,
				"dest_map": "MAP_SILPH_CO_4F",
				"dest_warp_id": 2
			},
			{
				"x": 2,
				"y": 14,
				"elevation": 3,
				"dest_map": "MAP_SILPH_CO_9F",
				"dest_warp_id": 2
			},
			{
				"x": 3,
				"y": 20,
				"elevation": 3,
				"dest_map": "MAP_SILPH_CO_5F",
				"dest_warp_id": 4
			},
			{
				"x": 29,
				"y": 14,
				"elevation": 3,
				"dest_map": "MAP_SILPH_CO_3F",
				"dest_warp_id": 7
			},
			{
				"x": 32,
				"y": 20,
				"elevation": 3,
				"dest_map": "MAP_SILPH_CO_3F",
				"dest_warp_id": 6
			},
			{
				"x": 33,
				"y": 5,
				"elevation": 3,
				"dest_map": "MAP_SILPH_CO_2F",
				"dest_warp_id": 1
			},
			{
				"x": 22,
				"y": 3,
				"elevation": 0,
				"dest_map": "MAP_SILPH_CO_ELEVATOR",
				"dest_warp_id": 0
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_SILPH_CO_4F",
		"alias": "SilphCo_4F",
		"key_items": (),
		"file_name": "SilphCo_4F",
		"warps": (
			{
				"x": 28,
				"y": 2,
				"elevation": 3,
				"dest_map": "MAP_SILPH_CO_5F",
				"dest_warp_id": 0
			},
			{
				"x": 18,
				"y": 6,
				"elevation": 3,
				"dest_map": "MAP_SILPH_CO_6F",
				"dest_warp_id": 3
			},
			{
				"x": 30,
				"y": 2,
				"elevation": 3,
				"dest_map": "MAP_SILPH_CO_3F",
				"dest_warp_id": 3
			},
			{
				"x": 12,
				"y": 9,
				"elevation": 3,
				"dest_map": "MAP_SILPH_CO_10F",
				"dest_warp_id": 1
			},
			{
				"x": 2,
				"y": 20,
				"elevation": 3,
				"dest_map": "MAP_SILPH_CO_10F",
				"dest_warp_id": 4
			},
			{
				"x": 18,
				"y": 14,
				"elevation": 3,
				"dest_map": "MAP_SILPH_CO_10F",
				"dest_warp_id": 2
			},
			{
				"x": 22,
				"y": 3,
				"elevation": 0,
				"dest_map": "MAP_SILPH_CO_ELEVATOR",
				"dest_warp_id": 0
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_SILPH_CO_5F",
		"alias": "SilphCo_5F",
		"key_items": ("card_key",),
		"file_name": "SilphCo_5F",
		"warps": (
			{
				"x": 28,
				"y": 2,
				"elevation": 3,
				"dest_map": "MAP_SILPH_CO_4F",
				"dest_warp_id": 0
			},
			{
				"x": 15,
				"y": 7,
				"elevation": 3,
				"dest_map": "MAP_SILPH_CO_3F",
				"dest_warp_id": 1
			},
			{
				"x": 30,
				"y": 2,
				"elevation": 3,
				"dest_map": "MAP_SILPH_CO_6F",
				"dest_warp_id": 2
			},
			{
				"x": 10,
				"y": 20,
				"elevation": 3,
				"dest_map": "MAP_SILPH_CO_9F",
				"dest_warp_id": 1
			},
			{
				"x": 2,
				"y": 20,
				"elevation": 3,
				"dest_map": "MAP_SILPH_CO_3F",
				"dest_warp_id": 5
			},
			{
				"x": 33,
				"y": 5,
				"elevation": 3,
				"dest_map": "MAP_SILPH_CO_7F",
				"dest_warp_id": 2
			},
			{
				"x": 22,
				"y": 3,
				"elevation": 0,
				"dest_map": "MAP_SILPH_CO_ELEVATOR",
				"dest_warp_id": 0
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_SILPH_CO_6F",
		"alias": "SilphCo_6F",
		"key_items": (),
		"file_name": "SilphCo_6F",
		"warps": (
			{
				"x": 14,
				"y": 2,
				"elevation": 3,
				"dest_map": "MAP_SILPH_CO_7F",
				"dest_warp_id": 0
			},
			{
				"x": 29,
				"y": 5,
				"elevation": 3,
				"dest_map": "MAP_SILPH_CO_2F",
				"dest_warp_id": 4
			},
			{
				"x": 26,
				"y": 2,
				"elevation": 3,
				"dest_map": "MAP_SILPH_CO_5F",
				"dest_warp_id": 2
			},
			{
				"x": 2,
				"y": 6,
				"elevation": 3,
				"dest_map": "MAP_SILPH_CO_4F",
				"dest_warp_id": 1
			},
			{
				"x": 20,
				"y": 3,
				"elevation": 0,
				"dest_map": "MAP_SILPH_CO_ELEVATOR",
				"dest_warp_id": 0
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_SILPH_CO_7F",
		"alias": "SilphCo_7F",
		"key_items": (),
		"file_name": "SilphCo_7F",
		"warps": (
			{
				"x": 19,
				"y": 2,
				"elevation": 3,
				"dest_map": "MAP_SILPH_CO_6F",
				"dest_warp_id": 0
			},
			{
				"x": 5,
				"y": 8,
				"elevation": 3,
				"dest_map": "MAP_SILPH_CO_11F",
				"dest_warp_id": 1
			},
			{
				"x": 25,
				"y": 17,
				"elevation": 3,
				"dest_map": "MAP_SILPH_CO_5F",
				"dest_warp_id": 5
			},
			{
				"x": 27,
				"y": 2,
				"elevation": 3,
				"dest_map": "MAP_SILPH_CO_8F",
				"dest_warp_id": 3
			},
			{
				"x": 5,
				"y": 4,
				"elevation": 3,
				"dest_map": "MAP_SILPH_CO_3F",
				"dest_warp_id": 2
			},
			{
				"x": 23,
				"y": 3,
				"elevation": 0,
				"dest_map": "MAP_SILPH_CO_ELEVATOR",
				"dest_warp_id": 0
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_SILPH_CO_8F",
		"alias": "SilphCo_8F",
		"key_items": (),
		"file_name": "SilphCo_8F",
		"warps": (
			{
				"x": 16,
				"y": 2,
				"elevation": 3,
				"dest_map": "MAP_SILPH_CO_9F",
				"dest_warp_id": 0
			},
			{
				"x": 11,
				"y": 10,
				"elevation": 3,
				"dest_map": "MAP_SILPH_CO_8F",
				"dest_warp_id": 4
			},
			{
				"x": 10,
				"y": 6,
				"elevation": 3,
				"dest_map": "MAP_SILPH_CO_2F",
				"dest_warp_id": 5
			},
			{
				"x": 28,
				"y": 2,
				"elevation": 3,
				"dest_map": "MAP_SILPH_CO_7F",
				"dest_warp_id": 3
			},
			{
				"x": 2,
				"y": 12,
				"elevation": 3,
				"dest_map": "MAP_SILPH_CO_8F",
				"dest_warp_id": 1
			},
			{
				"x": 2,
				"y": 17,
				"elevation": 3,
				"dest_map": "MAP_SILPH_CO_2F",
				"dest_warp_id": 2
			},
			{
				"x": 22,
				"y": 3,
				"elevation": 0,
				"dest_map": "MAP_SILPH_CO_ELEVATOR",
				"dest_warp_id": 0
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_SILPH_CO_9F",
		"alias": "SilphCo_9F",
		"key_items": (),
		"file_name": "SilphCo_9F",
		"warps": (
			{
				"x": 16,
				"y": 2,
				"elevation": 0,
				"dest_map": "MAP_SILPH_CO_8F",
				"dest_warp_id": 0
			},
			{
				"x": 22,
				"y": 18,
				"elevation": 3,
				"dest_map": "MAP_SILPH_CO_5F",
				"dest_warp_id": 3
			},
			{
				"x": 9,
				"y": 4,
				"elevation": 3,
				"dest_map": "MAP_SILPH_CO_3F",
				"dest_warp_id": 4
			},
			{
				"x": 18,
				"y": 2,
				"elevation": 3,
				"dest_map": "MAP_SILPH_CO_10F",
				"dest_warp_id": 3
			},
			{
				"x": 24,
				"y": 3,
				"elevation": 0,
				"dest_map": "MAP_SILPH_CO_ELEVATOR",
				"dest_warp_id": 0
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_SSANNE_1F_CORRIDOR",
		"alias": "SSAnne_1F_Corridor",
		"key_items": (),
		"file_name": "SSAnne_1F_Corridor",
		"warps": (
			{
				"x": 3,
				"y": 8,
				"elevation": 3,
				"dest_map": "MAP_SSANNE_2F_CORRIDOR",
				"dest_warp_id": 0,
				"pair_id": 143  # --------------------------------------------------------------
			},
			{
				"x": 2,
				"y": 18,
				"elevation": 3,
				"dest_map": "MAP_SSANNE_KITCHEN",
				"dest_warp_id": 0,
				"pair_id": 144  # --------------------------------------------------------------
			},
			{
				"x": 19,
				"y": 1,
				"elevation": 3,
				"dest_map": "MAP_SSANNE_EXTERIOR",
				"dest_warp_id": 2,
				"pair_id": 145  # --------------------------------------------------------------
			},
			{
				"x": 28,
				"y": 17,
				"elevation": 3,
				"dest_map": "MAP_SSANNE_B1F_CORRIDOR",
				"dest_warp_id": 0,
				"pair_id": 146  # --------------------------------------------------------------
			},
			{
				"x": 5,
				"y": 10,
				"elevation": 3,
				"dest_map": "MAP_SSANNE_1F_ROOM1",
				"dest_warp_id": 0,
				"pair_id": 147  # --------------------------------------------------------------
			},
			{
				"x": 8,
				"y": 10,
				"elevation": 3,
				"dest_map": "MAP_SSANNE_1F_ROOM2",
				"dest_warp_id": 0,
				"pair_id": 148  # --------------------------------------------------------------
			},
			{
				"x": 11,
				"y": 10,
				"elevation": 3,
				"dest_map": "MAP_SSANNE_1F_ROOM3",
				"dest_warp_id": 0,
				"pair_id": 149  # --------------------------------------------------------------
			},
			{
				"x": 14,
				"y": 10,
				"elevation": 3,
				"dest_map": "MAP_SSANNE_1F_ROOM4",
				"dest_warp_id": 0,
				"pair_id": 150  # --------------------------------------------------------------
			},
			{
				"x": 17,
				"y": 10,
				"elevation": 3,
				"dest_map": "MAP_SSANNE_1F_ROOM5",
				"dest_warp_id": 0,
				"pair_id": 151  # --------------------------------------------------------------
			},
			{
				"x": 23,
				"y": 10,
				"elevation": 3,
				"dest_map": "MAP_SSANNE_1F_ROOM7",
				"dest_warp_id": 0,
				"pair_id": 152  # --------------------------------------------------------------
			},
			{
				"x": 20,
				"y": 10,
				"elevation": 3,
				"dest_map": "MAP_SSANNE_1F_ROOM6",
				"dest_warp_id": 0,
				"pair_id": 153  # --------------------------------------------------------------
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_SSANNE_1F_ROOM1",
		"alias": "SSAnne_1F_Room1",
		"key_items": (),
		"file_name": "SSAnne_1F_Room1",
		"warps": (
			{
				"x": 2,
				"y": 1,
				"elevation": 0,
				"dest_map": "MAP_SSANNE_1F_CORRIDOR",
				"dest_warp_id": 6,
				"pair_id": 147  # --------------------------------------------------------------
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_SSANNE_1F_ROOM2",
		"alias": "SSAnne_1F_Room2",
		"key_items": (),
		"file_name": "SSAnne_1F_Room2",
		"warps": (
			{
				"x": 2,
				"y": 1,
				"elevation": 0,
				"dest_map": "MAP_SSANNE_1F_CORRIDOR",
				"dest_warp_id": 7,
				"pair_id": 148  # --------------------------------------------------------------
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_SSANNE_1F_ROOM3",
		"alias": "SSAnne_1F_Room3",
		"key_items": (),
		"file_name": "SSAnne_1F_Room3",
		"warps": (
			{
				"x": 2,
				"y": 1,
				"elevation": 0,
				"dest_map": "MAP_SSANNE_1F_CORRIDOR",
				"dest_warp_id": 8,
				"pair_id": 149  # --------------------------------------------------------------
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_SSANNE_1F_ROOM4",
		"alias": "SSAnne_1F_Room4",
		"key_items": (),
		"file_name": "SSAnne_1F_Room4",
		"warps": (
			{
				"x": 2,
				"y": 1,
				"elevation": 0,
				"dest_map": "MAP_SSANNE_1F_CORRIDOR",
				"dest_warp_id": 9,
				"pair_id": 150  # --------------------------------------------------------------
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_SSANNE_1F_ROOM5",
		"alias": "SSAnne_1F_Room5",
		"key_items": (),
		"file_name": "SSAnne_1F_Room5",
		"warps": (
			{
				"x": 2,
				"y": 1,
				"elevation": 0,
				"dest_map": "MAP_SSANNE_1F_CORRIDOR",
				"dest_warp_id": 10,
				"pair_id": 151  # --------------------------------------------------------------
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_SSANNE_1F_ROOM6",
		"alias": "SSAnne_1F_Room6",
		"key_items": (),
		"file_name": "SSAnne_1F_Room6",
		"warps": (
			{
				"x": 2,
				"y": 1,
				"elevation": 0,
				"dest_map": "MAP_SSANNE_1F_CORRIDOR",
				"dest_warp_id": 12,
				"pair_id": 153  # --------------------------------------------------------------
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_SSANNE_1F_ROOM7",
		"alias": "SSAnne_1F_Room7",
		"key_items": (),
		"file_name": "SSAnne_1F_Room7",
		"warps": (
			{
				"x": 2,
				"y": 1,
				"elevation": 0,
				"dest_map": "MAP_SSANNE_1F_CORRIDOR",
				"dest_warp_id": 11,
				"pair_id": 152  # --------------------------------------------------------------
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_SSANNE_2F_CORRIDOR",
		"alias": "SSAnne_2F_Corridor",
		"key_items": (),
		"file_name": "SSAnne_2F_Corridor",
		"warps": (
			{
				"x": 2,
				"y": 2,
				"elevation": 3,
				"dest_map": "MAP_SSANNE_1F_CORRIDOR",
				"dest_warp_id": 0,
				"pair_id": 143  # --------------------------------------------------------------
			},
			{
				"x": 3,
				"y": 12,
				"elevation": 3,
				"dest_map": "MAP_SSANNE_3F_CORRIDOR",
				"dest_warp_id": 1,
				"pair_id": 154  # --------------------------------------------------------------
			},
			{
				"x": 30,
				"y": 2,
				"elevation": 3,
				"dest_map": "MAP_SSANNE_CAPTAINS_OFFICE",
				"dest_warp_id": 0,
				"pair_id": 155  # --------------------------------------------------------------
			},
			{
				"x": 6,
				"y": 10,
				"elevation": 0,
				"dest_map": "MAP_SSANNE_2F_ROOM1",
				"dest_warp_id": 0,
				"pair_id": 156  # --------------------------------------------------------------
			},
			{
				"x": 10,
				"y": 10,
				"elevation": 0,
				"dest_map": "MAP_SSANNE_2F_ROOM2",
				"dest_warp_id": 0,
				"pair_id": 157  # --------------------------------------------------------------
			},
			{
				"x": 14,
				"y": 10,
				"elevation": 0,
				"dest_map": "MAP_SSANNE_2F_ROOM3",
				"dest_warp_id": 0,
				"pair_id": 158  # --------------------------------------------------------------
			},
			{
				"x": 18,
				"y": 10,
				"elevation": 0,
				"dest_map": "MAP_SSANNE_2F_ROOM4",
				"dest_warp_id": 0,
				"pair_id": 159  # --------------------------------------------------------------
			},
			{
				"x": 22,
				"y": 10,
				"elevation": 0,
				"dest_map": "MAP_SSANNE_2F_ROOM5",
				"dest_warp_id": 0,
				"pair_id": 160  # --------------------------------------------------------------
			},
			{
				"x": 26,
				"y": 10,
				"elevation": 0,
				"dest_map": "MAP_SSANNE_2F_ROOM6",
				"dest_warp_id": 0,
				"pair_id": 161  # --------------------------------------------------------------
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_SSANNE_2F_ROOM1",
		"alias": "SSAnne_2F_Room1",
		"key_items": (),
		"file_name": "SSAnne_2F_Room1",
		"warps": (
			{
				"x": 4,
				"y": 7,
				"elevation": 3,
				"dest_map": "MAP_SSANNE_2F_CORRIDOR",
				"dest_warp_id": 3,
				"pair_id": 156  # --------------------------------------------------------------
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_SSANNE_2F_ROOM2",
		"alias": "SSAnne_2F_Room2",
		"key_items": (),
		"file_name": "SSAnne_2F_Room2",
		"warps": (
			{
				"x": 4,
				"y": 7,
				"elevation": 3,
				"dest_map": "MAP_SSANNE_2F_CORRIDOR",
				"dest_warp_id": 4,
				"pair_id": 157  # --------------------------------------------------------------
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_SSANNE_2F_ROOM3",
		"alias": "SSAnne_2F_Room3",
		"key_items": (),
		"file_name": "SSAnne_2F_Room3",
		"warps": (
			{
				"x": 4,
				"y": 7,
				"elevation": 3,
				"dest_map": "MAP_SSANNE_2F_CORRIDOR",
				"dest_warp_id": 5,
				"pair_id": 158  # --------------------------------------------------------------
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_SSANNE_2F_ROOM4",
		"alias": "SSAnne_2F_Room4",
		"key_items": (),
		"file_name": "SSAnne_2F_Room4",
		"warps": (
			{
				"x": 4,
				"y": 7,
				"elevation": 3,
				"dest_map": "MAP_SSANNE_2F_CORRIDOR",
				"dest_warp_id": 6,
				"pair_id": 159  # --------------------------------------------------------------
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_SSANNE_2F_ROOM5",
		"alias": "SSAnne_2F_Room5",
		"key_items": (),
		"file_name": "SSAnne_2F_Room5",
		"warps": (
			{
				"x": 4,
				"y": 7,
				"elevation": 3,
				"dest_map": "MAP_SSANNE_2F_CORRIDOR",
				"dest_warp_id": 7,
				"pair_id": 160  # --------------------------------------------------------------
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_SSANNE_2F_ROOM6",
		"alias": "SSAnne_2F_Room6",
		"key_items": (),
		"file_name": "SSAnne_2F_Room6",
		"warps": (
			{
				"x": 4,
				"y": 7,
				"elevation": 3,
				"dest_map": "MAP_SSANNE_2F_CORRIDOR",
				"dest_warp_id": 8,
				"pair_id": 161  # --------------------------------------------------------------
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_SSANNE_3F_CORRIDOR",
		"alias": "SSAnne_3F_Corridor",
		"key_items": (),
		"file_name": "SSAnne_3F_Corridor",
		"warps": (
			{
				"x": 1,
				"y": 4,
				"elevation": 3,
				"dest_map": "MAP_SSANNE_DECK",
				"dest_warp_id": 0,
				"pair_id": 162  # --------------------------------------------------------------
			},
			{
				"x": 18,
				"y": 2,
				"elevation": 3,
				"dest_map": "MAP_SSANNE_2F_CORRIDOR",
				"dest_warp_id": 1,
				"pair_id": 154  # --------------------------------------------------------------
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_SSANNE_B1F_CORRIDOR",
		"alias": "SSAnne_B1F_Corridor",
		"key_items": (),
		"file_name": "SSAnne_B1F_Corridor",
		"warps": (
			{
				"x": 19,
				"y": 3,
				"elevation": 3,
				"dest_map": "MAP_SSANNE_1F_CORRIDOR",
				"dest_warp_id": 5,
				"pair_id": 146  # --------------------------------------------------------------
			},
			{
				"x": 2,
				"y": 2,
				"elevation": 0,
				"dest_map": "MAP_SSANNE_B1F_ROOM1",
				"dest_warp_id": 0,
				"pair_id": 163  # --------------------------------------------------------------
			},
			{
				"x": 6,
				"y": 2,
				"elevation": 0,
				"dest_map": "MAP_SSANNE_B1F_ROOM2",
				"dest_warp_id": 0,
				"pair_id": 164  # --------------------------------------------------------------
			},
			{
				"x": 10,
				"y": 2,
				"elevation": 0,
				"dest_map": "MAP_SSANNE_B1F_ROOM3",
				"dest_warp_id": 0,
				"pair_id": 165  # --------------------------------------------------------------
			},
			{
				"x": 14,
				"y": 2,
				"elevation": 0,
				"dest_map": "MAP_SSANNE_B1F_ROOM4",
				"dest_warp_id": 0,
				"pair_id": 166  # --------------------------------------------------------------
			},
			{
				"x": 18,
				"y": 2,
				"elevation": 0,
				"dest_map": "MAP_SSANNE_B1F_ROOM5",
				"dest_warp_id": 0,
				"pair_id": 167  # --------------------------------------------------------------
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_SSANNE_B1F_ROOM1",
		"alias": "SSAnne_B1F_Room1",
		"key_items": (),
		"file_name": "SSAnne_B1F_Room1",
		"warps": (
			{
				"x": 4,
				"y": 7,
				"elevation": 3,
				"dest_map": "MAP_SSANNE_B1F_CORRIDOR",
				"dest_warp_id": 1,
				"pair_id": 163  # --------------------------------------------------------------
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_SSANNE_B1F_ROOM2",
		"alias": "SSAnne_B1F_Room2",
		"key_items": (),
		"file_name": "SSAnne_B1F_Room2",
		"warps": (
			{
				"x": 4,
				"y": 7,
				"elevation": 3,
				"dest_map": "MAP_SSANNE_B1F_CORRIDOR",
				"dest_warp_id": 2,
				"pair_id": 164  # --------------------------------------------------------------
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_SSANNE_B1F_ROOM3",
		"alias": "SSAnne_B1F_Room3",
		"key_items": (),
		"file_name": "SSAnne_B1F_Room3",
		"warps": (
			{
				"x": 4,
				"y": 7,
				"elevation": 3,
				"dest_map": "MAP_SSANNE_B1F_CORRIDOR",
				"dest_warp_id": 3,
				"pair_id": 165  # --------------------------------------------------------------
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_SSANNE_B1F_ROOM4",
		"alias": "SSAnne_B1F_Room4",
		"key_items": (),
		"file_name": "SSAnne_B1F_Room4",
		"warps": (
			{
				"x": 4,
				"y": 7,
				"elevation": 3,
				"dest_map": "MAP_SSANNE_B1F_CORRIDOR",
				"dest_warp_id": 4,
				"pair_id": 166  # --------------------------------------------------------------
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_SSANNE_B1F_ROOM5",
		"alias": "SSAnne_B1F_Room5",
		"key_items": (),
		"file_name": "SSAnne_B1F_Room5",
		"warps": (
			{
				"x": 4,
				"y": 7,
				"elevation": 3,
				"dest_map": "MAP_SSANNE_B1F_CORRIDOR",
				"dest_warp_id": 5,
				"pair_id": 167  # --------------------------------------------------------------
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_SSANNE_CAPTAINS_OFFICE",
		"alias": "SSAnne_CaptainsOffice",
		"key_items": ("hm01_cut",),
		"file_name": "SSAnne_CaptainsOffice",
		"warps": (
			{
				"x": 3,
				"y": 7,
				"elevation": 3,
				"dest_map": "MAP_SSANNE_2F_CORRIDOR",
				"dest_warp_id": 2,
				# "req_items": ("badge2",),
				# "requires_all": True,
				"pair_id": 155  # --------------------------------------------------------------
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_SSANNE_DECK",
		"alias": "SSAnne_Deck",
		"key_items": (),
		"file_name": "SSAnne_Deck",
		"warps": (
			{
				"x": 16,
				"y": 8,
				"elevation": 3,
				"dest_map": "MAP_SSANNE_3F_CORRIDOR",
				"dest_warp_id": 0,
				"pair_id": 162  # --------------------------------------------------------------
			},
			{
				"x": 16,
				"y": 9,
				"elevation": 3,
				"dest_map": "MAP_SSANNE_3F_CORRIDOR",
				"dest_warp_id": 0,
				"pair_id": 162  # --------------------------------------------------------------
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_SSANNE_EXTERIOR",
		"alias": "SSAnne_Exterior",
		"key_items": (),
		"file_name": "SSAnne_Exterior",
		"warps": (
			{
				"x": 32,
				"y": 5,
				"elevation": 3,
				"dest_map": "MAP_VERMILION_CITY",
				"dest_warp_id": 1,
				"pair_id": 168  # --------------------------------------------------------------
			},
			{
				"x": 32,
				"y": 14,
				"elevation": 3,
				"dest_map": "MAP_SSANNE_1F_CORRIDOR",
				"dest_warp_id": 2,
				"pair_id": 145  # --------------------------------------------------------------
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_SSANNE_KITCHEN",
		"alias": "SSAnne_Kitchen",
		"key_items": (),
		"file_name": "SSAnne_Kitchen",
		"warps": (
			{
				"x": 7,
				"y": 1,
				"elevation": 0,
				"dest_map": "MAP_SSANNE_1F_CORRIDOR",
				"dest_warp_id": 1,
				"pair_id": 144  # --------------------------------------------------------------
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_UNDERGROUND_PATH_EAST_ENTRANCE",
		"alias": "UndergroundPath_EastEntrance",
		"key_items": (),
		"file_name": "UndergroundPath_EastEntrance",
		"warps": (
			{
				"x": 6,
				"y": 8,
				"elevation": 3,
				"dest_map": "MAP_ROUTE8",
				"dest_warp_id": 0,
				"pair_id": 130  # --------------------------------------------------------------
			},
			{
				"x": 7,
				"y": 4,
				"elevation": 3,
				"dest_map": "MAP_UNDERGROUND_PATH_EAST_WEST_TUNNEL",
				"dest_warp_id": 0,
				"pair_id": 169  # --------------------------------------------------------------
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_UNDERGROUND_PATH_EAST_WEST_TUNNEL",
		"alias": "UndergroundPath_EastWestTunnel",
		"key_items": (),
		"file_name": "UndergroundPath_EastWestTunnel",
		"warps": (
			{
				"x": 76,
				"y": 3,
				"elevation": 3,
				"dest_map": "MAP_UNDERGROUND_PATH_EAST_ENTRANCE",
				"dest_warp_id": 3,
				"pair_id": 169  # --------------------------------------------------------------
			},
			{
				"x": 3,
				"y": 4,
				"elevation": 3,
				"dest_map": "MAP_UNDERGROUND_PATH_WEST_ENTRANCE",
				"dest_warp_id": 3,
				"pair_id": 170  # --------------------------------------------------------------
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_UNDERGROUND_PATH_NORTH_ENTRANCE",
		"alias": "UndergroundPath_NorthEntrance",
		"key_items": (),
		"file_name": "UndergroundPath_NorthEntrance",
		"warps": (
			{
				"x": 6,
				"y": 8,
				"elevation": 3,
				"dest_map": "MAP_ROUTE5",
				"dest_warp_id": 0,
				"pair_id": 120  # --------------------------------------------------------------
			},
			{
				"x": 7,
				"y": 4,
				"elevation": 3,
				"dest_map": "MAP_UNDERGROUND_PATH_NORTH_SOUTH_TUNNEL",
				"dest_warp_id": 0,
				"pair_id": 171  # --------------------------------------------------------------
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_UNDERGROUND_PATH_NORTH_SOUTH_TUNNEL",
		"alias": "UndergroundPath_NorthSouthTunnel",
		"key_items": (),
		"file_name": "UndergroundPath_NorthSouthTunnel",
		"warps": (
			{
				"x": 4,
				"y": 3,
				"elevation": 3,
				"dest_map": "MAP_UNDERGROUND_PATH_NORTH_ENTRANCE",
				"dest_warp_id": 3,
				"pair_id": 171  # --------------------------------------------------------------
			},
			{
				"x": 3,
				"y": 60,
				"elevation": 3,
				"dest_map": "MAP_UNDERGROUND_PATH_SOUTH_ENTRANCE",
				"dest_warp_id": 3,
				"pair_id": 172  # --------------------------------------------------------------
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_UNDERGROUND_PATH_SOUTH_ENTRANCE",
		"alias": "UndergroundPath_SouthEntrance",
		"key_items": (),
		"file_name": "UndergroundPath_SouthEntrance",
		"warps": (
			{
				"x": 6,
				"y": 8,
				"elevation": 3,
				"dest_map": "MAP_ROUTE6",
				"dest_warp_id": 0,
				"pair_id": 124  # --------------------------------------------------------------
			},
			{
				"x": 7,
				"y": 4,
				"elevation": 3,
				"dest_map": "MAP_UNDERGROUND_PATH_NORTH_SOUTH_TUNNEL",
				"dest_warp_id": 1,
				"pair_id": 172  # --------------------------------------------------------------
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_UNDERGROUND_PATH_WEST_ENTRANCE",
		"alias": "UndergroundPath_WestEntrance",
		"key_items": (),
		"file_name": "UndergroundPath_WestEntrance",
		"warps": (
			{
				"x": 6,
				"y": 8,
				"elevation": 3,
				"dest_map": "MAP_ROUTE7",
				"dest_warp_id": 0,
				"pair_id": 127  # --------------------------------------------------------------
			},
			{
				"x": 7,
				"y": 4,
				"elevation": 3,
				"dest_map": "MAP_UNDERGROUND_PATH_EAST_WEST_TUNNEL",
				"dest_warp_id": 1,
				"pair_id": 170  # --------------------------------------------------------------
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_VERMILION_CITY",
		"alias": "VermilionCity",
		"key_items": (),
		"file_name": "VermilionCity",
		"warps": (
			# {
			# 	"x": 22,
			# 	"y": 34,
			# 	"elevation": 3,
			# 	"dest_map": "MAP_SSANNE_EXTERIOR",
			# 	"dest_warp_id": 1,
			# 	"req_items": ("ssanne_ticket",),
			# 	"requires_all": True,
			# 	"pair_id": 168
			# },
			# {
			# 	"x": 23,
			# 	"y": 34,
			# 	"elevation": 3,
			# 	"dest_map": "MAP_SSANNE_EXTERIOR",
			# 	"dest_warp_id": 1,
			# 	"req_items": ("ssanne_ticket",),
			# 	"requires_all": True,
			# 	"pair_id": 168  # --------------------------------------------------------------
			# },
			# {
			# 	"x": 24,
			# 	"y": 34,
			# 	"elevation": 3,
			# 	"dest_map": "MAP_SSANNE_EXTERIOR",
			# 	"dest_warp_id": 1,
			# 	"req_items": ("ssanne_ticket",),
			# 	"requires_all": True,
			# 	"pair_id": 168
			# },
			{
				"x": 9,
				"y": 6,
				"elevation": 0,
				"dest_map": "MAP_VERMILION_CITY_HOUSE1",
				"dest_warp_id": 1,
				"pair_id": 173  # --------------------------------------------------------------
			},
			{
				"x": 15,
				"y": 6,
				"elevation": 3,
				"dest_map": "MAP_VERMILION_CITY_POKEMON_CENTER_1F",
				"dest_warp_id": 1,
				"pair_id": 174  # --------------------------------------------------------------
			},
			{
				"x": 12,
				"y": 17,
				"elevation": 0,
				"dest_map": "MAP_VERMILION_CITY_POKEMON_FAN_CLUB",
				"dest_warp_id": 1,
				"pair_id": 175  # --------------------------------------------------------------
			},
			{
				"x": 19,
				"y": 17,
				"elevation": 0,
				"dest_map": "MAP_VERMILION_CITY_HOUSE2",
				"dest_warp_id": 1,
				"pair_id": 176  # --------------------------------------------------------------
			},
			{
				"x": 29,
				"y": 17,
				"elevation": 0,
				"dest_map": "MAP_VERMILION_CITY_MART",
				"dest_warp_id": 1,
				"pair_id": 177  # --------------------------------------------------------------
			},
			{
				"x": 28,
				"y": 24,
				"elevation": 0,
				"dest_map": "MAP_VERMILION_CITY_HOUSE3",
				"dest_warp_id": 1,
				"pair_id": 178  # --------------------------------------------------------------
			},
			# {
			# 	"x": 14,
			# 	"y": 25,
			# 	"elevation": 0,
			# 	"dest_map": "MAP_VERMILION_CITY_GYM",
			# 	"dest_warp_id": 1,
			# 	"req_items": ("hm01_cut", "hm03_surf",),
			# 	"requires_all": False,
			# 	"pair_id": 179  # --------------------------------------------------------------
			# },
		),
		"connections": (
			("Route6", None),
			("Route11_W", None),
			("VermilionCity_GateKeep", ("ssanne_ticket",)),
			("VermilionCity_War_Hero", ("hm01_cut", "hm03_surf",)),
		),
	},
	{
		"id": "MAP_VERMILION_CITY",
		"alias": "VermilionCity_GateKeep",
		"key_items": (),
		"file_name": "VermilionCity",
		"warps": (
			{
				"x": 22,
				"y": 34,
				"elevation": 3,
				"dest_map": "MAP_SSANNE_EXTERIOR",
				"dest_warp_id": 1,
				# "req_items": ("ssanne_ticket",),
				# "requires_all": True,
				"pair_id": 168
			},
			{
				"x": 23,
				"y": 34,
				"elevation": 3,
				"dest_map": "MAP_SSANNE_EXTERIOR",
				"dest_warp_id": 1,
				# "req_items": ("ssanne_ticket",),
				# "requires_all": True,
				"pair_id": 168  # --------------------------------------------------------------
			},
			{
				"x": 24,
				"y": 34,
				"elevation": 3,
				"dest_map": "MAP_SSANNE_EXTERIOR",
				"dest_warp_id": 1,
				# "req_items": ("ssanne_ticket",),
				# "requires_all": True,
				"pair_id": 168
			},
		),
		"connections": (
			("VermilionCity", ("ssanne_ticket",)),
		),
	},
	{
		"id": "MAP_VERMILION_CITY",
		"alias": "VermilionCity_War_Hero",
		"key_items": (),
		"file_name": "VermilionCity",
		"warps": (
			{
				"x": 14,
				"y": 25,
				"elevation": 0,
				"dest_map": "MAP_VERMILION_CITY_GYM",
				"dest_warp_id": 1,
				# "req_items": ("hm01_cut", "hm03_surf",),
				# "requires_all": False,
				"pair_id": 179  # --------------------------------------------------------------
			},
		),
		"connections": (
			("VermilionCity", ("hm01_cut", "hm03_surf",)),
		),
	},
	{
		"id": "MAP_VERMILION_CITY_GYM",
		"alias": "VermilionCity_Gym",
		"key_items": ("badge3",),
		"file_name": "VermilionCity_Gym",
		"warps": (
			{
				"x": 5,
				"y": 19,
				"elevation": 3,
				"dest_map": "MAP_VERMILION_CITY",
				"dest_warp_id": 9,
				"pair_id": 179  # --------------------------------------------------------------
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_VERMILION_CITY_HOUSE1",
		"alias": "VermilionCity_House1",
		"key_items": (),
		"file_name": "VermilionCity_House1",
		"warps": (
			{
				"x": 4,
				"y": 7,
				"elevation": 3,
				"dest_map": "MAP_VERMILION_CITY",
				"dest_warp_id": 3,
				"pair_id": 173  # --------------------------------------------------------------
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_VERMILION_CITY_HOUSE2",
		"alias": "VermilionCity_House2",
		"key_items": (),
		"file_name": "VermilionCity_House2",
		"warps": (
			{
				"x": 4,
				"y": 7,
				"elevation": 3,
				"dest_map": "MAP_VERMILION_CITY",
				"dest_warp_id": 6,
				"pair_id": 176  # --------------------------------------------------------------
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_VERMILION_CITY_HOUSE3",
		"alias": "VermilionCity_House3",
		"key_items": (),
		"file_name": "VermilionCity_House3",
		"warps": (
			{
				"x": 4,
				"y": 7,
				"elevation": 3,
				"dest_map": "MAP_VERMILION_CITY",
				"dest_warp_id": 8,
				"pair_id": 178  # --------------------------------------------------------------
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_VERMILION_CITY_MART",
		"alias": "VermilionCity_Mart",
		"key_items": (),
		"file_name": "VermilionCity_Mart",
		"warps": (
			{
				"x": 4,
				"y": 7,
				"elevation": 3,
				"dest_map": "MAP_VERMILION_CITY",
				"dest_warp_id": 7,
				"pair_id": 177  # --------------------------------------------------------------
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_VERMILION_CITY_POKEMON_CENTER_1F",
		"alias": "VermilionCity_PokemonCenter_1F",
		"key_items": (),
		"file_name": "VermilionCity_PokemonCenter_1F",
		"warps": (
			{
				"x": 7,
				"y": 8,
				"elevation": 3,
				"dest_map": "MAP_VERMILION_CITY",
				"dest_warp_id": 4,
				"pair_id": 174  # --------------------------------------------------------------
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_VERMILION_CITY_POKEMON_FAN_CLUB",
		"alias": "VermilionCity_PokemonFanClub",
		"key_items": ("bike_voucher",),
		"file_name": "VermilionCity_PokemonFanClub",
		"warps": (
			{
				"x": 5,
				"y": 10,
				"elevation": 3,
				"dest_map": "MAP_VERMILION_CITY",
				"dest_warp_id": 5,
				"pair_id": 175  # --------------------------------------------------------------
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_VICTORY_ROAD_1F",
		"alias": "VictoryRoad_1F",
		"key_items": (),
		"file_name": "VictoryRoad_1F",
		"warps": (
			{
				"x": 11,
				"y": 20,
				"elevation": 3,
				"dest_map": "MAP_ROUTE23",
				"dest_warp_id": 0,
				# "req_items": ("hm04_strength",),
				# "requires_all": True,
				"pair_id": 180  # --------------------------------------------------------------
			},
		),
		"connections": (
			("VictoryRoad_2F", ("hm04_strength",)),
		),
	},
	{
		"id": "MAP_VICTORY_ROAD_2F",
		"alias": "VictoryRoad_2F",
		"key_items": (),
		"file_name": "VictoryRoad_2F",
		"warps": (
			{
				"x": 1,
				"y": 9,
				"elevation": 3,
				"dest_map": "MAP_VICTORY_ROAD_1F",
				"dest_warp_id": 0
			},
			{
				"x": 3,
				"y": 3,
				"elevation": 3,
				"dest_map": "MAP_VICTORY_ROAD_3F",
				"dest_warp_id": 0
			},
			{
				"x": 34,
				"y": 9,
				"elevation": 3,
				"dest_map": "MAP_VICTORY_ROAD_3F",
				"dest_warp_id": 1
			},
			{
				"x": 38,
				"y": 9,
				"elevation": 3,
				"dest_map": "MAP_VICTORY_ROAD_3F",
				"dest_warp_id": 2
			},
			{
				"x": 36,
				"y": 17,
				"elevation": 4,
				"dest_map": "MAP_VICTORY_ROAD_3F",
				"dest_warp_id": 3
			},
			{
				"x": 49,
				"y": 13,
				"elevation": 0,
				"dest_map": "MAP_ROUTE23",
				"dest_warp_id": 1
			},
			{
				"x": 48,
				"y": 12,
				"elevation": 3,
				"dest_map": "MAP_ROUTE23",
				"dest_warp_id": 1,
				# "req_items": ("hm04_strength",),
				# "requires_all": True,
				"pair_id": 181  # --------------------------------------------------------------
			},
			{
				"x": 47,
				"y": 13,
				"elevation": 0,
				"dest_map": "MAP_ROUTE23",
				"dest_warp_id": 1
			},
			{
				"x": 34,
				"y": 19,
				"elevation": 3,
				"dest_map": "MAP_VICTORY_ROAD_3F",
				"dest_warp_id": 4
			},
		),
		"connections": (
			("VictoryRoad_1F", ("hm04_strength",)),
		),
	},
	{
		"id": "MAP_VICTORY_ROAD_3F",
		"alias": "VictoryRoad_3F",
		"key_items": (),
		"file_name": "VictoryRoad_3F",
		"warps": (
			{
				"x": 5,
				"y": 2,
				"elevation": 3,
				"dest_map": "MAP_VICTORY_ROAD_2F",
				"dest_warp_id": 1
			},
			{
				"x": 34,
				"y": 9,
				"elevation": 3,
				"dest_map": "MAP_VICTORY_ROAD_2F",
				"dest_warp_id": 2
			},
			{
				"x": 37,
				"y": 10,
				"elevation": 3,
				"dest_map": "MAP_VICTORY_ROAD_2F",
				"dest_warp_id": 3
			},
			{
				"x": 39,
				"y": 17,
				"elevation": 3,
				"dest_map": "MAP_VICTORY_ROAD_2F",
				"dest_warp_id": 4
			},
			{
				"x": 34,
				"y": 18,
				"elevation": 3,
				"dest_map": "MAP_VICTORY_ROAD_2F",
				"dest_warp_id": 8
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_VIRIDIAN_CITY",
		"alias": "ViridianCity_N",
		"key_items": (),
		"file_name": "ViridianCity",
		"warps": (
			# {
			# 	"x": 36,
			# 	"y": 10,
			# 	"elevation": 0,
			# 	"dest_map": "MAP_VIRIDIAN_CITY_GYM",
			# 	"dest_warp_id": 1,
			# 	"req_items": ("badge2", "badge3", "badge4", "badge5", "badge6", "badge7",),
			# 	"requires_all": True,
			# 	"pair_id": 184  # --------------------------------------------------------------
			# },
		),
		"connections": (
			("Route2_SW", None),
			("ViridianCity", ("oaks_parcel", "hm01_cut",)),
			("ViridianCity_Evil", ("all_badges",))
		)
	},
	{
		"id": "MAP_VIRIDIAN_CITY",
		"alias": "ViridianCity_Evil",
		"key_items": (),
		"file_name": "ViridianCity",
		"warps": (
			{
				"x": 36,
				"y": 10,
				"elevation": 0,
				"dest_map": "MAP_VIRIDIAN_CITY_GYM",
				"dest_warp_id": 1,
				# "req_items": ("badge2", "badge3", "badge4", "badge5", "badge6", "badge7",),
				# "requires_all": True,
				"pair_id": 184  # --------------------------------------------------------------
			},
		),
		"connections": (
			("ViridianCity_N", ("all_badges",)),
		)
	},
	{
		"id": "MAP_VIRIDIAN_CITY",
		"alias": "ViridianCity",
		"key_items": (),
		"file_name": "ViridianCity",
		"warps": (
			{
				"x": 26,
				"y": 26,
				"elevation": 0,
				"dest_map": "MAP_VIRIDIAN_CITY_POKEMON_CENTER_1F",
				"dest_warp_id": 1,
				"pair_id": 182  # --------------------------------------------------------------
			},
			{
				"x": 25,
				"y": 11,
				"elevation": 3,
				"dest_map": "MAP_VIRIDIAN_CITY_HOUSE1",
				"dest_warp_id": 1,
				"pair_id": 183  # --------------------------------------------------------------
			},
			{
				"x": 25,
				"y": 18,
				"elevation": 0,
				"dest_map": "MAP_VIRIDIAN_CITY_HOUSE2",
				"dest_warp_id": 1,
				"pair_id": 185  # --------------------------------------------------------------
			},
			{
				"x": 36,
				"y": 19,
				"elevation": 0,
				"dest_map": "MAP_VIRIDIAN_CITY_MART",
				"dest_warp_id": 1,
				"pair_id": 186  # --------------------------------------------------------------
			},
		),
		"connections": (
			("ViridianCity_N", ("oaks_parcel", "hm01_cut",)),
			("Route22", None),
		),
	},
	{
		"id": "MAP_VIRIDIAN_CITY_GYM",
		"alias": "ViridianCity_Gym",
		"key_items": ("badge8",),
		"file_name": "ViridianCity_Gym",
		"warps": (
			{
				"x": 17,
				"y": 22,
				"elevation": 3,
				"dest_map": "MAP_VIRIDIAN_CITY",
				"dest_warp_id": 2,
				"pair_id": 184  # --------------------------------------------------------------
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_VIRIDIAN_CITY_HOUSE1",
		"alias": "ViridianCity_House1",
		"key_items": (),
		"file_name": "ViridianCity_House1",
		"warps": (
			{
				"x": 4,
				"y": 7,
				"elevation": 0,
				"dest_map": "MAP_VIRIDIAN_CITY",
				"dest_warp_id": 1,
				"pair_id": 183  # --------------------------------------------------------------
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_VIRIDIAN_CITY_HOUSE2",
		"alias": "ViridianCity_House2",
		"key_items": (),
		"file_name": "ViridianCity_House2",
		"warps": (
			{
				"x": 4,
				"y": 7,
				"elevation": 0,
				"dest_map": "MAP_VIRIDIAN_CITY",
				"dest_warp_id": 3,
				"pair_id": 185  # --------------------------------------------------------------
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_VIRIDIAN_CITY_MART",
		"alias": "ViridianCity_Mart",
		"key_items": ("oaks_parcel",),
		"file_name": "ViridianCity_Mart",
		"warps": (
			{
				"x": 4,
				"y": 7,
				"elevation": 3,
				"dest_map": "MAP_VIRIDIAN_CITY",
				"dest_warp_id": 4,
				"pair_id": 186  # --------------------------------------------------------------
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_VIRIDIAN_CITY_POKEMON_CENTER_1F",
		"alias": "ViridianCity_PokemonCenter_1F",
		"key_items": (),
		"file_name": "ViridianCity_PokemonCenter_1F",
		"warps": (
			{
				"x": 7,
				"y": 8,
				"elevation": 3,
				"dest_map": "MAP_VIRIDIAN_CITY",
				"dest_warp_id": 0,
				"pair_id": 182  # --------------------------------------------------------------
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_VIRIDIAN_FOREST",
		"alias": "ViridianForest",
		"key_items": (),
		"file_name": "ViridianForest",
		"warps": (
			{
				"x": 29,
				"y": 62,
				"elevation": 3,
				"dest_map": "MAP_ROUTE2_VIRIDIAN_FOREST_SOUTH_ENTRANCE",
				"dest_warp_id": 3,
				"pair_id": 116  # --------------------------------------------------------------
			},
			{
				"x": 28,
				"y": 62,
				"elevation": 3,
				"dest_map": "MAP_ROUTE2_VIRIDIAN_FOREST_SOUTH_ENTRANCE",
				"dest_warp_id": 3,
				"pair_id": 116  # --------------------------------------------------------------
			},
			{
				"x": 5,
				"y": 9,
				"elevation": 3,
				"dest_map": "MAP_ROUTE2_VIRIDIAN_FOREST_NORTH_ENTRANCE",
				"dest_warp_id": 1,
				"pair_id": 117  # --------------------------------------------------------------
			},
			{
				"x": 6,
				"y": 9,
				"elevation": 3,
				"dest_map": "MAP_ROUTE2_VIRIDIAN_FOREST_NORTH_ENTRANCE",
				"dest_warp_id": 1,
				"pair_id": 117  # --------------------------------------------------------------
			},
			{
				"x": 30,
				"y": 62,
				"elevation": 3,
				"dest_map": "MAP_ROUTE2_VIRIDIAN_FOREST_SOUTH_ENTRANCE",
				"dest_warp_id": 3,
				"pair_id": 116  # --------------------------------------------------------------
			},
			{
				"x": 4,
				"y": 9,
				"elevation": 3,
				"dest_map": "MAP_ROUTE2_VIRIDIAN_FOREST_NORTH_ENTRANCE",
				"dest_warp_id": 1,
				"pair_id": 117  # --------------------------------------------------------------
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_CERULEAN_CAVE_1F",
		"alias": "CeruleanCave_1F",
		"key_items": (),
		"file_name": "CeruleanCave_1F",
		"low_priority": True,
		"warps": (
			{
				"x": 33,
				"y": 21,
				"elevation": 3,
				"dest_map": "MAP_CERULEAN_CITY",
				"dest_warp_id": 7,
				# "req_items": ("hm03_surf", "hm06_rocksmash",),
				# "requires_all": True,
				"pair_id": 200
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_MT_EMBER_SUMMIT",
		"alias": "MtEmber_Summit",
		"key_items": (),
		"file_name": "MtEmber_Summit",
		"low_priority": True,
		"warps": (
			{
				"x": 9,
				"y": 15,
				"elevation": 0,
				"dest_map": "MAP_MT_EMBER_EXTERIOR",
				"dest_warp_id": 4,
				# "req_items": ("hm04_strength",),
				# "requires_all": True,
				"pair_id": 201,

			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_MT_EMBER_EXTERIOR",
		"alias": "MtEmber_Exterior",
		"key_items": (),
		"file_name": "MtEmber_Exterior",
		"skip": True,
		"warps": (
			{
				"x": 29,
				"y": 7,
				"elevation": 3,
				"dest_map": "MAP_EMBER_SUMMIT",
				"dest_warp_id": 0,
				"req_items": ("hm04_strength",),
				"requires_all": True,
				"pair_id": 201,
				"skip": True
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_ONE_ISLAND_KINDLE_ROAD_EMBER_SPA",
		"alias": "OneIsland_KindleRoad_EmberSpa",
		"key_items": ("hm06_rocksmash",),
		"file_name": "OneIsland_KindleRoad_EmberSpa",
		"warps": (
			{
				"x": 13,
				"y": 36,
				"elevation": 3,
				"dest_map": "MAP_ONE_ISLAND_KINDLE_ROAD",
				"dest_warp_id": 2,
				"pair_id": 235,
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_ONE_ISLAND_KINDLE_ROAD",
		"alias": "OneIsland_KindleRoad",
		"key_items": (),
		"file_name": "OneIsland_KindleRoad",
		"skip": True,
		"warps": (
			{
				"x": 15,
				"y": 58,
				"elevation": 3,
				"dest_map": "MAP_ONE_ISLAND_KINDLE_ROAD_EMBER_SPA",
				"dest_warp_id": 0,
				"pair_id": 235,
				"skip": True
			},
		),
		"connections": (
		),
	},
	{
		"id": "MAP_TWO_ISLAND_HOUSE",
		"alias": "TwoIsland_House",
		"key_items": (),
		"file_name": "TwoIsland_House",
		"low_priority": True,
		"warps": (
			{
				"x": 4,
				"y": 7,
				"elevation": 3,
				"dest_map": "MAP_TWO_ISLAND",
				"dest_warp_id": 1,
				"pair_id": 253
			},
		),
		"connections": (
		)
	},
	{
		"id": "MAP_FOUR_ISLAND_HOUSE1",
		"alias": "FourIsland_House1",
		"key_items": (),
		"file_name": "FourIsland_House1",
		"low_priority": True,
		"warps": (
			{
				"x": 4,
				"y": 7,
				"elevation": 3,
				"dest_map": "MAP_FOUR_ISLAND",
				"dest_warp_id": 2,
				"pair_id": 254
			},
		),
		"connections": (
		)
	},
	{
		"id": "MAP_SEVEN_ISLAND_SEVAULT_CANYON_HOUSE",
		"alias": "SevenIsland_SevaultCanyon_House",
		"key_items": (),
		"file_name": "SevenIsland_SevaultCanyon_House",
		"low_priority": True,
		"warps": (
			{
				"x": 4,
				"y": 7,
				"elevation": 3,
				"dest_map": "MAP_SEVEN_ISLAND_SEVAULT_CANYON",
				"dest_warp_id": 1,
				"pair_id": 255
			},
		),
		"connections": (
		)
	},
	{
		"id": "MAP_TWO_ISLAND_CAPE_BRINK_HOUSE",
		"alias": "TwoIsland_CapeBrink_House",
		"key_items": (),
		"file_name": "TwoIsland_CapeBrink_House",
		"low_priority": True,
		"warps": (
			{
				"x": 4,
				"y": 7,
				"elevation": 3,
				"dest_map": "MAP_TWO_ISLAND_CAPE_BRINK",
				"dest_warp_id": 0,
				"pair_id": 256
			},
		),
		"connections": (
		)
	},
	{
		"id": "MAP_BIRTH_ISLAND_EXTERIOR",
		"alias": "BirthIsland_Exterior",
		"key_items": (),
		"file_name": "BirthIsland_Exterior",
		"low_priority": True,
		"warps": (
			{
				"x": 15,
				"y": 24,
				"elevation": 3,
				"dest_map": "MAP_BIRTH_ISLAND_HARBOR",
				"dest_warp_id": 0,
				"pair_id": 257
			},
		),
		"connections": (
		)
	},
	{
		"id": "MAP_NAVEL_ROCK_BASE",
		"alias": "NavelRock_Base",
		"key_items": (),
		"file_name": "NavelRock_Base",
		"low_priority": True,
		"warps": (
			{
				"x": 13,
				"y": 20,
				"elevation": 3,
				"dest_map": "MAP_NAVEL_ROCK_BASE_PATH_B11F",
				"dest_warp_id": 1,
				"pair_id": 258
			},
		),
		"connections": (
		)
	},
	{
		"id": "MAP_NAVEL_ROCK_SUMMIT",
		"alias": "NavelRock_Summit",
		"key_items": (),
		"file_name": "NavelRock_Summit",
		"low_priority": True,
		"warps": (
			{
				"x": 10,
				"y": 18,
				"elevation": 3,
				"dest_map": "MAP_NAVEL_ROCK_SUMMIT_PATH_5F",
				"dest_warp_id": 1,
				"pair_id": 259
			},
		),
		"connections": (
		)
	},
	{
		"id": "MAP_SEVEN_ISLAND_TANOBY_RUINS_VIAPOIS_CHAMBER",
		"alias": "SevenIsland_TanobyRuins_ViapoisChamber",
		"key_items": (),
		"file_name": "SevenIsland_TanobyRuins_ViapoisChamber",
		"low_priority": True,
		"warps": (
			{
				"x": 11,
				"y": 15,
				"elevation": 3,
				"dest_map": "MAP_SEVEN_ISLAND_TANOBY_RUINS",
				"dest_warp_id": 6,
				"pair_id": 260
			},
		),
		"connections": (
		)
	},
	{
		"id": "MAP_SEVEN_ISLAND_TANOBY_RUINS_RIXY_CHAMBER",
		"alias": "SevenIsland_TanobyRuins_RixyChamber",
		"key_items": (),
		"file_name": "SevenIsland_TanobyRuins_RixyChamber",
		"low_priority": True,
		"warps": (
			{
				"x": 11,
				"y": 15,
				"elevation": 3,
				"dest_map": "MAP_SEVEN_ISLAND_TANOBY_RUINS",
				"dest_warp_id": 5,
				"pair_id": 261
			},
		),
		"connections": (
		)
	},
	{
		"id": "MAP_SEVEN_ISLAND_TANOBY_RUINS_SCUFIB_CHAMBER",
		"alias": "SevenIsland_TanobyRuins_ScufibChamber",
		"key_items": (),
		"file_name": "SevenIsland_TanobyRuins_ScufibChamber",
		"low_priority": True,
		"warps": (
			{
				"x": 11,
				"y": 15,
				"elevation": 3,
				"dest_map": "MAP_SEVEN_ISLAND_TANOBY_RUINS",
				"dest_warp_id": 4,
				"pair_id": 262
			},
		),
		"connections": (
		)
	},
	{
		"id": "MAP_SEVEN_ISLAND_TANOBY_RUINS_DILFORD_CHAMBER",
		"alias": "SevenIsland_TanobyRuins_DilfordChamber",
		"key_items": (),
		"file_name": "SevenIsland_TanobyRuins_DilfordChamber",
		"low_priority": True,
		"warps": (
			{
				"x": 11,
				"y": 15,
				"elevation": 3,
				"dest_map": "MAP_SEVEN_ISLAND_TANOBY_RUINS",
				"dest_warp_id": 3,
				"pair_id": 263
			},
		),
		"connections": (
		)
	},
	{
		"id": "MAP_SEVEN_ISLAND_TANOBY_RUINS_WEEPTH_CHAMBER",
		"alias": "SevenIsland_TanobyRuins_WeepthChamber",
		"key_items": (),
		"file_name": "SevenIsland_TanobyRuins_WeepthChamber",
		"low_priority": True,
		"warps": (
			{
				"x": 11,
				"y": 15,
				"elevation": 3,
				"dest_map": "MAP_SEVEN_ISLAND_TANOBY_RUINS",
				"dest_warp_id": 2,
				"pair_id": 264
			},
		),
		"connections": (
		)
	},
	{
		"id": "MAP_SEVEN_ISLAND_TANOBY_RUINS_LIPTOO_CHAMBER",
		"alias": "SevenIsland_TanobyRuins_LiptooChamber",
		"key_items": (),
		"file_name": "SevenIsland_TanobyRuins_LiptooChamber",
		"low_priority": True,
		"warps": (
			{
				"x": 11,
				"y": 15,
				"elevation": 3,
				"dest_map": "MAP_SEVEN_ISLAND_TANOBY_RUINS",
				"dest_warp_id": 1,
				"pair_id": 265
			},
		),
		"connections": (
		)
	},
	{
		"id": "MAP_SEVEN_ISLAND_TANOBY_RUINS_MONEAN_CHAMBER",
		"alias": "SevenIsland_TanobyRuins_MoneanChamber",
		"key_items": (),
		"file_name": "SevenIsland_TanobyRuins_MoneanChamber",
		"low_priority": True,
		"warps": (
			{
				"x": 11,
				"y": 15,
				"elevation": 3,
				"dest_map": "MAP_SEVEN_ISLAND_TANOBY_RUINS",
				"dest_warp_id": 0,
				"pair_id": 266
			},
		),
		"connections": (
		)
	},
	{
		"id": "MAP_SEVEN_ISLAND_SEVAULT_CANYON_TANOBY_KEY",
		"alias": "SevenIsland_SevaultCanyon_TanobyKey",
		"key_items": (),
		"file_name": "SevenIsland_SevaultCanyon_TanobyKey",
		"low_priority": True,
		"warps": (
			{
				"x": 7,
				"y": 13,
				"elevation": 3,
				"dest_map": "MAP_SEVEN_ISLAND_SEVAULT_CANYON",
				"dest_warp_id": 0,
				# "req_items": ("hm04_strength",),
				# "requires_all": True,
				"pair_id": 267
			},
		),
		"connections": (
		)
	},
	{
		"id": "MAP_FIVE_ISLAND_LOST_CAVE_ROOM13",
		"alias": "FiveIsland_LostCave_Room13",
		"key_items": (),
		"file_name": "FiveIsland_LostCave_Room13",
		"low_priority": True,
		"warps": (
			{
				"x": 2,
				"y": 5,
				"elevation": 3,
				"dest_map": "MAP_FIVE_ISLAND_LOST_CAVE_ROOM1",
				"dest_warp_id": 2,
				"pair_id": 268
			},
		),
		"connections": (
		)
	},
	{
		"id": "MAP_FIVE_ISLAND_LOST_CAVE_ROOM14",
		"alias": "FiveIsland_LostCave_Room14",
		"key_items": (),
		"file_name": "FiveIsland_LostCave_Room14",
		"low_priority": True,
		"warps": (
			{
				"x": 8,
				"y": 5,
				"elevation": 3,
				"dest_map": "MAP_FIVE_ISLAND_LOST_CAVE_ROOM1",
				"dest_warp_id": 4,
				"pair_id": 269
			},
		),
		"connections": (
		)
	},
	{
		"id": "MAP_SIX_ISLAND_ALTERING_CAVE",
		"alias": "SixIsland_AlteringCave",
		"key_items": (),
		"file_name": "SixIsland_AlteringCave",
		"low_priority": True,
		"warps": (
			{
				"x": 18,
				"y": 22,
				"elevation": 3,
				"dest_map": "MAP_SIX_ISLAND_OUTCAST_ISLAND",
				"dest_warp_id": 0,
				"pair_id": 270
			},
		),
		"connections": (
		)
	},
	{
		"id": "MAP_FOUR_ISLAND_POKEMON_DAY_CARE",
		"alias": "FourIsland_PokemonDayCare",
		"key_items": (),
		"file_name": "FourIsland_PokemonDayCare",
		"low_priority": True,
		"warps": (
			{
				"x": 4,
				"y": 7,
				"elevation": 3,
				"dest_map": "MAP_FOUR_ISLAND",
				"dest_warp_id": 1,
				"pair_id": 271
			},
		),
		"connections": (
		)
	},
	{
		"id": "MAP_FIVE_ISLAND_LOST_CAVE_ROOM11",
		"alias": "FiveIsland_LostCave_Room11",
		"key_items": (),
		"file_name": "FiveIsland_LostCave_Room11",
		"low_priority": True,
		"warps": (
			{
				"x": 5,
				"y": 1,
				"elevation": 3,
				"dest_map": "MAP_FIVE_ISLAND_LOST_CAVE_ROOM1",
				"dest_warp_id": 3,
				"pair_id": 272
			},
		),
		"connections": (
		)
	},
	{
		"id": "MAP_FIVE_ISLAND_RESORT_GORGEOUS_HOUSE",
		"alias": "FiveIsland_ResortGorgeous_House",
		"key_items": (),
		"file_name": "FiveIsland_ResortGorgeous_House",
		"low_priority": True,
		"warps": (
			{
				"x": 4,
				"y": 7,
				"elevation": 3,
				"dest_map": "MAP_FIVE_ISLAND_RESORT_GORGEOUS",
				"dest_warp_id": 1,
				"pair_id": 273
			},
		),
		"connections": (
		)
	},
	# {
	# 	"id": "MAP_SIX_ISLAND_WATER_PATH_HOUSE1",
	# 	"alias": "SixIsland_WaterPath_House1",
	# 	"key_items": (),
	# 	"file_name": "SixIsland_WaterPath_House1",
	# 	"low_priority": True,
	# 	"warps": (
	# 		{
	# 			"x": 3,
	# 			"y": 7,
	# 			"elevation": 3,
	# 			"dest_map": "MAP_SIX_ISLAND_WATER_PATH",
	# 			"dest_warp_id": 1,
	# 			"pair_id": 274
	# 		},
	# 	),
	# 	"connections": (
	# 	)
	# },
	# {
	# 	"id": "MAP_SIX_ISLAND_WATER_PATH_HOUSE2",
	# 	"alias": "SixIsland_WaterPath_House2",
	# 	"key_items": (),
	# 	"file_name": "SixIsland_WaterPath_House2",
	# 	"low_priority": True,
	# 	"warps": (
	# 		{
	# 			"x": 4,
	# 			"y": 7,
	# 			"elevation": 3,
	# 			"dest_map": "MAP_SIX_ISLAND_WATER_PATH",
	# 			"dest_warp_id": 1,
	# 			"pair_id": 275
	# 		},
	# 	),
	# 	"connections": (
	# 	)
	# },
	{
		"id": "DUMMY_ROOM",
		"alias": "Dummy Room",
		"key_items": (),
		"file_name": None,
		"skip": True,
		"warps": (
			# {
			# 	"x": 5,
			# 	"y": 13,
			# 	"elevation": 0,
			# 	"dest_map": "MAP_SIX_ISLAND_WATER_PATH_HOUSE1",
			# 	"dest_warp_id": 0,
			# 	"pair_id": 274
			# },
			# {
			# 	"x": 11,
			# 	"y": 19,
			# 	"elevation": 0,
			# 	"dest_map": "MAP_SIX_ISLAND_WATER_PATH_HOUSE2",
			# 	"dest_warp_id": 0,
			# 	"pair_id": 275
			# },
			{
				"x": 2,
				"y": 37,
				"elevation": 3,
				"dest_map": "MAP_POWER_PLANT",
				"dest_warp_id": 3,
				"skip": True,
				"pair_id": 80
			},
			{
				"x": 5,
				"y": 5,
				"elevation": 3,
				"dest_map": "MAP_FIVE_ISLAND_LOST_CAVE_ROOM1",
				"dest_warp_id": 0,
				"pair_id": 202,
				"skip": True
			},
			{
				"x": 5,
				"y": 8,
				"elevation": 3,
				"dest_map": "MAP_FIVE_ISLAND_LOST_CAVE_ROOM1",
				"dest_warp_id": 1,
				"pair_id": 203,
				"skip": True
			},
			{
				"x": 2,
				"y": 5,
				"elevation": 3,
				"dest_map": "MAP_FIVE_ISLAND_LOST_CAVE_ROOM1",
				"dest_warp_id": 2,
				"pair_id": 204,
				"skip": True
			},
			{
				"x": 5,
				"y": 1,
				"elevation": 3,
				"dest_map": "MAP_FIVE_ISLAND_LOST_CAVE_ROOM1",
				"dest_warp_id": 3,
				"pair_id": 205,
				"skip": True
			},
			{
				"x": 8,
				"y": 5,
				"elevation": 3,
				"dest_map": "MAP_FIVE_ISLAND_LOST_CAVE_ROOM1",
				"dest_warp_id": 3,
				"pair_id": 206,
				"skip": True
			},
			{
				"x": 5,
				"y": 8,
				"elevation": 3,
				"dest_map": "MAP_FIVE_ISLAND_LOST_CAVE_ROOM3",
				"dest_warp_id": 0,
				"pair_id": 207,
				"skip": True
			},
			{
				"x": 2,
				"y": 5,
				"elevation": 3,
				"dest_map": "MAP_FIVE_ISLAND_LOST_CAVE_ROOM1",
				"dest_warp_id": 2,
				"pair_id": 208,
				"skip": True
			},
			{
				"x": 5,
				"y": 1,
				"elevation": 3,
				"dest_map": "MAP_FIVE_ISLAND_LOST_CAVE_ROOM1",
				"dest_warp_id": 3,
				"pair_id": 209,
				"skip": True
			},
			{
				"x": 8,
				"y": 5,
				"elevation": 3,
				"dest_map": "MAP_FIVE_ISLAND_LOST_CAVE_ROOM2",
				"dest_warp_id": 3,
				"pair_id": 210,
				"skip": True
			},
			{
				"x": 5,
				"y": 8,
				"elevation": 3,
				"dest_map": "MAP_FIVE_ISLAND_LOST_CAVE_ROOM1",
				"dest_warp_id": 1,
				"pair_id": 211,
				"skip": True
			},
			{
				"x": 2,
				"y": 5,
				"elevation": 3,
				"dest_map": "MAP_FIVE_ISLAND_LOST_CAVE_ROOM1",
				"dest_warp_id": 2,
				"pair_id": 212,
				"skip": True
			},
			{
				"x": 5,
				"y": 1,
				"elevation": 3,
				"dest_map": "MAP_FIVE_ISLAND_LOST_CAVE_ROOM12",
				"dest_warp_id": 0,
				"pair_id": 213,
				"skip": True
			},
			{
				"x": 8,
				"y": 5,
				"elevation": 3,
				"dest_map": "MAP_FIVE_ISLAND_LOST_CAVE_ROOM2",
				"dest_warp_id": 3,
				"pair_id": 214,
				"skip": True
			},
			{
				"x": 5,
				"y": 8,
				"elevation": 3,
				"dest_map": "MAP_FIVE_ISLAND_LOST_CAVE_ROOM1",
				"dest_warp_id": 1,
				"pair_id": 215,
				"skip": True
			},
			{
				"x": 2,
				"y": 5,
				"elevation": 3,
				"dest_map": "MAP_FIVE_ISLAND_LOST_CAVE_ROOM1",
				"dest_warp_id": 2,
				"pair_id": 216,
				"skip": True
			},
			{
				"x": 5,
				"y": 1,
				"elevation": 3,
				"dest_map": "MAP_FIVE_ISLAND_LOST_CAVE_ROOM1",
				"dest_warp_id": 3,
				"pair_id": 217,
				"skip": True
			},
			{
				"x": 8,
				"y": 5,
				"elevation": 3,
				"dest_map": "MAP_FIVE_ISLAND_LOST_CAVE_ROOM2",
				"dest_warp_id": 3,
				"pair_id": 218,
				"skip": True
			},
			{
				"x": 5,
				"y": 8,
				"elevation": 3,
				"dest_map": "MAP_FIVE_ISLAND_LOST_CAVE_ROOM1",
				"dest_warp_id": 1,
				"pair_id": 219,
				"skip": True
			},
			{
				"x": 2,
				"y": 5,
				"elevation": 3,
				"dest_map": "MAP_FIVE_ISLAND_LOST_CAVE_ROOM7",
				"dest_warp_id": 1,
				"pair_id": 220,
				"skip": True
			},
			{
				"x": 5,
				"y": 1,
				"elevation": 3,
				"dest_map": "MAP_FIVE_ISLAND_LOST_CAVE_ROOM1",
				"dest_warp_id": 3,
				"pair_id": 221,
				"skip": True
			},
			{
				"x": 8,
				"y": 5,
				"elevation": 3,
				"dest_map": "MAP_FIVE_ISLAND_LOST_CAVE_ROOM2",
				"dest_warp_id": 3,
				"pair_id": 222,
				"skip": True
			},
			{
				"x": 5,
				"y": 8,
				"elevation": 3,
				"dest_map": "MAP_FIVE_ISLAND_LOST_CAVE_ROOM1",
				"dest_warp_id": 1,
				"pair_id": 223,
				"skip": True
			},
			{
				"x": 2,
				"y": 5,
				"elevation": 3,
				"dest_map": "MAP_FIVE_ISLAND_LOST_CAVE_ROOM1",
				"dest_warp_id": 2,
				"pair_id": 224,
				"skip": True
			},
			{
				"x": 5,
				"y": 1,
				"elevation": 3,
				"dest_map": "MAP_FIVE_ISLAND_LOST_CAVE_ROOM1",
				"dest_warp_id": 3,
				"pair_id": 225,
				"skip": True
			},
			{
				"x": 8,
				"y": 5,
				"elevation": 3,
				"dest_map": "MAP_FIVE_ISLAND_LOST_CAVE_ROOM1",
				"dest_warp_id": 4,
				"pair_id": 226,
				"skip": True
			},

			{
				"x": 5,
				"y": 8,
				"elevation": 3,
				"dest_map": "MAP_FIVE_ISLAND_LOST_CAVE_ROOM1",
				"dest_warp_id": 1,
				"pair_id": 227,
				"skip": True
			},
			{
				"x": 2,
				"y": 5,
				"elevation": 3,
				"dest_map": "MAP_FIVE_ISLAND_LOST_CAVE_ROOM1",
				"dest_warp_id": 2,
				"pair_id": 228,
				"skip": True
			},
			{
				"x": 5,
				"y": 8,
				"elevation": 3,
				"dest_map": "MAP_FIVE_ISLAND_LOST_CAVE_ROOM1",
				"dest_warp_id": 1,
				"pair_id": 229,
				"skip": True
			},
			{
				"x": 8,
				"y": 5,
				"elevation": 3,
				"dest_map": "MAP_FIVE_ISLAND_LOST_CAVE_ROOM2",
				"dest_warp_id": 3,
				"pair_id": 230,
				"skip": True
			},
			{
				"x": 4,
				"y": 4,
				"elevation": 3,
				"dest_map": "MAP_NAVEL_ROCK_FORK",
				"dest_warp_id": 1,
				"pair_id": 239,
				"skip": True
			},
			{
				"x": 2,
				"y": 2,
				"elevation": 3,
				"dest_map": "MAP_NAVEL_ROCK_FORK",
				"dest_warp_id": 2,
				"pair_id": 240,
				"skip": True
			},
			{
				"x": 11,
				"y": 5,
				"elevation": 3,
				"dest_map": "MAP_NAVEL_ROCK_FORK",
				"dest_warp_id": 0,
				"pair_id": 241,
				"skip": True
			},
			{
				"x": 13,
				"y": 9,
				"elevation": 3,
				"dest_map": "MAP_MT_EMBER_RUBY_PATH_B3F",
				"dest_warp_id": 0,
				"pair_id": 242,
				"skip": True
			},
			{
				"x": 4,
				"y": 2,
				"elevation": 3,
				"dest_map": "MAP_MT_EMBER_RUBY_PATH_B3F",
				"dest_warp_id": 2,
				"pair_id": 243,
				"skip": True
			},
			{
				"x": 4,
				"y": 1,
				"elevation": 0,
				"dest_map": "MAP_MT_EMBER_RUBY_PATH_B3F",
				"dest_warp_id": 1,
				"pair_id": 244,
				"skip": True
			},
			{
				"x": 4,
				"y": 7,
				"elevation": 3,
				"dest_map": "MAP_FOUR_ISLAND",
				"dest_warp_id": 1,
				"pair_id": 245,
				"skip": True
			},
			{
				"x": 4,
				"y": 7,
				"elevation": 3,
				"dest_map": "MAP_FOUR_ISLAND",
				"dest_warp_id": 2,
				"pair_id": 246,
				"skip": True
			},
			{
				"x": 17,
				"y": 30,
				"elevation": 3,
				"dest_map": "MAP_FOUR_ISLAND",
				"dest_warp_id": 3,
				"pair_id": 247,
				"skip": True
			},
			{
				"x": 7,
				"y": 8,
				"elevation": 3,
				"dest_map": "MAP_FOUR_ISLAND",
				"dest_warp_id": 0,
				"pair_id": 248,
				"skip": True
			},
			{
				"x": 4,
				"y": 7,
				"elevation": 3,
				"dest_map": "MAP_FOUR_ISLAND",
				"dest_warp_id": 4,
				"pair_id": 249,
				"skip": True
			},
			{
				"x": 4,
				"y": 7,
				"elevation": 3,
				"dest_map": "MAP_FOUR_ISLAND",
				"dest_warp_id": 7,
				"pair_id": 250,
				"skip": True
			},
			{
				"x": 4,
				"y": 7,
				"elevation": 3,
				"dest_map": "MAP_FOUR_ISLAND",
				"dest_warp_id": 5,
				"pair_id": 251,
				"skip": True
			},
			{
				"x": 8,
				"y": 2,
				"elevation": 3,
				"dest_map": "MAP_FOUR_ISLAND",
				"dest_warp_id": 6,
				"pair_id": 252,
				"skip": True
			},
			{
				"x": 33,
				"y": 9,
				"elevation": 0,
				"dest_map": "MAP_TWO_ISLAND_HOUSE",
				"dest_warp_id": 0,
				"pair_id": 253,
				"skip": True
			},
			{
				"x": 25,
				"y": 14,
				"elevation": 0,
				"dest_map": "MAP_FOUR_ISLAND_HOUSE1",
				"dest_warp_id": 0,
				"pair_id": 254,
				"skip": True
			},
			{
				"x": 14,
				"y": 61,
				"elevation": 0,
				"dest_map": "MAP_SEVEN_ISLAND_SEVAULT_CANYON_HOUSE",
				"dest_warp_id": 0,
				"pair_id": 255,
				"skip": True
			},
			{
				"x": 12,
				"y": 16,
				"elevation": 0,
				"dest_map": "MAP_TWO_ISLAND_CAPE_BRINK_HOUSE",
				"dest_warp_id": 0,
				"pair_id": 256,
				"skip": True
			},
			{
				"x": 8,
				"y": 2,
				"elevation": 3,
				"dest_map": "MAP_BIRTH_ISLAND_EXTERIOR",
				"dest_warp_id": 0,
				"pair_id": 257,
				"skip": True
			},
			{
				"x": 4,
				"y": 4,
				"elevation": 3,
				"dest_map": "MAP_NAVEL_ROCK_BASE",
				"dest_warp_id": 0,
				"pair_id": 258,
				"skip": True
			},
			{
				"x": 4,
				"y": 4,
				"elevation": 3,
				"dest_map": "MAP_NAVEL_ROCK_SUMMIT",
				"dest_warp_id": 0,
				"pair_id": 259,
				"skip": True
			},
			{
				"x": 11,
				"y": 6,
				"elevation": 3,
				"dest_map": "MAP_SEVEN_ISLAND_TANOBY_RUINS_VIAPOIS_CHAMBER",
				"dest_warp_id": 0,
				"pair_id": 260,
				"skip": True
			},
			{
				"x": 12,
				"y": 15,
				"elevation": 3,
				"dest_map": "MAP_SEVEN_ISLAND_TANOBY_RUINS_RIXY_CHAMBER",
				"dest_warp_id": 0,
				"pair_id": 261,
				"skip": True
			},
			{
				"x": 32,
				"y": 9,
				"elevation": 3,
				"dest_map": "MAP_SEVEN_ISLAND_TANOBY_RUINS_SCUFIB_CHAMBER",
				"dest_warp_id": 0,
				"pair_id": 262,
				"skip": True
			},
			{
				"x": 44,
				"y": 11,
				"elevation": 3,
				"dest_map": "MAP_SEVEN_ISLAND_TANOBY_RUINS_DILFORD_CHAMBER",
				"dest_warp_id": 0,
				"pair_id": 263,
				"skip": True
			},
			{
				"x": 88,
				"y": 8,
				"elevation": 3,
				"dest_map": "MAP_SEVEN_ISLAND_TANOBY_RUINS_WEEPTH_CHAMBER",
				"dest_warp_id": 0,
				"pair_id": 264,
				"skip": True
			},
			{
				"x": 103,
				"y": 10,
				"elevation": 3,
				"dest_map": "MAP_SEVEN_ISLAND_TANOBY_RUINS_LIPTOO_CHAMBER",
				"dest_warp_id": 0,
				"pair_id": 265,
				"skip": True
			},
			{
				"x": 120,
				"y": 10,
				"elevation": 3,
				"dest_map": "MAP_SEVEN_ISLAND_TANOBY_RUINS_MONEAN_CHAMBER",
				"dest_warp_id": 0,
				"pair_id": 266,
				"skip": True
			},
			{
				"x": 7,
				"y": 17,
				"elevation": 5,
				"dest_map": "MAP_SEVEN_ISLAND_SEVAULT_CANYON_TANOBY_KEY",
				"dest_warp_id": 0,
				"pair_id": 267,
				"skip": True
			},
			{
				"x": 8,
				"y": 5,
				"elevation": 3,
				"dest_map": "MAP_FIVE_ISLAND_LOST_CAVE_ROOM13",
				"dest_warp_id": 0,
				"pair_id": 268,
				"skip": True
			},
			{
				"x": 2,
				"y": 5,
				"elevation": 3,
				"dest_map": "MAP_FIVE_ISLAND_LOST_CAVE_ROOM14",
				"dest_warp_id": 0,
				"pair_id": 269,
				"skip": True
			},
			{
				"x": 7,
				"y": 21,
				"elevation": 3,
				"dest_map": "MAP_SIX_ISLAND_ALTERING_CAVE",
				"dest_warp_id": 0,
				"pair_id": 270,
				"skip": True
			},
			{
				"x": 12,
				"y": 13,
				"elevation": 0,
				"dest_map": "MAP_FOUR_ISLAND_POKEMON_DAY_CARE",
				"dest_warp_id": 0,
				"pair_id": 271,
				"skip": True
			},
			{
				"x": 5,
				"y": 8,
				"elevation": 3,
				"dest_map": "MAP_FIVE_ISLAND_LOST_CAVE_ROOM11",
				"dest_warp_id": 0,
				"pair_id": 272,
				"skip": True
			},
			{
				"x": 39,
				"y": 8,
				"elevation": 0,
				"dest_map": "MAP_FIVE_ISLAND_RESORT_GORGEOUS_HOUSE",
				"dest_warp_id": 0,
				"pair_id": 273,
				"skip": True
			},
		),
		"connections": (
		),
	},
)
