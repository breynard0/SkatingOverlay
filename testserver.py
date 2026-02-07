import http.server
import socketserver
import mimetypes
from functools import partial

PORT = 4192
DIRECTORY = "."

# Explicitly map .json to application/json
mimetypes.add_type('application/json', '.json')

class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Adding CORS headers to every response
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

    def do_OPTIONS(self):
        """Respond to browser preflight requests."""
        self.send_response(204)
        self.end_headers()

# Use partial to pass the directory argument to the Handler class
handler_with_directory = partial(Handler, directory=DIRECTORY)

with socketserver.TCPServer(("", PORT), handler_with_directory) as httpd:
    print(f"Serving files from '{DIRECTORY}' at http://localhost:{PORT}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server.")
        httpd.server_close()