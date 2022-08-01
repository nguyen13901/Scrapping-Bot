from selenium import webdriver
from selenium.webdriver.common.by import By
import booking.constants as const

class Booking(webdriver.Chrome):
    def __init__(self, driver_path="", teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        super(Booking, self).__init__()
        self.implicitly_wait(15)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)

    def change_currency(self, currency=None):
        currency_element = self.find_element(
            By.CSS_SELECTOR, 
            "button[data-tooltip-text='Choose your currency']"
        )
        currency_element.click()
        selected_currency_element = self.find_element(
            By.CSS_SELECTOR,
            f"a[data-modal-header-async-url-param*='selected_currency={currency}']"
        )
        selected_currency_element.click()

    def select_place_to_go(self, address):
        search_box = self.find_element(By.ID, "ss")
        search_box.clear()
        search_box.send_keys(f"{address}")
        first_search = self.find_element(
            By.CSS_SELECTOR,
            "li[data-i='0']"    
        )
        first_search.click()

    def select_dates(self, check_in_date, check_out_date):
        check_in_date = self.find_element(
            By.CSS_SELECTOR,
            f"td[data-date='{check_in_date}']"
        )
        check_in_date.click()
        check_out_date = self.find_element(
            By.CSS_SELECTOR,
            f"td[data-date='{check_out_date}']"
        )
        check_out_date.click()

    def search(self):
        search_button = self.find_element(
            By.CLASS_NAME,
            "js-sb-submit-text"    
        )
        search_button.click()