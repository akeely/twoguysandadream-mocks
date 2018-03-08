from SimpleHTTPServer import SimpleHTTPRequestHandler
import BaseHTTPServer


class CustomRequestHandler (SimpleHTTPRequestHandler):
    def end_headers (self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Content-Type', 'application/json')
        SimpleHTTPRequestHandler.end_headers(self)

def run(server_class=BaseHTTPServer.HTTPServer,
        handler_class=CustomRequestHandler):
    server_address = ('', 8080)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

if __name__ == "__main__":
    run()