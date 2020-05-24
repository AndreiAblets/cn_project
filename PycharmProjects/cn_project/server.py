import socket
from _thread import *
from player_file import Player
import pickle


server = "192.168.0.105"
port = 5555
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#AF_INET refers to the address family ipv4.
                                                    #The SOCK_STREAM means connection oriented TCP protocol.
try:
    s.bind((server, port))
except socket.error as e:
    print(str(e))

s.listen() #разрешение серверу принимать соединения
print("Waiting for a connection, Server Started")

player1 = Player(0, 0, 'g.png', 'top', [0,0,0,1], 3)
player2 = Player(465, 430, 'r.png', 'bottom', [0,1,0,0], 3)
players = [player1, player2]


def threaded_client(conn, player):
    conn.send(pickle.dumps(players[player]))

    while True:
        try:
            data = pickle.loads(conn.recv(512))
            players[player] = data

            if not data:
                print("Disconnected")
                break
            else:
                if player == 1:

                    reply = players[0]

                else:

                    reply = players[1]

            conn.sendall(pickle.dumps(reply))
        except:
            break

    print("Lost connection")
    conn.close()

currentPlayer = 0
while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1