from socket  import *
from constCS import * #-

s = socket(AF_INET, SOCK_STREAM)
s.connect((HOST, PORT)) # connect to server (block until accepted)


while True:
    inp = input("Commando: uppercase/lowercase/reverse texto OU 'q' para sair ")

    if inp.lower() == 'q':
        break
    
    s.send(str.encode(inp))
    data = s.recv(1024)     # receive the response
    print ("Servidor: ", bytes.decode(data))            # print the result

s.close()               # close the connection
