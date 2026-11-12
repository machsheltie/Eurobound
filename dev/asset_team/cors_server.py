import sys, os, re, http.server, functools
SERVE, INBOX = sys.argv[1], sys.argv[2]
class H(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Private-Network', 'true')
        self.send_header('Access-Control-Allow-Headers', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        super().end_headers()
    def do_OPTIONS(self):
        self.send_response(204); self.end_headers()
    def do_POST(self):
        name = re.sub(r'[^A-Za-z0-9_.-]', '_', self.path.strip('/').split('/')[-1]) or 'upload.bin'
        n = int(self.headers.get('Content-Length', 0))
        data = self.rfile.read(n)
        with open(os.path.join(INBOX, name), 'wb') as f: f.write(data)
        self.send_response(200); self.end_headers(); self.wfile.write(f'saved {name} {len(data)}'.encode())
PORT=int(sys.argv[3]) if len(sys.argv)>3 else 8765
http.server.ThreadingHTTPServer(('127.0.0.1', PORT), functools.partial(H, directory=SERVE)).serve_forever()
