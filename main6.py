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
from selenium.common.exceptions import TimeoutException


def login(driver, i):
    try:
        name = 'bot231- '
        # driver.find_element(
        #     "id", 'firstName').send_keys(name)
        WebDriverWait(driver, 1).until(EC.element_to_be_clickable(
            (("id", 'firstName')))).send_keys(name)
        driver.find_element(
            "id", 'lastName').send_keys(i)
        driver.find_element(
            'xpath', '//*[@id="root"]/section/div/form/button').click()
        # driver.delete_cookie('auth-zaeem-e8a2f45f')
        time.sleep(0.9)
        print(f'{i} is ok')

    except NoSuchElementException as e:
        print(e)
        raise Exception(f'{i} is in dashboard')


def loginGenerator(driver, max=0):
    i = 0
    while i < max:
        name = 'bot231- '
        try:
            # driver.find_element(
            #     "id", 'firstName').send_keys(name)
            WebDriverWait(driver, 1).until(EC.element_to_be_clickable(
                (("id", 'firstName')))).send_keys(name)
            driver.find_element(
                "id", 'lastName').send_keys(i)
            driver.find_element(
                'xpath', '//*[@id="root"]/section/div/form/button').click()
            driver.delete_cookie('auth-zaeem-e8a2f45f')
            time.sleep(0.9)
            driver.execute_script(f'window.open("{link}","_blank");')
            driver.switch_to.window(driver.window_handles[i+1])
            yield i
        except TimeoutException as e:
            # driver.find_element(
            #     "id", 'firstName').send_keys(name)
            WebDriverWait(driver, 1).until(EC.element_to_be_clickable(
                (("id", 'firstName')))).send_keys(name)
            driver.find_element(
                "id", 'lastName').send_keys(i)
            driver.find_element(
                'xpath', '//*[@id="root"]/section/div/form/button').click()
            driver.delete_cookie('auth-zaeem-e8a2f45f')
            time.sleep(0.9)
            driver.execute_script(f'window.open("{link}","_blank");')
            driver.switch_to.window(driver.window_handles[i+1])
            yield i


def selenium(guests, link):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_argument(
        '--user-agent="Mozilla/108 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.119')
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
    for i in loginGenerator(driver, guests):
        print(f'{i} is current user')
        driver.delete_cookie('auth-zaeem-e8a2f45f')
        print(f'cache deleted {driver.get_cookie("auth-zaeem-e8a2f45f")}')
        time.sleep(0.9)


if __name__ == '__main__':
    pc.printout("Hello there\n", pc.YELLOW)
    # link = input('please enter link: ')
    link = "https://test.alocom.co/class/zaeem/e8a2f45f"
    # guests = int(input('please enter guests number: '))
    guests = 500
    selenium(guests, link)
