
# Socket
import socket
server_ip = "" # Ip address of Raspberry PI
server_port = 13000 # The socket port
server = socket.socket() # Create socket server
server.bind((server_ip, server_port)) # Bind socket server to ip address and port
server.listen(5)
print("Server Online")
print(server_ip)

# Raspberry PI
import RPi.GPIO as GPIO
RPI_Port = 18 # Sets Raspberry PI port
GPIO.setmode(GPIO.BCM) # Sets GPIO mode
GPIO.setup(RPI_Port, GPIO.OUT) # Setup Raspberry PI Port

while True: # Loop
    client, addr = server.accept() # Get client on connection
    data = client.recv(1024).decode() or None # Gets and decode data
    client.close() # Close client connection

    if data == "on": # Checks if data equals "on"
        GPIO.output(RPI_Port, GPIO.HIGH)
    elif data == "off": # Checks if data equals "off"
        GPIO.output(RPI_Port, GPIO.LOW)
