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
            button_present = EC.presence_of_element_located((By.CLASS_NAME, 'fusion-infinite-scroll-trigger'))
            WebDriverWait(driver, timeout).until(button_present)

            driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            time.sleep(1)

    except TimeoutException:
        print ("Timed out waiting for page to load")
        return
    except:
        print('???')
        return

def load_contents_upto_pagenumb(driver, page_numb, timeout=20):
    try:
        while(True):
            button_present = EC.presence_of_element_located((By.CLASS_NAME, 'fusion-infinite-scroll-trigger'))
            WebDriverWait(driver, timeout).until(button_present)

            driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

            post_cnt = len(driver.find_elements_by_css_selector('h2.entry-title.fusion-post-title > a'))
            if post_cnt > (12*page_numb):
                time.sleep(timeout)
                return

            time.sleep(1)

    except TimeoutException:
        print ("Timed out waiting for page to load")
        return
    except:
        print('???')
        return

def vogue_korea_title_webdriver(page_numb=1):
    driver = webdriver.Chrome('./chromedriver')
    # driver.implicitly_wait(5)

    driver.get("http://www.vogue.co.kr/category/fashion/")
    # load_all_contents(driver)
    load_contents_upto_pagenumb(driver, page_numb)

    title_list = driver.find_elements_by_css_selector('h2.entry-title.fusion-post-title > a')
    title_list = [convert_utf8_to_euckr(tag.text) for tag in title_list]
    title_list = title_list[:(12*page_numb)]

    # print(title_list)
    # print(len(title_list))

    driver.close()

    return title_list


if __name__=='__main__':
    vogue_korea_title_no_webdriver(10)
