from selenium import webdriver
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent
from tqdm import tqdm
import re


class ParserAvito:
    def __init__(self, url: str, db: object, coordinate: object) -> None:
        self.url = url
        self.db = db
        self.coordinate = coordinate

    def start_webdriver(self, proxy_options: dict[str, dict[str, str]]=None) -> None:
        options = webdriver.FirefoxOptions()
        # options.headless = True
        useragent = UserAgent()
        options.set_preference('general.useragent.override', useragent.random)
        if proxy_options is not None:
            self.driver = webdriver.Firefox(options=proxy_options)
        else:
            self.driver = webdriver.Firefox(options=options)
    
    def get_link(self) -> None:
        self.driver.get(self.url)
            
    def parser_page(self) -> None:
        cards = self.driver.find_elements(By.CSS_SELECTOR, '[data-marker="item"]')

        cards = [card.text.split('\n') for card in cards]
        for card in cards:
            if 'Аукцион:' in card[0]:
                continue
            name = card[0]
            price = int(card[1][:-2].replace(" ", ""))
            pattern_area = r'\b\d+(?:,\d+)?\s*м²\b'
            area = re.findall(pattern_area, card[0])[0]
            if 'Квартира-студия' in card[0]:
                count_room = 1
            else:
                count_room = card[0][0]
            pattern_floor = r'\b\d+/\d+\b'
            floor = re.findall(pattern_floor, card[0])[0]
            for el in card:
                if 'ул.' in el or 'мкр.' in el or 'д.' in el:
                    address = el
                    break
            
            if not self.db.check_ad_in_base(name, price):
                width, longitude = self.coordinate.get_coordinate_address(address)
                self.db.insert_ad(name, price, area, count_room, floor, address, width, longitude, True)
        
    def next_page(self) -> None:
        page_button = self.driver.find_element(By.CSS_SELECTOR, f'[data-marker="pagination-button/nextPage"]')
        page_button.click()
    
    def get_count_page(self) -> int:
        pagination_container = self.driver.find_element(By.CSS_SELECTOR, "nav[aria-label='Пагинация']")
        pagination_buttons = pagination_container.find_elements(By.CSS_SELECTOR, "li.styles-module-listItem-_La42")
        last_page_element = pagination_buttons[-2]
        last_page_number = int(last_page_element.find_element(By.CSS_SELECTOR, "span.styles-module-text-InivV").text)
        return last_page_number

    def start_parser(self) -> None:
        for _ in tqdm(range(0, self.get_count_page() - 1), desc='Скачка и сохранение данных'):
            self.parser_page()
            self.next_page()
    
    def close_browser(self) -> None:
        self.driver.quit()
    




