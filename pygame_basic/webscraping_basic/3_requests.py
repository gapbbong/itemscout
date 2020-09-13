import requests
res = requests.get("http://google.com")
with open ("mygoogle.html","w", encoding="utf8") as f:
    f.write(res.text)