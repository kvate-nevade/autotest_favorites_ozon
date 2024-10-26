from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = webdriver.ChromeOptions()
options.add_extension('ublock.crx')
driver = webdriver.Chrome(service = Service('chromedriver.exe'), options=options)
driver.implicitly_wait(5)

link = 'https://www.ozon.ru/'

try:
    driver.get(url=link)
    driver.maximize_window()

    # Click on button reload if its needed for ozon
    try:
        driver.find_element(By.ID, 'reload-button').click()
    except:
        pass

    field_of_search = driver.find_element(By.CSS_SELECTOR, '.ai3a_33.tsBody500Medium') # Click on search field on ozon
    field_of_search.click()
    field_of_search.send_keys('Кроссовки reebok') # Writing text on search field on ozon
    field_of_search.send_keys(Keys.ENTER)
    WebDriverWait(driver, 8).until(EC.visibility_of_any_elements_located((By.CSS_SELECTOR, 'button.fd9_9.b2117-a0.b2117-b5.b2117-a4'))) # Waits to cookie popup
    buttons_of_like = driver.find_elements(By.CSS_SELECTOR, 'button.jn3_23') # Find all likes buttons on result page ozon
    #print(len(buttons_of_like))

    counter = 1
    for like in buttons_of_like:
        like.click()
        print(f'Its {counter} buttons of like while i click ')
        counter += 1

    driver.find_element(By.CSS_SELECTOR, 'span.d4p_16_9').click() # Click on the button favorites
    action_likes = WebDriverWait(driver, 5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'button.jn3_23 [fill="#F8104B"]'))) # Find all likes goods in favorites
    assert len(action_likes) == len(buttons_of_like), 'Failed. The number of products in favorites is less than necessary'
    print(f'Autotest completed {len(buttons_of_like)} = {len(action_likes)}')

except Exception as ex:
    print(ex)
    pass

finally:
    #time.sleep(15)
    driver.close()
    driver.quit()