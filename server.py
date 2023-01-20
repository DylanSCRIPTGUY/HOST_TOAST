import os
from http.server import BaseHTTPRequestHandler, HTTPServer

class RequestHandler(BaseHTTPRequestHandler):
    def _send_response(self, message):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(bytes(message, "utf8"))

    def do_GET(self):
        if self.path == '/':
            filename = 'index.html'
        else:
            filename = self.path[1:]

        if not os.path.isfile(filename):
            self.send_error(404, f"File not found: {self.path}")
            return

        with open(filename, 'r') as f:
            message = f.read()

        self._send_response(message)

def run(server_class=HTTPServer, handler_class=RequestHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting httpd on port {port}...')
    httpd.serve_forever()

if __name__ == "__main__":
    run()
