import websocket
import threading
import time
import json
import string
import random

query = """
  subscription {
    printRequested {
      id
      success
    }
  }
"""

# generate random alphanumeric id
def gen_id(size=6, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def on_message(ws, message):
    # print(f'ws - message: {message}')

    jsonReponse = json.loads(message)

    if jsonReponse['type'] == 'data':
        j = jsonReponse['payload']
        print(f'ws - data: { j }')
        return j



def on_error(ws, error):
    # pass
    print(error)

def on_close(ws):
    print("### closed ###")
    # _payload = {'id': _id, 'type': 'stop'}
    #  self._conn.send(json.dumps(payload))
    # return self._conn.recv()

    # Reimplemented
    # ws.send(json.dumps(payload))

def on_open(ws, headers = None):
    payload = {
            'type': 'connection_init',
            'payload': {'headers': headers}
        }
    # self._conn.send(json.dumps(payload))
    # self._conn.recv()

    # Reimplemented
    # self._ws.run_forever()
    ws.send(json.dumps(payload))
    # ws.recv()

    payload = {'headers': None, 'query': query, 'variables': None}

    _id = gen_id()
    frame = {'id': _id, 'type': 'start', 'payload': payload}
    # self._conn.send(json.dumps(frame))
    # self._conn.recv()

    # Reimplemented
    ws.send(json.dumps(frame))
    # ws.recv()

    def run(*args):
        while True:
            time.sleep(1)
            ws.send("Hello %d")
        time.sleep(1)
        ws.close()
        print("thread terminating...")
    t = threading.Thread(target=run, args=())
    t.start()


def start(callback):
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp('ws://172.16.20.53:7777/graphql',header={'Sec-WebSocket-Protocol': 'graphql-ws'},on_message = on_message, on_error = on_error, on_close = on_close, on_open = on_open)
    ws.on_message =  callback
    ws.run_forever()