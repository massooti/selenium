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
from urllib import parse
import os
from dotenv import load_dotenv
load_dotenv()


def login(driver, i, cookie):
    try:
        name = os.getenv('ROBOT_NAME')
        # driver.find_element(
        #     "id", 'firstName').send_keys(name)
        WebDriverWait(driver, 1).until(EC.element_to_be_clickable(
            (("id", 'firstName')))).send_keys(name + '-')
        driver.find_element(
            "id", 'lastName').send_keys(i)
        driver.find_element(
            'xpath', '//*[@id="root"]/section/div/form/button').click()
        time.sleep(0.9)
        pc.printout(f"{i} is ok\n", pc.GREEN)
        driver.delete_cookie(cookie)

    except NoSuchElementException as e:
        raise Exception(f'{i} is in dashboard')


def close():
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=chrome_options)
    driver.close()


def selenium(guests, link):
    path = link.rsplit('/class', 1)[-1]
    cookie = 'auth' + path.replace('/', '-')

    def open_new_tab(link, i):
        driver.delete_cookie(cookie)
        driver.execute_script(f'window.open("{link}","_blank");')
        driver.switch_to.window(driver.window_handles[i+1])

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_experimental_option(
        "excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    chrome_options.add_experimental_option('prefs', {
        "profile.default_content_setting_values.notifications": 1,
        "profile.default_content_setting_values.media_stream_mic": 1,
        "profile.default_content_setting_values.media_stream_camera": 1,
    })

    chrome_options.add_argument(
        '--user-agent="Mozilla/108 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--proxy-server='direct://'")
    chrome_options.add_argument("--proxy-bypass-list=*")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Chrome(options=chrome_options,
                              executable_path='chromedriver')
    print(link, guests)
    driver.get(link)
    for i in range(guests):
        pc.printout(f"{i} is current user\n", pc.CYAN)
        try:
            if driver.get_cookie(cookie) != None:
                open_new_tab(link, i)
            if (driver.find_element(
                    'xpath', '/html/body/div[1]/main/div[1]/section[1]').is_displayed()):
                pc.printout(f"{i} logged in\n", pc.BLACK)

                i += 1
        except NoSuchElementException as e:
            pc.printout(f"{i} is in login page\n", pc.BLUE)
            # driver.close()
            login(driver, i, cookie)
            open_new_tab(link, i)
        except Exception as exception:
            pc.printout(f"{i} is in DASHBOARD\n", pc.RED)
            # print(i, 'is in DASHBOARD')


if __name__ == '__main__':
    # link = "https://test.alocom.co/class/zaeem/e8a2f45f"
    link = str(os.getenv('LINK_CLASS'))
    guests = int(os.getenv('GUESTS'))
    selenium(guests, link)
