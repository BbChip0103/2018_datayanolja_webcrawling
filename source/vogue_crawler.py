# -*- coding: utf-8 -*-

import sys
from bs4 import BeautifulSoup
import requests
import time
import re

def get_page(url):
    headers = {'Content-Type': 'application/json; charset=utf-8',
                'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'lxml', from_encoding='utf-8')
    r.close()
    return soup

def get_post_list(soup):
    return soup.select('h2.entry-title.fusion-post-title > a')

def utf8_to_euckr(unicode_string):
    p = re.compile('\xc2|\xa0')
    text = p.sub('', unicode_string)
    text = text.encode('euc-kr', 'replace').decode('euc-kr')
    return text

def vogue_korea_title_no_webdriver(page_numb):
    base_url = 'http://www.vogue.co.kr/category/fashion/page/{}/?noCache'

    title_list = []
    for page_numb in range(1, page_numb+1):
        target_url = base_url.format(page_numb)
        soup = get_page(target_url)
        post_list = get_post_list(soup)

        title_list += [utf8_to_euckr(post.get_text(strip=True))
                        for post in post_list]

    # print(title_list)
    # print(len(title_list))

    return title_list

if __name__ == '__main__':
    page_numb = 10
    vogue_korea_title_no_webdriver(page_numb)
