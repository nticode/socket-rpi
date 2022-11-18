# Socket
import socket # import socket library
client_ip = "192.168.0.8" # Raspberry PI ip address
client_port = 13000 # Socket port
server = socket.socket() # Create socket server
server.connect((client_ip, client_port)) # Connect socket server to client

# Website
from flask import Flask, render_template, Response # Import flask library for html
server_ip = socket.gethostbyname(socket.gethostname()) # Gets server IP address
server_port = "1011" # Servers Web Port
app = Flask(__name__) # Creates Flask Application


@app.route("/") # Sets "http://{server_ip}:{server_port}/" to run main function
def main():
    return render_template("index.html") # renders index.html

@app.route("/api/<state>", methods = ['POST']) # Listens for POST requests
def on(state):
    server.send(state.encode()) # Sends encoded <state> to client
    return Response(status=200) # Returns status 200 to website

app.run(server_ip, server_port, debug=True) # Starts website