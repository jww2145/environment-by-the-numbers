from http.server import BaseHTTPRequestHandler
from flask import Flask

app = Flask()

@app.route('/')
def hello():
    return "Hello, World!"

class handler(BaseHTTPRequestHandler):
 
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write('Hello, world!'.encode('utf-8'))
        return

