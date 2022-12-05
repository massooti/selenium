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
# from fake_headers import Headers


def check_exists_by_xpath(driver) -> bool:
    try:
        print(11111111111111111)
        # wait = driver.setScriptTimeout(0.3)
        # driver = webdriver(driver, 0.3)
        # t = driver.find_element(
        #     'xpath', '/html/body/div[1]/main/div[1]/section[1]')
        # y = wait.until(
        #     EC.presence_of_element_located(('xpath', '/html/body/div[1]/main/div[1]/section[1]')))
        t = WebDriverWait(driver, 0.5).until(EC.element_to_be_clickable(
            (('xpath', '/html/body/div[1]/main/div[1]/section[1]'))))
        print(t)
        return True
    except NoSuchElementException:
        print(2222222222222222222222)
        return False


def selenium(guests, link):
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_experimental_option("detach", True)
    chrome_options.add_argument(
        '--user-agent="Mozilla/108 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79')
    # chrome_options.add_argument('--headless')
    chrome_options.add_experimental_option("detach", True)
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
    while True:
        i = 1
        try:
            name = 'bot- '
            driver.get(link)
            driver.find_element(
                "id", 'name').send_keys(name)
            driver.find_element(
                "id", 'lastName').send_keys(i)
            driver.find_element(
                'xpath', '/html/body/div/section/div/form/div[4]/button').click()
            # wait = WebDriverWait(driver, timeout=1)
            time.sleep(1)
            exit()
            driver.find_element(
                'xpath', '/html/body/div[1]/main/div[1]/section[1]')
            time.sleep(1)
            print(driver.get_cookie('auth-zaeem-e8a2f45f'))
            driver.delete_cookie('auth-zaeem-e8a2f45f')
            # driver.execute_script(f'window.open("{link}");')

        except NoSuchElementException as e:
            driver.execute_script(f'window.open("{link}", );')
            driver = webdriver.Chrome(options=chrome_options)
            print(i)


if __name__ == '__main__':
    pc.printout("Hello there\n", pc.YELLOW)
    # link = input('please enter link: ')
    link = "https://test.alocom.co/class/zaeem/e8a2f45f"
    # guests = int(input('please enter guests number: '))
    guests = 15
    selenium(guests, link)
