import socketserver
import termcolor
import pathlib
import http.server
from urllib.parse import urlparse, parse_qs
import server_utils as su

import jinja2


PORT = 8080
BASES_INFORMATION = {
    'A': {'link': "https://en.wikipedia.org/wiki/Adenine",
          'formula': "C5H5NH",
          'name': "ADENINE",
          'colour': 'lightgreen'
    },
    'C': {'link': "https://en.wikipedia.org/wiki/Cytosine",
          'formula': "C4H5N3O",
          'name': "CYTOSINE",
          'colour': 'yellow'
    },
    'G': {'link': "https://en.wikipedia.org/wiki/Guanine",
          'formula': "C5H5N5O",
          'name': "GUANINE",
          'colour': 'lightblue'
    },
    'T': {'link': "https://en.wikipedia.org/wiki/Thymine",
          'formula': "C5H6N2O2",
          'name': "TYROSINE",
          'colour': 'pink'
    }
}

list_sequences = ["ACGTAAAAGTTTAAGCGCCAAT", "AGTCCCCCCAAAATTTTGGGGGAATAT", "AGAGAGAGGATTATTATATACTCTTC", "GGGGGGGGGGGTTTTTTTTTAAAAAACCCC", "AAAAAATTTTTCGAAAAAAA"]

list_genes = ["ADA", "FRAT1", "FXN", "RNU6_269P", "U5"]
def read_html_file(filename):
    return pathlib.Path(filename).read_text()


def read_template_html_file(filename):
    return jinja2.Template(pathlib.Path(filename).read_text())


socketserver.TCPServer.allow_reuse_address = True


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        termcolor.cprint(self.requestline, 'green')
        termcolor.cprint(self.path, 'blue')

        o = urlparse(self.path)
        path_name = o.path
        arguments = parse_qs(o.query)
        print("Resource requested: ", path_name)
        print("Parameters: ", arguments)
        # IN this simple server version:
        # We are NOT processing the client's request
        # It is a happy server: It always returns a message saying
        # that everything is ok
        context = {}
        # Message to send back to the client
        if path_name == '/':
            context["n_sequences"] = len(list_sequences)
            context["list_genes"] = list_genes
            contents = su.read_template_html_file('./html/index.html').render(context=context)
        elif path_name == "/ping":
            contents = su.read_template_html_file("./html/ping.html").render()
        elif path_name == "/get":
            number_sequence = arguments["sequence"][0]
            contents = su.get(list_sequences, number_sequence)
        elif path_name == "/gene":
            gene = arguments["gene"][0]
            contents = su.gene(gene)
        elif path_name == "/operation":
            sequence = arguments['sequence'][0]
            calculation = arguments['calculation'][0]
            if calculation == 'Info':
                contents = su.info(sequence)
            elif calculation == 'Comp':
                contents = su.comp(sequence)
            elif calculation == 'Rev':
                contents = su.rev(sequence)
            else:
                contents = su.read_template_html_file("./html/ERROR.html").render()
        else:
            contents = su.read_template_html_file("./html/ERROR.html").render()

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