# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time

def convert_utf8_to_euckr(unicode_string):
    return unicode_string.encode('euc-kr', 'replace').decode('euc-kr')

def load_all_contents(driver, timeout=20):
    try:
        while(True):
            button_present = EC.presence_of_element_located((By.CLASS_NAME, 'feed-load-more-button'))
            WebDriverWait(driver, timeout).until(button_present)

            driver.find_element_by_class_name('feed-load-more-button').click()
            time.sleep(1)

    except TimeoutException:
        # print ("Timed out waiting for page to load")
        return
    except:
        # print('???')
        return


def google_trend_title_webdriver():
    driver = webdriver.Chrome('./chromedriver')
    # driver.implicitly_wait(5)

    driver.get("https://trends.google.com/trends/trendingsearches/realtime?geo=US&category=all")
    load_all_contents(driver)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    title_list = driver.find_elements_by_class_name('details-top')
    title_list = [convert_utf8_to_euckr(tag.text) for tag in title_list]

    # print(title_list)
    # print(len(title_list))

    driver.close()

    return title_list


if __name__=='__main__':
    google_trend_title_webdriver()
