import concurrent.futures
import time
import re

import requests

url = 'https://tw.appledaily.com/new/realtime/{}'

def get_page(url):
    resp = requests.get(url)
    return resp.text

total_pg = 10
cnt = 0
list_page_queue = []
detail_page_queue = []

"""
切換Worker種類非常簡單，把ThreadPoolExecutor換成ProcessPoolExecutor就可以
做切換

ThreadPoolExecutor(max_workers=worker的數量，不寫就是預設值)
"""
#with concurrent.futures.ProcessPoolExecutor(max_workers=1000) as executor:
with concurrent.futures.ThreadPoolExecutor(max_workers=1000) as executor:
    t_start = time.time()
    for page in range(1,total_pg + 1):
        list_page_queue.append(executor.submit(get_page, url.format(page)))

    """
    只要有完成的Futures，就會開始for loop，所以順序可能會不一樣
    試試看這個
    """
    for future in concurrent.futures.as_completed(list_page_queue):
        detail_urls = re.findall('''<a href="(https://tw.news.+?)" target="_blank">''',future.result())
        for detail_url, detail in zip(detail_urls, executor.map(get_page, detail_urls)):
            filename = detail_url.replace('/', '_')
            with open('/tmp/%s.html'%filename, 'w') as f:
                f.write(detail)
        
