import socketserver
import termcolor
import pathlib
import http.server

import jinja2


PORT = 8080
HTML_ASSETS = "./html/"
BASES_INFORMATION = {
    "A":{"link": "https://en.wikipedia.org/wiki/Adenine",
        "formula": "C5H5N5",
        "color": "lightgreen",
        "name": "ADENINE"},
    "C":{"link": "https://en.wikipedia.org/wiki/Cytosine",
        "formula": "C4H5N3O",
        "color": "yellow",
        "name": "CYTOSINE"},
    "T":{"link": "https://en.wikipedia.org/wiki/Thymine",
        "formula": "C5H6N2O2",
        "color": "pink",
        "name": "THYMINE"},
    "G":{"link": "https://en.wikipedia.org/wiki/Guanine",
        "formula": "C5H5N5O",
        "color": "lightblue",
        "name": "GUANINE"},
    }


def read_html_file(filename):
    return pathlib.Path(filename).read_text()


def read_template_html_file(filename):
    return jinja2.Template(pathlib.Path(filename).read_text())


socketserver.TCPServer.allow_reuse_address = True


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        termcolor.cprint(self.requestline, 'green')

        if self.path == "/":
            contents = read_html_file(HTML_ASSETS + "index.html")
        elif "/info/" in self.path:
            base = self.path.split("/")[-1]
            context = BASES_INFORMATION[base]
            context["letter"] = base
            contents = read_template_html_file(HTML_ASSETS + "info/general.html").render(base_info=context)

        elif self.path.endswith(".html"):
            try:
                contents = read_html_file(HTML_ASSETS + self.path)
            except FileNotFoundError:
                contents = read_html_file(HTML_ASSETS + "ERROR.html")
        else:
            contents = read_html_file(HTML_ASSETS + "ERROR.html")

        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(contents.encode()))
        self.end_headers()
        self.wfile.write(contents.encode())
        return

Handler = TestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at PORT", PORT)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()