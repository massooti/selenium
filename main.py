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
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(chrome_options=chrome_options)
    # for _ in range(guests):
    driver.get(link)
    driver.find_element(
        "id", 'name').send_keys('ali')
    driver.find_element(
        "id", 'lastName').send_keys('xx1X2bc@#')
    log_in_button = driver.find_element(
        'xpath', '/html/body/div/section/div/form/div[4]/button')
    log_in_button.click()


if __name__ == '__main__':
    pc.printout("Hello there\n", pc.YELLOW)
    # link = input('please enter link: ')
    link = "https://test.alocom.co/class/you123/a4bbabab"
    # guests = int(input('please enter guests number: '))
    guests = 1
    selenium(guests, link)
