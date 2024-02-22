from sqlalchemy import create_engine, Column, Integer, String, Boolean, Float
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class DBHelper:
    def __init__(self, data_base_name: str) -> None:
        self.__engine = create_engine(f'sqlite:///db/{data_base_name}')
        self.__Session = sessionmaker(bind=self.__engine)
        self.__session = self.__Session()
        Base.metadata.create_all(self.__engine)

    def insert_ad(self, name: str, price: int, area: int, count_room: int, floor: str, address: str, width: float, longitude: float, flag: bool) -> None:
        ad = Ad(name=name, price=price, area=area, count_room=count_room, floor=floor, address=address, width=width, longitude=longitude, downloaded=flag)
        self.__session.add(ad)
        self.__session.commit()
    
    def check_ad_in_base(self, name: str, price: int) -> bool:
        existing_ad = self.__session.query(Ad).filter(Ad.name == name, Ad.price == price).first()
        return existing_ad
    
    def get_count_rows(self) -> int:
        total_records = self.__session.query(Ad).count()
        return total_records
    
    def get_width(self) -> list:
        width = self.__session.query(Ad.width).all()
        return [wid[0] for wid in width]
    
    def get_longitude(self) -> list:
        longitude = self.__session.query(Ad.longitude).all()
        return [long[0] for long in longitude]
    
    def get_flat(self) -> list:
        flats = self.__session.query(Ad.name).all()
        return [flat[0] for flat in flats]
    
    def get_price(self) -> list:
        prices = self.__session.query(Ad.price).all()
        return [price[0] for price in prices]
    
    def get_area(self) -> list:
        area = self.__session.query(Ad.area).all()
        return [ar[0] for ar in area]
    
    def get_count_rooms(self) -> list:
        count_rooms = self.__session.query(Ad.count_room).all()
        return [count_room[0] for count_room in count_rooms]
    
    def get_floors(self) -> list:
        floors = self.__session.query(Ad.floor).all()
        return [floor[0] for floor in floors]
    
    def delete_invalid_data(self):
        pass 
    
    

class Ad(Base):
    __tablename__ = 'ad'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)
    area = Column(String)
    count_room = Column(Integer)
    floor = Column(String)
    address = Column(String)
    width = Column(Float) 
    longitude = Column(Float)
    downloaded = Column(Boolean, default=False)
   

