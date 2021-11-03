import queue
import threading
import time
import requests
from bs4 import BeautifulSoup
from queue import Queue

threads = []

urls = ['https://flatfy.ua/%D0%BF%D1%80%D0%BE%D0%B4%D0%B0%D0%B6%D0%B0-%D0%BA%D0%B2%D0%B0%D1%80%D1%82%D0%B8%D1%80-%D0%BA%D0%B8%D0%B5%D0%B2', 'https://dom.ria.com/uk/prodazha-kvartir/kiev/', 'https://dimdim.ua/ru/kyiv/sale/']

start = time.perf_counter()

q = queue.Queue()

def get_title(url):
     responce = requests.get(url=url)
     parser = BeautifulSoup(responce.text, 'html.parser')
     title = parser.find('title').text
     print(title)

for url in urls:
     thread = threading.Thread(target=get_title, args=(url,))
     threads.append(thread)
     thread.start()

for thread in threads:
     thread.join()

finish = time.perf_counter()

print(f'Finished in {finish-start} seconds')