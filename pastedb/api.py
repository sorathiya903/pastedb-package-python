import requests

class Client:
    def __init__(self, api_key): # Fixed argument name
        self.api_key = api_key   # Match the argument above

    def test(self):
        return self.api_key
