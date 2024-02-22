import folium

class Map:
    def __init__(self, apartment_coordinates: list[dict[str, list], dict[str, str]]) -> None:
        self.apartment_coordinates = apartment_coordinates
        self.width = 58.0531#55.1545
        self.longitude = 60.5564 #61.4368

    def build_map_flats(self) -> None:
        city_map = folium.Map(location=[self.width, self.longitude], zoom_start=12)

        for apartment in self.apartment_coordinates:
            folium.Marker(
                location=apartment["location"],
                popup=apartment["address"],
                icon=folium.Icon(color="blue")
            ).add_to(city_map)

        # Сохраняем карту в файл
        city_map.save("city_apartments_map.html")
        



