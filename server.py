import http.server
import ssl
import os

# cannot use reverse proxy with tls services
# traefik gives error with cert: valid for 127.0.0.1, ::1, not 172.27.212.222"
# my-router-1:
#       #  entryPoints:
#         #  - websecure
#       rule: "Host(`traefik-test.dev.localhost`)"
#       service: custom-service-1
#       tls:
#         domains:
#           - main: "dev.localhost"
#             sans:
#               - "*.dev.localhost"
# services:
#     custom-service-1:
#       loadBalancer:
#         servers:
#           - url: "https://172.27.212.222:8499/"

class OKHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"OK")

def run(server_class=http.server.HTTPServer, handler_class=OKHandler, port=8499):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    current_dir = os.path.dirname(os.path.abspath(__file__))
    keyfile_path = os.path.join(current_dir, "traefik/certificates/localhost-key.pem")
    certfile_path = os.path.join(current_dir, "traefik/certificates/localhost.pem")
    httpd.socket = ssl.wrap_socket(httpd.socket, keyfile=keyfile_path, certfile=certfile_path, server_side=True)
    print(f"Starting server on port {port}...")
    httpd.serve_forever()

if __name__ == '__main__':
    run()
