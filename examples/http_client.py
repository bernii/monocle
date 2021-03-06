import sys

import monocle
from monocle import _o
monocle.init(sys.argv[1])

from monocle.stack import eventloop
from monocle.stack.network.http import HttpClient

@_o
def req():
    client = HttpClient()
    try:
        resp = yield client.request('http://www.google.com/')
        print resp.code, resp.body
    finally:
        eventloop.halt()

monocle.launch(req)
eventloop.run()
