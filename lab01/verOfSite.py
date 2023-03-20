import requests
import json

# przykładowa strona internetowa i trzy daty
pageurl = "https://pl.wikipedia.org/wiki/Python"
dates = ["20210101", "20190101", "20180101"]

# zapytanie do API Wayback Machine dla każdej daty i pobranie URL archiwum
archived_urls = []
for date in dates:
    url = "http://archive.org/wayback/available?url=" + pageurl + "&timestamp=" + date
    response = requests.get(url)
    d = json.loads(response.text)
    if "archived_snapshots" in d and d["archived_snapshots"]:
        archived_urls.append(d["archived_snapshots"]["closest"]["url"])

# otwarcie każdej archiwalnej strony w przeglądarce
import webbrowser
for url in archived_urls:
    webbrowser.open(url)

# wysłanie zmian na Github
import os
os.system("git add .")
os.system("git commit -m stronyArchwialne")
os.system("git push")
