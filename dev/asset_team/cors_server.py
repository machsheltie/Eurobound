"""Local helper so Firefly / ChatGPT pages can fetch reference images and POST results back.

Usage: python dev/asset_team/cors_server.py <serve_dir> <inbox_dir> <port>
Only the allowed origins below may use it; uploads never overwrite an existing file.
"""
import sys, os, re, http.server, functools

SERVE, INBOX = sys.argv[1], sys.argv[2]
PORT = int(sys.argv[3]) if len(sys.argv) > 3 else 8765
ALLOWED = {
    "https://firefly.adobe.com",
    "https://chatgpt.com",
    "https://chat.openai.com",
}


class H(http.server.SimpleHTTPRequestHandler):
    def _origin_ok(self):
        return self.headers.get("Origin") in ALLOWED

    def end_headers(self):
        origin = self.headers.get("Origin")
        if origin in ALLOWED:
            self.send_header("Access-Control-Allow-Origin", origin)
            self.send_header("Vary", "Origin")
            self.send_header("Access-Control-Allow-Private-Network", "true")
            self.send_header("Access-Control-Allow-Headers", "Content-Type")
            self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(204 if self._origin_ok() else 403)
        self.end_headers()

    def do_GET(self):
        if not self._origin_ok():
            self.send_response(403); self.end_headers(); return
        super().do_GET()

    def do_POST(self):
        if not self._origin_ok():
            self.send_response(403); self.end_headers(); return
        name = re.sub(r"[^A-Za-z0-9_.-]", "_", self.path.strip("/").split("/")[-1]) or "upload.bin"
        base, ext = os.path.splitext(name)
        path, i = os.path.join(INBOX, name), 1
        while os.path.exists(path):
            path = os.path.join(INBOX, f"{base}_{i}{ext}"); i += 1
        n = int(self.headers.get("Content-Length", 0))
        data = self.rfile.read(n)
        with open(path, "wb") as f:
            f.write(data)
        self.send_response(200); self.end_headers()
        self.wfile.write(f"saved {os.path.basename(path)} {len(data)}".encode())


http.server.ThreadingHTTPServer(("127.0.0.1", PORT), functools.partial(H, directory=SERVE)).serve_forever()
