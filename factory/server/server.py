'''
This file implements the factory method using email accounts as the example
'''
import json
import logging


from typing import Any
from handlers import GmailHandler, YahooHandler, ProtonHandler
from http.server import HTTPServer, BaseHTTPRequestHandler



class handler(BaseHTTPRequestHandler):
    def log_message(self, format: str, *args: Any) -> None:
        logging.info(format % args)
        return super().log_message(format, *args)

    def do_GET(self):

        paths = self.path.split('/')[1:]

        routes_dict = {
            'gmail': GmailHandler(),
            'yahoo': YahooHandler(),
            'proton': ProtonHandler()
        }
        handler = routes_dict.get(paths[0], False)

        if handler:
            response_json = handler.handle(paths[1])


        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        message = {"data": "Hello, World! Here is a GET response"}
        self.wfile.write(bytes(json.dumps(message, ensure_ascii=False), 'utf-8'))

    def do_POST(self):

        paths = self.path.split('/')[1:]
        response_json = {}

        routes_dict = {
            'gmail': GmailHandler(),
            'yahoo': YahooHandler(),
            'proton': ProtonHandler()
        }
        handler = routes_dict.get(paths[0], False)

        if handler:
            # get payload
            length = int(self.headers.get('content-length'))
            message = json.loads(self.rfile.read(length))

            response_json = handler.handle(paths[1], payload=message)
        
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        self.wfile.write(bytes(json.dumps(response_json, ensure_ascii=False), 'utf-8'))



def run_server(server_class=HTTPServer, handler_class=handler):
    server_address = ('0.0.0.0', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


if __name__ == '__main__':
    logging.basicConfig(filename='logs/http_server.log', 
                        level=logging.INFO,
                        format="[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s",
                        datefmt='%Y-%m-%dT%H:%M:%S')
    run_server()