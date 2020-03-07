"""
Data utilities
"""

###########
# Imports #
###########
from bs4 import BeautifulSoup
import requests

def get_user_data(username):
    url = f"https://github.com/{username}"
    request = requests.get(url)
    if request.status_code != 200:
        raise ValueError(f"Invalid user name: {username}")
    data = request.text
    return data

def get_fill_values(data):
    soup = BeautifulSoup(data, features="lxml")
    days = soup.find_all("rect")
    fill_values = [d["fill"] for d in days]
    return fill_values
