from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from helper import save_cookie, load_cookie, save_cookie2
import pickle
from selenium.webdriver.support.ui import WebDriverWait
from src import printcolors as pc
import time
# from fake_headers import Headers


def selenium(guests, link):
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_experimental_option("detach", True)
    chrome_options.add_argument(
        '--user-agent="Mozilla/108 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79')
    chrome_options.add_argument('--headless')
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
    for i in range(guests):
        try:
            driver.get(link)
            driver.find_element(
                "id", 'name').send_keys(f'bot{i}-')
            driver.find_element(
                "id", 'lastName').send_keys(f'{i}')
            log_in_button = driver.find_element(
                'xpath', '/html/body/div/section/div/form/div[4]/button')
            log_in_button.click()
            time.sleep(0.9)
            isLoginedIn = driver.find_element(
                'xpath', '/html/body/div[1]/main/div[1]/section[2]/div/span/span/button/span[1]/i')

            if isLoginedIn:
                print(i)

        except Exception as e:
            print(e)
            exit()

    # driver.manage().timeouts().implicitlyWait(5, TimeUnit.SECONDS)


if __name__ == '__main__':
    pc.printout("Hello there\n", pc.YELLOW)
    # link = input('please enter link: ')
    link = "https://test.alocom.co/class/you123/a4bbabab"
    # guests = int(input('please enter guests number: '))
    guests = 15
    selenium(guests, link)
