import socket
import sys
import select

# get two python programs to talk to each other over a network.

# connecting to a socket is analogous to opening a file. 
# receiving data is analogous to reading a file

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.connect(("localhost", 5555))


# select.select() will wait until data is ready to be read
running = True
while running:
    inputready, outputready, exceptready = select.select([my_socket, sys.stdin], [], [])
# for this exercise we only care about reading...WHY.

# three lists of arguments for input:

# A list to check if they're available for reading
# A list to check if they're available for writing
# A list to check if they have an exception


    
    for s in inputready:
        # what connection type was returned? 

        if s == my_socket:
            msg = s.recv(1024)

            if msg:
                print msg
            else:
                print "Disconnected from server!"
                running = False

        else: 
            # get a line of input from the user (keyboard) 
            user_input = s.readline()

            # send input to server socket
            my_socket.sendall(user_input)





# receive 1024 bytes from the socket and display them
data = my_socket.recv(1024)
print "received:\n%s" % data

# get a line of input from the user (keyboard) 
user_input = sys.stdin.readline()

# send input to server socket
my_socket.sendall(user_input)

# receive another 1024 bytes from socket and display
data = my_socket.recv(1024)
print "received:\n%s" % data

# just like with our file handle, 
# it's good practice to call .close() on our socket when we're finished with it.
my_socket.close()


