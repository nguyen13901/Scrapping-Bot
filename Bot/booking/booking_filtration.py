# This file will include a class with instance methods
# That will be responsible to interact with our websites
# After we have some results, to apply filtrations
from nis import cat
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class BookingFiltration:
    def __init__(self, driver=WebDriver):
        self.driver = driver
    
    def apply_star_ratings(self, *star_values):

        star_filtration_boxs = self.driver.find_elements(
            By.CSS_SELECTOR,
            "div[data-filters-group='class'] div[data-filters-item*='class:class=']"
        ) 

        try: 
            self.driver.find_element(By.ID, "onetrust-accept-btn-handler").click()
        except Exception:
            pass
        
        for star in star_values:
            star_filtration_boxs[star-1].click()

    def sort_price_lowest_first(self):
        self.driver.implicitly_wait(0)
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.invisibility_of_element_located((
            By.CSS_SELECTOR, 
            "div[data-testid='overlay-spinner']"
        )))
        self.driver.implicitly_wait(15)
        
        sorters_dropdown = self.driver.find_element(
            By.CSS_SELECTOR,
            "button[data-testid='sorters-dropdown-trigger']"
        )

        sorters_dropdown.click()

        price = self.driver.find_element(
            By.CSS_SELECTOR,
            "button[data-id='price']"
        )
        price.click()

