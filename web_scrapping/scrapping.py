import requests
from bs4 import BeautifulSoup
from secrets import username, password

payload = {
            'email': username,
            'pass': password
        }

POST_LOGIN_URL = "www.facebook.com/login"

with requests.Session() as session:
    post = session.post(POST_LOGIN_URL, data=payload)
    page = requests.get("https://mbasic.facebook.com/ufi/reaction/profile/browser/fetch/?limit=100&total_count=18&ft_ent_identifier=908976296236140")
s