#Question 10 (Client-Srever Program)

import socket

def start_server(host='127.0.0.1', port=65432):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.bind((host, port))
            server_socket.listen()
            print(f"Server listening on {host}:{port}...")

            conn, addr = server_socket.accept()
            with conn:
                print(f"Connected by {addr}")
                message = "Hello from server!"
                conn.sendall(message.encode())
                print("Message sent to client.")
    except Exception as e:
        print(f"Server error: {e}")

if __name__ == "__main__":
    start_server()

