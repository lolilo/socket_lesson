import socket

# connecting to a socket is analogous to opening a file. 
# receiving data is analogous to reading a file

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.connect(("localhost", 5555))

# receive 1024 bytes from the socket and display them
data = my_socket.recv(1024)
print "received:\n%s" % data

# get a line of input from the user (keyboard) 
user_input = sys.stdin.readline()

# just like with our file handle, 
# it's good practice to call .close() on our socket when we're finished with it.
my_socket.close()


