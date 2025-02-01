
 

 
import socket
 
client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
 
client_socket.connect(('127.0.0.1',65433))
print("connect to the server")
 
while True:
    client_message=input("client: ")
    client_socket.send(client_message.encode())
    if client_message.lower()=='exit':
        print("Client Shutting down")
        break
 
    server_message=client_socket.recv(1024).decode()
    if server_message.lower()=='exit':
        print("Server shutting down")
        break
    print(f"server {server_message}")
 
client_socket.close()
 