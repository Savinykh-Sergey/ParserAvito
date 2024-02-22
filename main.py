from Proxy.ProxyManager import ProxyManager
from Proxy.proxy import list_proxy
from db.DBHelper import DBHelper
from ParserAvito.parser_avito import ParserAvito
from Proxy.config import login, password
from coordinates.address_to_coord import CoordinatesFlats
from MapFlats.build_map import Map


# url = 'https://www.avito.ru/chelyabinsk/kvartiry/prodam-ASgBAgICAUSSA8YQ?cd=1&q=%D1%87%D0%B5%D0%BB%D1%8F%D0%B1%D0%B8%D0%BD%D1%81%D0%BA%D0%B8%D0%B9'
url = 'https://www.avito.ru/verhnyaya_salda/kvartiry/prodam-ASgBAgICAUSSA8YQ?cd=1'

db = DBHelper('parser_data.db')
coordinates_flats = CoordinatesFlats()
proxy_manager = ProxyManager(list_proxy, login, password)
parser = ParserAvito(url, db, coordinates_flats)

parser.start_webdriver()
parser.get_link()
parser.start_parser()
parser.close_browser()



