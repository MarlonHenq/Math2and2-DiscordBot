from flask import Flask, request

import stringManage
import execute

queue = 0

def queueId():
    global queue
    queue += 1
    return queue

def newRequest(massage):
    toExecute = stringManage.input(massage)
    if (toExecute != False):
        
        id = queueId()
        response = execute.oct(toExecute, id)

        return response
    else:
        return "Disallowed term detected!"

app = Flask("oct-server")

@app.route("/oct", methods=["GET"])
def main():
    command = request.args.get('command')

    response = newRequest(command)

    return str(response)

app.run(port = 1123, debug = False)