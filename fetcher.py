import urllib.request, json

urlLink = ""
with urllib.request.urlopen() as url:
    data = json.load(url)
    print(data)