import requests
import json
import base64

BASE_URL = "https://blog.divinechristianassembly.com/wp-json/wp/v2/posts/"

user = "DCA_Admin"
password = "owRQ DsqR MaQr 6cz6 Bc4t zWwO"

credentials = user + ':' + password

token = base64.b64encode(credentials.encode())

headers = {'Authorization': 'Basic ' + token.decode('utf-8')}

data = {
    "title": "Tope Test",
    "content": "TEST CONTENT OF THE THIS TEST PAGE via PYTHON",
    "status": "publish",
    "meta_fields": {
        'Author': "Testing Tope June 13th"
    }
}

response = requests.post(BASE_URL, headers=headers, data=data)

print(response.content)
