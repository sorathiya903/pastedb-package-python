import requests

BASE_URL = "https://pastedb.onrender.com"


def create_paste_request(
    api_key,
    data
):

    response = requests.post(

        f"{BASE_URL}/api/create",

        headers={
            "x-api-key": api_key
        },

        json=data
    )

    return response.json()

def knowMe(api_key):
    res = requests.get("https://pastedb.onrender.com/api/me",
                        headers={"x-api-key":api_key}
                       
                       )
    return res.json()
