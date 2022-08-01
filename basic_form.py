from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://demo.anhtester.com/basic-first-form-demo.html")

driver.implicitly_wait(5)

try:
    no_button = driver.find_element(By.CLASS_NAME, "at-cm-no-button")
    no_button.click()
except:
    print('No element with this class name. Skipping ....')

driver.find_element(By.ID, "sum1").send_keys("15")
driver.find_element(By.ID, "sum2").send_keys("20")

get_total_button = driver.find_element(By.CSS_SELECTOR, "button[onclick='return total()']")
# get_total_button = driver.find_element(By.CLASS_NAME, "btn btn-default")
get_total_button.click()

text = driver.find_element(By.ID, "displayvalue").text

print("Result: ", text)