import os
import threading
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pyngrok import ngrok

# Paste your auth token
ngrok.set_auth_token("3IuKoLN6gCcgsVQNgU9RtExtyeg_if76RVDxPcPNTe7P9SjY")

WEBSITE_FOLDER = os.path.dirname(os.path.abspath(__file__))
os.chdir(WEBSITE_FOLDER)

# --- THE MAGIC NO-CACHE HANDLER ---
class NoCacheHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        # These headers tell the browser: "Do not save any files. Always download them fresh."
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

def run_server():
    # We use NoCacheHandler instead of the default SimpleHTTPRequestHandler
    server = HTTPServer(('localhost', 8000), NoCacheHandler)
    print(f"\n{'='*60}")
    print(f"SERVER RUNNING IN NO-CACHE MODE")
    print(f"Serving: {WEBSITE_FOLDER}")
    print(f"{'='*60}\n")
    server.serve_forever()

server_thread = threading.Thread(target=run_server, daemon=True)
server_thread.start()

print("Starting ngrok tunnel...")
public_url = ngrok.connect(8000)

print(f"\nYOUR WEBSITE IS LIVE AT: {public_url}")
print("Every refresh will download fresh files (No 304 codes!)\n")

input("Press Enter to shut down...")
ngrok.disconnect(public_url)
ngrok.kill()