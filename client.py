# Documentation
# Name : Yohjit Chopra
# Roll No. 2110994798

# Import the necessary modules
from socket import *

# Set the IP address and port number for the server
Client_IP = "localhost"
Port = 65534

# Create a socket object for the client using UDP protocol
clientSocket = socket(AF_INET, SOCK_DGRAM)

# Start an infinite loop to keep the client running until the user decides to quit
while True:
    # Get the website name from the user for which the IP address is required
    website_name = input("Website name you wish to get the IP address of: ")

    # Send the website name to the server
    data_send = clientSocket.sendto(website_name.encode(), (Client_IP, Port))

    # Receive the IP address of the requested website from the server
    ip_address, address = clientSocket.recvfrom(2048)
    cname, address = clientSocket.recvfrom(2048)

    # Decode the received data to get the IP address as a string
    server_rec = ip_address.decode()
    cname_rec = cname.decode()

    # Print the IP address of the requested website
    print(f"The IP address for the required host is : {server_rec}")
    print(f"The CNAME for the required host is : {cname_rec}")
    print('')

    # Ask the user if they want to continue
    continuation = input("Wish to continue (y/n):  ")

    # If the user chooses to quit, break out of the loop
    if continuation.lower() == "n":
        break

# Close the client socket once the user is done
clientSocket.close()
