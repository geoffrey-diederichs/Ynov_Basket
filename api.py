import requests

URL = "https://api.balldontlie.io/v1/"
HEADERS = {
    "Authorization": ""
}

def load_key():
    try:
        with open("key.txt", "r") as f:
            HEADERS["Authorization"] = f.read()
    except:
        print("File key.txt not found.\nPlease save your api key inside a key.txt file.")
        exit()

def get_api(path:str):
    url = URL+path
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        return response.json()['data']
    print("Couldn't get : ", path)
    exit()