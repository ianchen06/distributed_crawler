import concurrent.futures
import time

import requests

url = 'http://api.ipify.org'

def get_page(url):
    resp = requests.get(url)
    return resp.text

cnt = 0
fus = []

"""
切換Worker種類非常簡單，把ThreadPoolExecutor換成ProcessPoolExecutor就可以
做切換

ThreadPoolExecutor(max_workers=worker的數量，不寫就是預設值)
"""
#with concurrent.futures.ProcessPoolExecutor(max_workers=1000) as executor:
with concurrent.futures.ThreadPoolExecutor(max_workers=1000) as executor:
    t_start = time.time()
    for i in range(0, 1000):
        fus.append(executor.submit(get_page, url))

    # 等全部的Futures都完成
    concurrent.futures.wait(fus)
    print([f.result() for f in fus])
    t_end = time.time()
    print(t_end - t_start)
    
    """
    只要有完成的Futures，就會開始for loop，所以順序可能會不一樣
    試試看這個
    """
    #for future in concurrent.futures.as_completed(fu):
    #    print(future.result())
    
