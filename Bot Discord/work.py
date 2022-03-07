import requests
from requests.utils import quote
import json

f = open("keys.env")
content = f.read()
data = json.loads(content)
f.close()

def input(message):
    command = message.replace("-mth ", "")
    command = quote(command)

    r = requests.get(data["SeverHTTP"], params={"command": command})
    return r.text
    