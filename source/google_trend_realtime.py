# -*- coding: utf-8 -*-

import requests
import json

import time

def res_to_dict(text):
    # 첫줄이')]}\',와 같은 의미없는 문자가 들어있어서 제외
    # text = text.split('\n')[1]
    # text = convert_utf8_to_euckr(text)
    text = text[5:]
    trend_dic = json.loads(text)
    return trend_dic

def utf8_to_euckr(unicode_string):
    return unicode_string.encode('euc-kr', 'replace').decode('euc-kr')

def get_keyword_id_list(hl='ko',geo='US',category='all'):
    url = 'https://trends.google.co.kr/trends/api/realtimetrends'
    query = {'hl':hl, 'geo':geo, 'cat':category, 'sort':'0',
             'tz':'-540', 'fi':'0', 'fs':'0', 'ri':'300', 'rs':'20'}
    response = requests.get(url, params=query)
    keyword_dict = res_to_dict(response.text)
    keyword_list = keyword_dict['trendingStoryIds']
    return keyword_list

def get_realtime_keyword_data(keyword):
    url = "https://trends.google.co.kr/trends/api/stories"+'/'+keyword
    query = {'hl':'ko', 'tz':'-540'}
    response = requests.get(url, params=query)
    keyword_dict = res_to_dict(response.text)
    return keyword_dict

def get_reltime_keword_summary(keyword_list):
    url = 'https://trends.google.co.kr/trends/api/stories/summary?id='
    url = url + '&id='.join(keyword_list)
    query = {'hl':'ko', 'tz':'-540', 'cat':'all'}
    response = requests.get(url, params=query)
    summary_dict = res_to_dict(response.text)
    return summary_dict

def google_trend_title_no_webdriver():
    id_list = get_keyword_id_list()

    chunk_size = 40 # max chunk size is 40
    id_list_chunked = [id_list[i:i+chunk_size]
                            for i in range(0, len(id_list), chunk_size)]

    # 이 부분 분산처리 가능
    title_list = []
    for chunk in id_list_chunked:
        summary_dict = get_reltime_keword_summary(chunk)
        keyword_list = summary_dict['trendingStories']
        title_list += [utf8_to_euckr(data['title']) for data in keyword_list]

    # print(title_list)
    # print(len(title_list))

    return title_list


if __name__ == '__main__':
    google_trend_title_no_webdriver()
