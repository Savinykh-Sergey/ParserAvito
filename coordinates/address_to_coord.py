from geopy.geocoders import Nominatim 


class CoordinatesFlats:
    def __init__(self) -> None:
        self.geolocator = Nominatim(user_agent="Tester") 

    def get_coordinate_address(self, address: str) -> tuple[float]:
        try:
            # location = self.geolocator.geocode(f'Челябинская область, Челябинск, {address[address.find("ул."):]}')
            location = self.geolocator.geocode(f'Свердловская область, Верхняя Салда, {address[address.find("ул."):]}')  
            return location.latitude, location.longitude
        except:
            return 0, 0
        
    def apply_filter(self, from_price: int, before_price: int, count_rooms: int, floor: int, count_floor: int, db: object):
        apartment_coordinates = []
        for idx in range(db.get_count_rows()):
            if from_price <= int(db.get_price()[idx]) <= before_price:
                if int(db.get_count_rooms()[idx]) == count_rooms:
                    fl = db.get_floors()[idx].split('/')
                    if int(fl[0]) == floor and int(fl[1]) == count_floor:
                        data = {
                            'location': [db.get_width()[idx], db.get_longitude()[idx]],
                            'address': f'{db.get_flat()[idx]}\n{db.get_price()[idx]} ₽\n{db.get_area()[idx]}\nКол-во комнат: {db.get_count_rooms()[idx]}\n{db.get_floors()[idx]} этаж',
                        }  
                        apartment_coordinates.append(data)

        return apartment_coordinates
        
    def create_dict_flats(self, db: object) -> list[dict[str, list], dict[str, str]]:
        apartment_coordinates = []
        for idx in range(db.get_count_rows()):
            data = {
                'location': [db.get_width()[idx], db.get_longitude()[idx]],
                'address': f'{db.get_flat()[idx]}\n{db.get_price()[idx]} ₽\n{db.get_area()[idx]}\nКол-во комнат: {db.get_count_rooms()[idx]}\n{db.get_floors()[idx]} этаж',
            }  
            apartment_coordinates.append(data)
        return apartment_coordinates
    



        



    
        

        