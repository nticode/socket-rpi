# Socket
import socket # import socket library
client_ip = "192.168.0.8" # Raspberry PI ip address
client_port = 13000 # Socket port

# Website
from flask import Flask, render_template, Response # Import flask library for html
server_ip = "192.168.0.9" # Gets client IP address
server_port = "1011" # Client Web Port
app = Flask(__name__) # Creates Flask Application


@app.route("/") # Sets "http://{server_ip}:{server_port}/" to run main function
def main():
    return render_template("index.html") # renders index.html

@app.route("/api/<state>", methods = ['POST']) # Listens for POST requests
def on(state):
    client = socket.socket() # Create socket client
    client.connect((client_ip, client_port)) # Connect socket client to server
    client.send(state.encode()) # Sends encoded <state> to server
    client.close() # Closes socket client
    return Response(status=200) # Returns status 200 to website

app.run(server_ip, server_port) # Starts website
