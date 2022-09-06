"""
it's module need's for parsing on site https://enter.kg
"""
import requests
from bs4 import BeautifulSoup


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

    def build(self):
        soup = self.soup()
        find_all = self.find_all(soup)
        print(find_all)
