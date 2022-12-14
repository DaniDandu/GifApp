import json
from urllib import parse, request
from api_key import key

def search(name: str):
    url = "http://api.giphy.com/v1/gifs/search"

    params = parse.urlencode({
    "q": name,
    "api_key": str(key),
    "limit": "5"
    })

    with request.urlopen("".join((url, "?", params))) as response:
        data = json.loads(response.read())
    
    list = []

    for key, value in data.items():
        for item in value:
            for k in item:
                if k == "images":
                    list.append(item.get("images").get("original").get("url"))
                    # print(item.get("images").get("original").get("url"))
                    # return item.get("images").get("original").get("url")
    return list
