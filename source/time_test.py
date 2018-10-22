import time
from google_trend_realtime_webdriver import google_trend_title_webdriver
from google_trend_realtime import google_trend_title_no_webdriver
from vogue_crawler_webdriver import vogue_korea_title_webdriver
from vogue_crawler import vogue_korea_title_no_webdriver
from functools import partial

def check_time(func):
    start_time = time.time()
    result = func()
    e = int(time.time() - start_time)
    print(result[:5])
    # print(len(result))
    print('{:02d}:{:02d}:{:02d}'.format(e//3600, (e%3600 // 60), e%60))
    return e

def google_trend_time_test(test_cnt=1):
    print('--google_trend_title_webdriver--')
    total_time = 0
    for i in range(test_cnt):
        total_time += check_time(google_trend_title_webdriver)
    average_sec = int(total_time / test_cnt)
    average_time = '{:02d}:{:02d}:{:02d}'.format(average_sec//3600,
                                                 average_sec%3600 // 60,
                                                 average_sec%60)
    print('average_time:', average_time, ',', average_sec, '[sec]')
    print()

    print('--google_trend_title_no_webdriver--')
    total_time = 0
    for i in range(test_cnt):
        total_time += check_time(google_trend_title_no_webdriver)
    average_sec = int(total_time / test_cnt)
    average_time = '{:02d}:{:02d}:{:02d}'.format(average_sec//3600,
                                                 average_sec%3600 // 60,
                                                 average_sec%60)
    print('average_time:', average_time, ',', average_sec, '[sec]')
    print()

def vogue_korea_time_test(test_cnt=1, page_numb=1):
    vogue_webd = partial(vogue_korea_title_webdriver, page_numb=page_numb)
    vogue_no_webd = partial(vogue_korea_title_no_webdriver, page_numb=page_numb)

    print('--vogue_korea_title_webdriver--')
    total_time = 0
    for i in range(test_cnt):
        total_time += check_time(vogue_webd)
    average_sec = int(total_time / test_cnt)
    average_time = '{:02d}:{:02d}:{:02d}'.format(average_sec//3600,
                                                 average_sec%3600 // 60,
                                                 average_sec%60)
    print('average_time:', average_time, ',', average_sec, '[sec]')
    print()

    print('--vogue_korea_title_no_webdriver--')
    total_time = 0
    for i in range(test_cnt):
        total_time += check_time(vogue_no_webd)
    average_sec = int(total_time / test_cnt)
    average_time = '{:02d}:{:02d}:{:02d}'.format(average_sec//3600,
                                                 average_sec%3600 // 60,
                                                 average_sec%60)
    print('average_time:', average_time, ',', average_sec, '[sec]')
    print()


if __name__ == '__main__':
    google_trend_time_test(3)
    vogue_korea_time_test(3, 10)
