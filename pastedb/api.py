import requests

BASE_URL = "https://pastedb.onrender.com"

def makePaste(title, content, api_key):

    res = requests.post(
        f"{BASE_URL}/api/make-paste",
        headers={
            "x-api-key": api_key
        },
        json={
            "title": title,
            "content": content
        }
    )

    return res.json()
