import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/67.0.3396.87 Safari/537.36"
}

url = "https://live.bilibili.com/21834279"

response = requests.get(url, headers=headers).text

print(response)
