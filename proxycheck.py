import threading
import queue
import requests

q = queue.Queue()

valid = []

with open("C:\GitHub\Land-value-GIS\proxylist.txt", "r") as file:
    proxies = file.read().split("\n")
    for p in proxies:
        q.put(p)


def check_proxies():
    global q
    while not q.empty():
        proxy = q.get()
        try:
            res = requests.get(
                "http://ipinfo.io/json", proxies={"https": proxy, "https": proxy}
            )

        except:
            continue
        if res.status_code == 200:
            print(proxy)


for _ in range(10):
    threading.Thread(target=check_proxies).start()
