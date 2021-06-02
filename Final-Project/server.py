import socketserver
import termcolor
from pathlib import Path
import http.server
from urllib.parse import urlparse, parse_qs
import Server_utils as su
import http.client
import json
from Seq1 import Seq
import jinja2


PORT = 8080
genes_dict = {
    "FRAT1": "ENSG00000165879",
    "ADA": "ENSG00000196839",
    "FXN": "ENSG00000165060",
    "RNU6_269P": "ENSG00000212379",
    "MIR633": "ENSG00000207552",
    "TTTY4C": "ENSG00000228296",
    "RBMY2YP": "ENSG00000227633",
    "FGFR3": "ENSG00000068078",
    "KDR": "ENSMUSG00000062960",
    "ANK2": "ENSG00000145362"
}
def read_html_file(filename):
    return pathlib.Path(filename).read_text()


def read_template_html_file(filename):
    return jinja2.Template(pathlib.Path(filename).read_text())


socketserver.TCPServer.allow_reuse_address = True


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        global contents
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
        PARAMETERS = '?content-type=application/json'
        SERVER = "rest.ensembl.org"
        connection = http.client.HTTPConnection(SERVER)
        if path_name == '/':
            contents = Path('./html/index.html').read_text()
        elif path_name == "/listSpecies":
            try:
                ENDPOINT = '/info/species'
                connection.request('GET', ENDPOINT + PARAMETERS)
                response = connection.getresponse()
                final_response = json.loads(response.read().decode())
                species_list = final_response['species']
                names_list = []
                for elem in species_list:
                    s1 = elem['name']
                    lists = [s1]
                    names_list = names_list + lists
                if 'limit' in arguments:
                    limit = int(arguments['limit'][0])
                    final_list = names_list[:limit]
                    if limit <= len(final_list) :
                        context['length'] = len(names_list)
                        context['final_list'] = final_list
                        context['limit'] = limit
                        contents = su.read_template_html_file('./html/limit_name_list.html').render(context=context)
                    else :
                        contents = su.read_template_html_file('./html/error.html').render(context=context)
                elif 'limit' not in arguments:
                    context['length'] = len(names_list)
                    context['final_list'] = names_list
                    contents = su.read_template_html_file('./html/full_name_list.html').render(context=context)
            except KeyError:
                contents = su.read_template_html_file('./html/error.html').render(context=context)
        elif path_name == "/karyotype" :
            try:
                species_name = arguments['species_name'][0]
                ENDPOINT = '/info/assembly/'
                connection.request('GET', ENDPOINT + species_name + PARAMETERS)
                response = connection.getresponse()
                final_response = json.loads(response.read().decode())
                karyotype = final_response['karyotype']
                context['karyotype'] = karyotype
                contents = su.read_template_html_file('./html/karyotype.html').render(context=context)
            except KeyError:
                contents = su.read_template_html_file('./html/error.html').render(context=context)
        elif path_name == "/chromosomeLength" :
            try:
                if 'species_name' not in arguments:
                    contents = su.read_template_html_file('./html basic/ERROR.html').render()
                elif 'chromosome_name' not in arguments:
                    contents = su.read_template_html_file('./html basic/ERROR.html').render()
                else:
                    global chromosome_length
                    species_name = arguments['species_name'][0]
                    chromosome_name = arguments['chromosome_name'][0]
                    ENDPOINT = '/info/assembly/'
                    connection.request('GET', ENDPOINT + species_name + PARAMETERS)
                    response = connection.getresponse()
                    final_response = json.loads(response.read().decode())
                    list_dict = final_response['top_level_region']
                    for elem in list_dict:
                        if (elem['name'] == chromosome_name) and (elem['coord_system'] == 'chromosome'):
                            chromosome_length = elem['length']
                        else:
                            contents = su.read_template_html_file('./html/error.html').render(context=context)
                    context['chromosome_length'] = chromosome_length
                    contents = su.read_template_html_file('./html/chromosome_length.html').render(context=context)



            except KeyError:
                contents = su.read_template_html_file('./html/error.html').render(context=context)
        elif path_name == "/geneSeq":
            try:
                gene = arguments['gene'][0]
                GENE_ID = genes_dict[gene]

                ENDPOINT = '/sequence/id/'
                connection.request('GET', ENDPOINT + GENE_ID + PARAMETERS)
                response = connection.getresponse()
                final_response = json.loads(response.read().decode())
                sequence = final_response['seq']
                context['sequence'] = sequence
                contents = su.read_template_html_file('./html/Seq.html').render(context=context)
            except KeyError:
                contents = su.read_template_html_file('./html/error.html').render(context=context)
        elif path_name == "/geneInfo":
            try:
                gene = arguments['gene'][0]
                GENE_ID = genes_dict[gene]
                ENDPOINT = '/sequence/id/'
                connection.request('GET', ENDPOINT + GENE_ID + PARAMETERS)
                response = connection.getresponse()
                final_response = json.loads(response.read().decode())
                info_list = final_response['desc'].split(':')
                context['genname'] = gene
                context['start'] = info_list[3]
                context['end'] = info_list[4]
                context['length'] = int(info_list[4]) - int(info_list[3])
                context['id'] = GENE_ID
                context['chromoname'] = info_list[1]
                contents = su.read_template_html_file('./html/Info.html').render(context=context)
            except KeyError:
                contents = su.read_template_html_file('./html/error.html').render(context=context)
        elif path_name == '/geneCalc':
            try:
                gene = arguments['gene'][0]
                GENE_ID = genes_dict[gene]
                ENDPOINT = '/sequence/id/'
                connection.request('GET', ENDPOINT + GENE_ID + PARAMETERS)
                response = connection.getresponse()
                final_response = json.loads(response.read().decode())
                sequence = final_response['seq']
                s = Seq(sequence)
                context['length'] = s.len()
                context['percentageA'] = s.percentage_base('A')
                context['percentageC'] = s.percentage_base('C')
                context['percentageG'] = s.percentage_base('G')
                context['percentageT'] = s.percentage_base('T')
                contents = su.read_template_html_file('./html/Calc.html').render(context=context)
            except KeyError:
                contents = su.read_template_html_file('./html/error.html').render(context=context)
        else:
            pass
        self.send_response(200)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        content_length = len(str.encode(contents))
        self.send_header('Content-Length', content_length)

        # The header is finished
        self.end_headers()

        # Send the response message
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

