import crawler

url = 'http://api.ipify.org'

for i in range(1000):
    print(crawler.get_page.delay(url))
