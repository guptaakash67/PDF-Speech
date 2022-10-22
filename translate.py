import requests, uuid, json
from main import *

# Add your key and endpoint
key = "e080665c75bc4281819fa6c7b56330e9"
endpoint = "https://api.cognitive.microsofttranslator.com"


class MyTranslate:
    # location, also known as region.
    # required if you're using a multi-service or regional (not global) resource. It can be found in the Azure portal on the Keys and Endpoint page.
    def __init__(self, text_input, translate_to_language):
        self.location = "centralindia"
        self.path = '/translate'
        self.constructed_url = endpoint + self.path
        self.params = {
            'api-version': '3.0',
            'from': 'en',
            'to': translate_to_language          # ['mr', 'hi']
        }
        self.constructed_url = endpoint + self.path

        self.headers = {
            'Ocp-Apim-Subscription-Key': key,
            # location required if you're using a multi-service or regional (not global) resource.
            'Ocp-Apim-Subscription-Region': self.location,
            'Content-type': 'application/json',
            'X-ClientTraceId': str(uuid.uuid4())
        }

        # You can pass more than one object in body.
        self.input_text = text_input
        self.body = [{
            'text': self.input_text
        }]

    def connection(self):
        request = requests.post(self.constructed_url, params=self.params, headers=self.headers, json=self.body)
        response = request.json()
        # print(response[0]["translations"][0]["text"])
        return response[0]["translations"][0]["text"]

        # print(json.dumps(response, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': ')))



# test = Translate(text_input="Maza nav Yash aahe", translate_to_language="mr")
# test.connection()
