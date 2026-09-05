import os
import threading
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pyngrok import ngrok

ngrok.set_auth_token("3IuKoLN6gCcgsVQNgU9RtExtyeg_if76RVDxPcPNTe7P9SjY")

# Debug: Show us exactly what Python sees
print(f"\nDEBUG: This script file is at: {__file__}")
print(f"DEBUG: Absolute path: {os.path.abspath(__file__)}")
print(f"DEBUG: Folder name: {os.path.dirname(os.path.abspath(__file__))}")
print(f"DEBUG: Current working directory: {os.getcwd()}")

WEBSITE_FOLDER = os.path.dirname(os.path.abspath(__file__))

print(f"\n{'='*60}")
print(f"WE WILL SERVE FROM: {WEBSITE_FOLDER}")
print(f"{'='*60}\n")

class SafeHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        print(f"DEBUG: Handler initialized with directory={WEBSITE_FOLDER}")
        super().__init__(*args, directory=WEBSITE_FOLDER, **kwargs)

def run_server():
    server = HTTPServer(('localhost', 8000), SafeHandler)
    print(f"Server running on http://localhost:8000")
    server.serve_forever()

server_thread = threading.Thread(target=run_server, daemon=True)
server_thread.start()

print("Starting ngrok tunnel...")
public_url = ngrok.connect(8000)

print(f"\nYOUR WEBSITE IS LIVE AT: {public_url}")

input("Press Enter to shut down...")
ngrok.disconnect(public_url)
ngrok.kill()