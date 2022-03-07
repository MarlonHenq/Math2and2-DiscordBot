import json

f = open("defaultVariables.json")
content = f.read()
defaultVariables = json.loads(content)
f.close()

def verify(string):
    return True

def input(string):
    if (verify(string)):
        return string
    else:
        return False