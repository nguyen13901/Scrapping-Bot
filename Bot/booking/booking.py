from selenium import webdriver
from selenium.webdriver.common.by import By
from booking.booking_filtration import BookingFiltration
import booking.constants as const
from selenium.webdriver.remote.webelement import WebElement

class Booking(webdriver.Chrome):
    def __init__(self, driver_path="", teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        super(Booking, self).__init__()
        self.implicitly_wait(15)
        self.maximize_window()

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

    def select_adult(self, count):
        toggle = self.find_element(By.ID, "xp__guests__toggle")
        toggle.click()
        decrease_button = self.find_element(
            By.CSS_SELECTOR, 
            "button[aria-label='Decrease number of Adults']"
        )
        increase_button = self.find_element(
            By.CSS_SELECTOR,
            "button[aria-label='Increase number of Adults']"
        )
        group_adults = self.find_element(
            By.ID, "group_adults"
        )
        while True:
            value = group_adults.get_attribute("value")
            if int(value) == 1:
                break
            decrease_button.click()
        
        for _ in range(count-1):
            increase_button.click()


    def search(self):
        search_button = self.find_element(
            By.CLASS_NAME,
            "js-sb-submit-text"    
        )
        search_button.click()

    def apply_filtration(self):
        filtration = BookingFiltration(driver=self)
        filtration.apply_star_ratings(3, 4, 5)

        filtration.sort_price_lowest_first()

    def report_results(self):
        