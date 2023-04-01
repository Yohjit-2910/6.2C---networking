# Import the necessary modules
from socket import *

# Define a dictionary containing domain names and their corresponding IP addresses
dns_data = {
    'www.google.com': '142.250.192.14',
    'www.facebook.com': '157.240.23.35',
    'www.chalkpad.com': '52.206.180.240',
    'www.netflix.com': '54.74.73.31',
    'www.w3schools.com': '76.223.115.82',
    'www.trello.com': '104.192.137.10',
    'www.geeksforgeeks.com': '199.59.243.223'
}

# Set the IP address and port number for the server
serverAddress = 'localhost'
Port = 65534
# choosing this port as this port is not used in any computer by default and will work in every computer

# Create a socket object for the server using UDP protocol
serverSocket = socket(AF_INET, SOCK_DGRAM)

# Bind the server socket to the IP address and port number
serverSocket.bind((serverAddress, Port))

# Print a message to confirm that the server is running and listening for incoming connections
print("The server is listening")

while True:

    # Receive the data sent by the client and the address of the client
    client_request, client_address = serverSocket.recvfrom(2048)

    # Decode the data received from the client to get the domain name for which the IP address is requested
    client_request = client_request.decode()

    # Search for the IP address of the requested domain name in the dictionary
    sample_ip = dns_data.get(
        client_request, "No website with this name available").encode()

    # Send the IP address of the requested domain name to the client
    serverSocket.sendto(sample_ip, client_address)
