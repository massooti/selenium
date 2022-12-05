from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from helper import save_cookie, load_cookie, save_cookie2
import pickle
from selenium.webdriver.support.ui import WebDriverWait
from src import printcolors as pc
import time
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common import window


def login(driver, i):
    name = 'bot- '
    driver.find_element(
        "id", 'firstName').send_keys(name)
    driver.find_element(
        "id", 'lastName').send_keys(i)
    driver.find_element(
        'xpath', '//*[@id="root"]/section/div/form/button').click()
    # wait = WebDriverWait(driver, timeout=1)
    time.sleep(0.9)
    print(i, 'logiedin')
    driver.find_element(
        'xpath', '/html/body/div[1]/main/div[1]/section[1]')


def selenium(guests, link):
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
    driver.get(link)
    i = 1
    for i in range(guests):
        try:
            if driver.get_cookie('auth-zaeem-e8a2f45f') != None:
                driver.delete_cookie('auth-zaeem-e8a2f45f')
                time.sleep(0.3)
                driver.execute_script(f'window.open("{link}","_blank");')
                driver.switch_to.window(driver.window_handles[i])

            print(i, 'new tab')
            login(driver, i)
            i += 1

        except NoSuchElementException as e:
            print(i)
            driver.delete_cookie('auth-zaeem-e8a2f45f')
            driver.switch_to.window(driver.window_handles[i])
            time.sleep(0.3)
            login(driver, i)


if __name__ == '__main__':
    pc.printout("Hello there\n", pc.YELLOW)
    # link = input('please enter link: ')
    link = "https://test.alocom.co/class/zaeem/e8a2f45f"
    # guests = int(input('please enter guests number: '))
    guests = 15
    selenium(guests, link)
