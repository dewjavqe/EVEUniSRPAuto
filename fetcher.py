import urllib.request, json

urlLink = "https://esi.evetech.net/v1/killmails/120569227/bef1a45562d05559443646a53e35f3f6a507027d/?datasource=tranquility"
with urllib.request.urlopen(urlLink) as url:
    data = json.load(url)
    print(data)