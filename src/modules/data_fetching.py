import requests
import json


class DataFetching:

    def __init__(self, api_url):
        self.Data = None
        self.api_url = api_url
        self.__get_api_data()

    def refresh(self):
        self.__get_api_data()

    def get_data(self):
        return self.Data

    def __get_api_data(self):

        try:
            self.Data = requests.get(self.api_url).json()

        except Exception:

            with open('src/config/users.json', 'r') as jsonArchive:
                self.Data = json.load(jsonArchive)