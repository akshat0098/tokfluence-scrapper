import requests
from bs4 import BeautifulSoup
import pandas as pd
username =[ ]
def top_100_cel():
    response = requests.get(f'https://tokfluence.com/top?limit=100&country=us').text
    soup = BeautifulSoup(response,'lxml-xml')
    s = soup.find('div',class_='Landing_influencer_list_element center').ul
    #Landing_influencer_list_element center
    for x in s:
        url = x.find('div',class_='User_vignette_info_bio').a['href']
        username.append(url)
