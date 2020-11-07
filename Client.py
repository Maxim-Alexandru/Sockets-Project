import socket

"""
Creating the socket for each client
"""
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 7777))

# Each client will have a unique name, to be identifier easier
name = input("Please enter your nickname: ")
s.send(name.encode())

# The server will verify if the name if indeed unique
# Otherwise, it will ask the client to change its name

serverMessage = s.recv(100).decode()
if serverMessage == "Nickname already in our database. Please choose another one.":
    while serverMessage == "Nickname already in our database. Please choose another one.":
        print(serverMessage)
        name = input("Please enter your nickname: ")
        s.send(name.encode())
        serverMessage = s.recv(100).decode()

# The server sends the total number of clients that are connected
print(serverMessage)

# If the server hosts more than one client, then it will allow clients to send messages
# In order for a client to receive a message, he should constantly listen for a message from the server
# That is way, if the client doesn't want sending a message, but wants to receive one, he will enter 'N' and 'Y'
# If the client wants to leave the session, he will be disconnected

if int(serverMessage) > 1:
    option = input("Would you like to send a message? (Y/N) ")
    while option != "Terminate connection":
        if option == "Y":
            message = input("Please enter the nickname of the person you want to communicate with and the message: ")
            s.send(message.encode())
        else:
            option = input("Would you like to leave te session? ")
            if option != "Y":
                message = s.recv(100).decode()
                while message == "":
                    message = s.recv(100).decode()
                print(message)
            else:
                break
        option = input("Would you like to send a message? (Y/N) ")
    s.send((name + " Terminate connection").encode())

s.close()
