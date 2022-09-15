"""
it's module need's for parsing on site https://enter.kg
"""
from cgitb import text
from unittest import result
from urllib import response
import requests
from bs4 import BeautifulSoup

from .utils import deep_requests

class Response():

    URL = "https://enter.kg"

    def __init__(self, category: str) -> None:
        self.category = category

    def get_response(self) -> str:
        url = "{}/{}".format(Response.URL, self.category)
        response = requests.get(url=url).text
        return response


class Parsing():

    def __init__(self, response: Response) -> None:
        self.response = response

    def soup(self) -> BeautifulSoup:
        response = self.response.get_response()
        soup = BeautifulSoup(response, "lxml")
        return soup

    def find_all(self, soup: BeautifulSoup):
        all_data = soup.find_all("div", class_="row")
        return all_data

    @deep_requests()
    def find_title(self, data: BeautifulSoup) -> str:
        title = data.find('span', class_='prouct_name').text
        return title
    
    @deep_requests()
    def find_price(self, data: BeautifulSoup):
        price = data.find('span', class_='price').text
        return price

    @deep_requests()
    def find_articule(self, data: BeautifulSoup):
        articule = data.find('span', class_='sku').text
        return articule

    def build(self):
        soup = self.soup()
        find_all = self.find_all(soup)
        result = []
        for obj in find_all:
            data = {
                'title': self.find_title(obj),
                'price': self.find_price(obj),
                'articule': self.find_articule(obj)
            }
            result.append(data)
            break
        return result
