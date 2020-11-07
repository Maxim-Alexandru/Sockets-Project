import time
import socket
from threading import Thread

"""
In order to keep track of the clients connected to the server, the application will store
in 2 different lists the name of the client and its socket.
"""

listOfClients = []
listOfNames = []


def receiveMessagesAndSendResponses(cs, ):
    # The server will display the IP and the port of the processed client
    print("Processing the following client: " + str(addr))
    message = cs.recv(10).decode()

    # Here, it will verify whether or not the name if already in use

    if not (message in listOfNames):
        listOfNames.append(message)
    else:
        while message in listOfNames:
            cs.send(str("Nickname already in our database. Please choose another one.").encode())
            message = cs.recv(10).decode()
        listOfNames.append(message)
    time.sleep(15)

    # The server informs the clients about the total number of
    # users connected 10 seconds from the start of the session

    cs.send(str(listOfClients.__len__()).encode())

    # The message from the user that wants to communicate will contain
    # the name of the client whom he wants to communicate with, and the
    # the actual message

    message = cs.recv(100).decode()
    strings = message.split()
    messageForDestination = ""

    for i in range(1, len(strings)):
        messageForDestination += strings[i] + " "
    listOfClients.__getitem__(listOfNames.index(strings[0])).send(
        ("You have a message from " + listOfNames.__getitem__(
            listOfClients.index(cs)) + " " + messageForDestination).encode())

    message = cs.recv(25).decode()
    if "Terminate connection" in message:
        listOfNames.remove(message.split[0])
        listOfClients.remove(listOfClients.__getitem__(listOfNames.index(message.split[0])))

    cs.close()


"""
The instructions needed for creating a socket used by the server
"""
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("0.0.0.0", 7777))
s.listen(5)
ok = True

"Here, the server will handle each client trough multithreading"

while ok:
    cs, addr = s.accept()
    listOfClients.append(cs)
    t = Thread(target=receiveMessagesAndSendResponses, args=(cs,))
    t.start()

