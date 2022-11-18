import socket
import RPi.GPIO as GPIO

client_ip = socket.gethostbyname(socket.gethostname()) # Ip address of Raspberry PI
client_port = 13000 # The socket port

server = socket.socket()
server.bind((client_ip, client_port))
server.listen(5)
print("Server Online")

data = None # Set the data to none
RPi_Port = 18 # Sets Raspberry PI port

while True: # Loop
    client, addr = server.accept() # Waits for connection
    data = client.recv(1024).decode() # Gets and decode data
    client.close() # Close client connection

    if data == "on": # Checks if data equals "on"
        GPIO.output(18, GPIO.HIGH)
    elif data == "off": # Checks if data equals "off"
        GPIO.output(18, GPIO.LOW)
