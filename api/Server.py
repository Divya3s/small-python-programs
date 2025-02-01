import socket
 
server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
 
server_socket.bind(('127.0.0.1',65433))
server_socket.listen(1)
print("Server is listening on 127.0.0.1:65432....")
 
conn,addr=server_socket.accept()
print(f"Connect to client at {addr}")
 
while True:
    client_message=conn.recv(1024).decode()
    if client_message.lower()=='exit':
        print("Client has disconnected")
        break
    print(f"Client: {client_message}")
 
    server_message=input("Server: ")
    conn.send(server_message.encode())
    if server_message.lower()=='exit':
        print("Server shutting down")
        break
 
 
conn.close()
server_socket.close()