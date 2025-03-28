from socket  import *
from constCS import * #-



def process(cmd, text):
    if cmd == 'uppercase':
        return text.upper()
    elif cmd == 'lowercase':
        return text.lower()
    elif cmd == 'reverse':
        return text[::-1]
    else:
        return "Erro: Comando desconhecido"
    

s = socket(AF_INET, SOCK_STREAM) 
s.bind((HOST, PORT))  #-
s.listen(1)           #-
print(f"Servidor de Texto ativo em {HOST}:{PORT}...")

(conn, addr) = s.accept()  # returns new socket and addr. client 
print(f"Conexão recebida de {addr}")

while True:                # forever
  data = conn.recv(1024)   # receive data from client
  if not data: break       # stop if client stopped

  msg = bytes.decode(data)
  print(f"Recebido: {msg}")
  
  command_struct = msg.strip().split(maxsplit=1)

  if len(command_struct) < 2:
      ans = "Erro: formato esperado é 'uppercase/lowercase/reverse texto"
  else:
      cmd, text = command_struct
      ans = process(cmd, text)

  conn.send(str.encode(ans+"*")) # return sent data plus an "*"
conn.close()               # close the connection
