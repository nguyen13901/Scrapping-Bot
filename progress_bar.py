from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get("https://jqueryui.com/resources/demos/progressbar/download.html")

download_button = driver.find_element(By.ID, "downloadButton")
download_button.click()

progress_label = driver.find_element(By.CLASS_NAME, "progress-label")

wait = WebDriverWait(driver, 10)
wait.until(EC.text_to_be_present_in_element(
    (By.CLASS_NAME, "progress-label"),
    "Complete!"
))
print(progress_label.text)