"""Lab 11 (Jenkins Pipelines): a tiny web application without external dependencies."""
from http.server import BaseHTTPRequestHandler, HTTPServer

STUDENT = "Mykytyshyn"
PORT = 5000


def greeting(name: str = STUDENT) -> str:
    """Text that the application returns to the client."""
    return f"Hello from Jenkins pipeline, {name}!"


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        body = (greeting() + "\n").encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


def make_server(port: int = PORT) -> HTTPServer:
    return HTTPServer(("0.0.0.0", port), Handler)


if __name__ == "__main__":
    print(f"Listening on port {PORT}", flush=True)
    make_server().serve_forever()
