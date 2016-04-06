__author__ = 'Tibbers'
from Tkinter import *
import tkMessageBox
from PIL import Image,ImageTk
import socket, threading, sys, traceback, os

class Client:


    #Initialization
    def __init__(self, master, serveraddr, serverport):
        self.master = master
        self.master.protocol("WM_DELETE_WINDOW",self.handler)
        self.createWidgets()
        self.server_addr = serveraddr
        self.server_port = int(serverport)
        self.connectToServer()


    def createWidgets(self):
        "Build GUI"

        #Create Setup button
        self.setup = Button(self.master, width = 20, padx = 3, pady = 3)
        self.setup["text"] =  "Send Data to iOS"
        self.setup["command"] = self.sendDataToiOS
        self.setup.grid(row = 1, column = 0, padx = 2, pady = 2)

    def connectToServer(self):
        "Connect to server"
        self.TCPSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.TCPSocket.connect((self.server_addr, self.server_port))
        except:
            tkMessageBox.showwarning('Connection Failed', 'Connection to \'%s\' failed.' %self.server_addr)

    def sendDataToiOS(self):
        packet = "Hello iOS"
        self.TCPSocket.send(packet)

    def handler(self):
        """Handler on explicitly closing the GUI Window."""
        if tkMessageBox.askokcancel("Quit","GPS Car is shutting off"):
            self.exitClient();

    def exitClient(self):
        """Exit button handler"""
        self.master.destroy()
        sys.exit(0)


if __name__ == "__main__":
	try:
		serverAddr = sys.argv[1]
		serverPort = sys.argv[2]
	except:
		print "[Usage: Client.py Server_IP Server_port]\n"

	root = Tk()

	# Create a new client

	app = Client(root, serverAddr, serverPort)
	app.master.title("PythonClient")
	root.mainloop()
