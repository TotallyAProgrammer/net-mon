from http.server import SimpleHTTPRequestHandler, HTTPServer

HOST = "0.0.0.0"
PORT = 8080

class webServer(SimpleHTTPRequestHandler):
    def do_GET_old(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>Test</title></head>", "utf-8"))
        self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p>This is an example web server.</p>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))

if __name__ == "__main__":        
    ws = HTTPServer((HOST, PORT), webServer)
    print("Server started http://%s:%s" % (HOST, PORT))

    try:
        ws.serve_forever()
    except KeyboardInterrupt:
        pass

    ws.server_close()
    print("Server stopped.")
