from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")  # Teljes képernyős mód
driver = webdriver.Chrome(options=options)
driver.get("https://www.techlistic.com/p/selenium-practice-form.html")

# Cookie elfogadása (várjuk meg, hogy látható legyen)
try:
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'ez-accept-all'))
    ).click()
except:
    print("Nem található cookie gomb, vagy már eltűnt")

# Kitöltjük az űrlapot
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//input[@name="firstname"]'))
).send_keys('hello')

WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//input[@name="lastname"]'))
).send_keys('xd')

# A reklám miatt JavaScript kattintást használunk
a1 = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'sex-0'))
)
driver.execute_script("arguments[0].click();", a1)

a2 = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'exp-3'))
)
driver.execute_script("arguments[0].click();", a2)

# Professzionális checkboxok
a3 = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'profession-0'))
)
driver.execute_script("arguments[0].click();", a3)

a4 = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'profession-1'))
)
driver.execute_script("arguments[0].click();", a4)

# Lenyíló menü kezelése
dropdown = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "continents"))
)
select = Select(dropdown)
select.select_by_visible_text("South America")

# Várakozás és kilépés
time.sleep(2)
driver.save_screenshot("final_screenshot.png")
driver.quit()