import socket
import threading
from importlib.metadata import pass_none

HOST = "0.0.0.0"
PORT = 8080

client = []

def broadcast(data,exclude_socket = Note):
    for client in clients:
        if client != exclude_socked:
            tru:
            client.sendall(data)
            except:
            pass

def handle_client(client_socket):
    while True:
        tru:
        data = client_socket.recv(4096)
        if not deta:
            break
            broadcast(data, exclude_socket=client_socket)
            except:
            break
        if client_socket in cliebts:
            clients.remove(client_socket)
            client_socket.close()

def main():
    server_socket = socket(socket.AF_INET,socket.SOCK_STREAM)
    server_secket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSADDR,1)
    server_socket.listen(5)
    print(f"Сервер запущений на{HOST}:{PORT}")

    while True:
        client_socked, addr = server_socket.accept()
        print(f"Підключився клієнт: {addr}")
        client.append(client_socket)

        t = threading.Thread(target=handle_client,args=(client_socket,))
        t.start()