

class myhandler(baseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; <charset=vtf-g')
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd =HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.ssserve_forever()