import requests
from bs4 import BeautifulSoup



def deep_requests():

    def main_request(func):

        def wrapper(self, data):

            link = data.find('a').get('href')
            url = self.response.URL + link
            response = requests.get(url).text
            soup = BeautifulSoup(response, 'lxml')

            return func(self, soup)

        return wrapper

    return main_request