from db.DBHelper import DBHelper
from coordinates.address_to_coord import CoordinatesFlats
from MapFlats.build_map import Map


db = DBHelper('parser_data.db')
coordinates_flats = CoordinatesFlats()
map_flats = Map(coordinates_flats.create_dict_flats(db))

map_flats.build_map_flats()