# is_port_listening

import socket

def check_port(host, port):
    # create a socket object
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(5)  # set a timeout for the connection attempt

    try:
        # try to connect to the host on the given port
        sock.connect((host, port))
        return True
    except (socket.timeout, ConnectionRefusedError):
        return False
    finally:
        sock.close()

# usage
is_listening = check_port('localhost', 8000)
print(f"Is port 8000 listening? {is_listening}")