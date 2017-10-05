''' server.py '''
import socket
import json
import random
import requests

WORD_SITE = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
WORDS = requests.get(WORD_SITE).content.splitlines()

def random_key():
    ''' get a random key from bsd words '''
    return random.choice(WORDS) + '-' + random.choice(WORDS)

def create_server():
    ''' create a server object '''
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # get local machine name
    host = ''
    port = 8080
    sock.bind((host, port)) # bind to the port
    sock.listen(5) # queue up to 5 requests

    rooms = {}

    while 1:
        # establish a connection
        client, addr = sock.accept()

        print('Connection from %s' % str(addr))
        command = client.recv(1024).decode('ascii')
        print(command[0] == '/')
        if command[0] == '/':
            if command == '/CREATE_ROOM':
                print('CREATE_ROOM request from %s' % str(addr))
                room_key = random_key()
                rooms[room_key] = {
                    "songs": [],
                    "state": "PAUSE",
                    "users": [],
                    "host": str(addr)
                }
                client.send((room_key + "\r\n").encode('ascii'))

            elif command == '/JOIN_ROOM':
                print('JOIN_ROOM request from %s' % str(addr))
                room_addr = client.recv(1024).decode('ascii')
                if rooms[room_addr]:
                    client.send(json.dumps(rooms[room_addr]).encode('ascii'))
                else:
                    client.send(('@ ERROR: Invalid room address\r\n').encode('ascii'))

            elif command == '/LEAVE_ROOM':
                print('LEAVE_ROOM request from %s' % str(addr))
                room_addr = client.recv(1024).decode('ascii')
                if rooms[room_addr]:
                    rooms[room_addr]["users"].remove(str(addr))
                    client.send(('Room %s left.' % room_key + "\r\n").encode('ascii'))
                else:
                    client.send(('@ ERROR: Invalid room address').encode('ascii'))

            elif command == '/PLAY':
                print('PLAY request from %s' % str(addr))
                room_addr = client.recv(1024).decode('ascii')
                if rooms[room_addr]:
                    if rooms[room_addr].host == str(addr):
                        rooms[room_addr]["state"] = "PLAY"
                        client.send(json.dumps(rooms[room_addr]).encode('ascii'))
                    else:
                        client.send(('@ ERROR: Invalid permissions\r\n').encode('ascii'))
                else:
                    client.send(('@ ERROR: Invalid room address\r\n').encode('ascii'))

            elif command == '/PAUSE':
                print('PAUSE request from %s' % str(addr))
                room_addr = client.recv(1024).decode('ascii')
                if rooms[room_addr]:
                    if rooms[room_addr].host == str(addr):
                        rooms[room_addr]["state"] = "PAUSE"
                        client.send(json.dumps(rooms[room_addr]).encode('ascii'))
                    else:
                        client.send(('@ ERROR: Invalid permissions\r\n').encode('ascii'))
                else:
                    client.send(('@ ERROR: Invalid room address\r\n').encode('ascii'))

            elif command == '/NEXT_SONG':
                print('NEXT_SONG request from %s' % str(addr))
                room_addr = client.recv(1024).decode('ascii')
                if rooms[room_addr]:
                    if rooms[room_addr].host == str(addr):
                        rooms[room_addr]["state"] = "PLAY"
                        rooms[room_addr]["songs"].pop(0)
                        client.send(json.dumps(rooms[room_addr]).encode('ascii'))
                    else:
                        client.send(('@ ERROR: Invalid permissions\r\n').encode('ascii'))
                else:
                    client.send(('@ ERROR: Invalid room address\r\n')).encode('ascii')

            elif command == '/UPDATE_Q':
                print('UPDATE_Q request from %s' % str(addr))
                room_addr = client.recv(1024).decode('ascii')
                new_queue = json.loads(client.recv(1024).decode('ascii'))
                if rooms[room_addr]:
                    rooms[room_addr]["songs"] = new_queue
                    client.send(('^ Queue updated.\r\n').encode('ascii'))
                else:
                    client.send(('@ ERROR: Invalid room address\r\n'))

            else:
                print('Unknown command received.')
        else:
            print('Unknown command received.')

        client.close()

if __name__ == "__main__":
    create_server()
