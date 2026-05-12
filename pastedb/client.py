from .api import create_paste_request, knowMe

class Client:

    def __init__(self, api_key):

        self.api_key = api_key

    def makePaste(

        self,

        title,

        content,

        syntax="text",

        visibility="public"
    ):

        data = {

            "title": title,

            "content": content,

            "syntax": syntax,

            "visibility": visibility
        }

        return create_paste_request(

            self.api_key,

            data
        )
        
        def me(self):
            return knowMe(self.api_key)




