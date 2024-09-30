from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
import time

options = webdriver.ChromeOptions()
options.add_extension('ublock.crx')
driver = webdriver.Chrome(service = Service('chromedriver.exe'), options=options)

link = 'https://www.ozon.ru/'

try:
    driver.get(url=link)
    driver.maximize_window()
    time.sleep(3)

    # Click on button reload if its needed for ozon
    try:
        driver.find_element(By.CSS_SELECTOR, '#reload-button').click()
    except:
        pass

    field_of_search = driver.find_element(By.CSS_SELECTOR, '[placeholder="Искать на Ozon"]') # Click on search field on ozon
    field_of_search.click()
    time.sleep(1)
    field_of_search.send_keys('Кроссовки reebok') # Writing text on search field on ozon
    field_of_search.send_keys(Keys.ENTER)
    time.sleep(3)
    buttons_of_like = driver.find_elements(By.CSS_SELECTOR, '.jm3_23') # Find all likes buttons on result page ozon
    print(len(buttons_of_like))

    counter = 1
    for e in buttons_of_like:
        e.click()
        print(f'Its {counter} buttons of like while i click ')
        counter += 1
        time.sleep(2)

    driver.find_element(By.CSS_SELECTOR, '.dp3_16_9').click() # Click on the button favorites
    time.sleep(2)
    action_likes = driver.find_elements(By.CSS_SELECTOR, '[class="jm3_23"] [fill="#F8104B"]') # Find all likes goods in favorites
    time.sleep(1)
    assert len(action_likes) == 60, 'Ошибка, количество товаров в избранном меньше, чем 60'
    print('Congratulation i all do it')

except Exception as ex:
    print(ex)
    pass

finally:
    time.sleep(15)
    driver.close()
    driver.quit()