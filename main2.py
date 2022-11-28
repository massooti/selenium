from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from helper import save_cookie, load_cookie, save_cookie2
import pickle
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains


from src import printcolors as pc
import time


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument(
    '--user-agent="Mozilla/108 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79')
# chrome_options.add_argument('--headless')
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--proxy-server='direct://'")
chrome_options.add_argument("--proxy-bypass-list=*")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(options=chrome_options)
i = 1


link = "https://test.alocom.co/class/zaeem/e8a2f45f"
driver.get(link)

driver.find_element('xpath', '/html/body').send_keys(Keys.CONTROL + 't')

print(11111)
exit()


def login(driver):
    driver.get(link)
    driver.find_element(
        "id", 'name').send_keys(f'bot{i}-')
    driver.find_element(
        "id", 'lastName').send_keys(f'{i}')
    log_in_button = driver.find_element(
        'xpath', '/html/body/div/section/div/form/div[4]/button')
    log_in_button.click()


while True:
    try:
        login(driver)
        time.sleep(0.9)
        driver.find_element(
            'xpath', '/html/body/div[1]/main/div[1]/section[2]/div/span/span/button/span[1]/i')
        driver.delete_cookie('auth-zaeem-e8a2f45f')

    except NoSuchElementException:
        login(driver)
    except Exception as e:
        driver.delete_cookie('auth-zaeem-e8a2f45f')
        break
