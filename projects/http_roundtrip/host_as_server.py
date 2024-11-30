# pip install requests
from http.server import BaseHTTPRequestHandler, HTTPServer
from dotenv import load_dotenv
import os
# Load the .env file 
load_dotenv()

server=os.getenv('HOST_MACHINE_IP')
http_port=os.getenv('HTTP_SERVER_PORT')

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'Hello from the server!')

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=http_port):
    server_address = (server, port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting httpd server on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
