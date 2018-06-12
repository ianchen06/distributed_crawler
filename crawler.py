from celery import Celery
import requests

app = Celery('crawler', broker='amqp://guest:guest@localhost/')

@app.task
def get_page(url):
    resp = requests.get(url)
    return resp.text
