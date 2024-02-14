from http.server import BaseHTTPRequestHandler
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World!"

class handler(BaseHTTPRequestHandler):
 
    def do_GET(self):
        self.send_response(200)
        return

