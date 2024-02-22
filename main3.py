from application.app import main
from db.DBHelper import DBHelper
from coordinates.address_to_coord import CoordinatesFlats
from MapFlats.build_map import Map


db = DBHelper('parser_data.db')
coordinates_flats = CoordinatesFlats()
data = main()

with open('data.txt', 'r') as file:
    data = list(map(int, file.readline().split()))

apartment_coordinates = coordinates_flats.apply_filter(data[0], data[1], data[2], data[3], data[4], db)
    
map_flats = Map(apartment_coordinates)
map_flats.build_map_flats()

# map_flats.build_map_flats()

