from Client0 import Client

list_sequences = ['ACCGTGGTGTAACGAAA', 'ATTTGCTGTCTCT', 'CTCTCTCGAGAGAG', 'TACTCGGCCG', 'CGCGTAGGGATGACGTAGC']
list_genes = ['U5', 'ADA', 'FRAT1', 'FXN', 'RNU6_269P']

IP = "127.0.0.1"
PORT = 8080

c = Client(IP, PORT)
print('Connection to SERVER. Client ip, port: ', str(IP) + ',', str(PORT))

print("- Testing PING...")
response = c.talk("PING")
print(f"{response}")

print("- Testing GET...")
for n in range(0, len(list_sequences)):
    response = c.talk("GET " + str(n))
    print(f"{response}")

print("- Testing INFO...")
response = c.talk("INFO " + list_sequences[0])
print(f"{response}")

print("- Testing COMP...")
response = c.talk("COMP " + list_sequences[0])
print(f"{response}")

print("- Testing REV...")
response = c.talk("REV " + list_sequences[0])
print(f"{response}")

print("- Testing GENE...")
for gene in list_genes:
    response = c.talk("GENE " + gene)
    print(f"{response}")