import requests
url = "http://xn--289aqcqql4x71pv5igxah49e.com/"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"}
res = requests.get(url, headers = headers)
res.raise_for_status()
with open("nado.html","w", encoding="utf8") as f:
    f.write(res.text)