from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from helper import save_cookie, load_cookie, save_cookie2
import pickle
from selenium.webdriver.support.ui import WebDriverWait
from src import printcolors as pc


def selenium(guests, link):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(chrome_options=chrome_options)
    for i in range(guests):
        driver.get(link)
        # driver.maximize_window()
        # Find Login button
        # driver.find_element('xpath', "xpath").click()
        driver.maximize_window()
        driver.find_element(
            "id", 'name').send_keys(f'bot-{i}')
        driver.find_element(
            "id", 'lastName').send_keys('me')
        log_in_button = driver.find_element(
            'xpath', '/html/body/div/section/div/form/div[4]/button')
        log_in_button.click()
        # Wait for login process to complete.


if __name__ == '__main__':
    pc.printout("Hello there\n", pc.YELLOW)
    # link = input('please enter link: ')
    link = "https://test.alocom.co/class/you123/a4bbabab"
    # guests = int(input('please enter guests number: '))
    guests = 2
    selenium(guests, link)
