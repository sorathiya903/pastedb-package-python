from .api import create_paste_request, knowMe

class Client:

    def __init__(self, api_key):

        self.api_key = api_key

    def makePaste(

        self,data :dict
    ):

        info=data
        return create_paste_request(

            self.api_key,

            info
        )
        
    def me(self):
        return knowMe(self.api_key)




