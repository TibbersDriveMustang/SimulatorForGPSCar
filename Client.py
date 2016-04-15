__author__ = 'Tibbers'
from Tkinter import *
import tkMessageBox
from PIL import Image,ImageTk
import socket, threading, sys, traceback, os
import time

class Client:


    #Initialization
    def __init__(self, master, serveraddr, serverport):
        self.master = master
        self.master.protocol("WM_DELETE_WINDOW",self.handler)
        self.localPort = 0
        self.localIP = ""

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


        #Create GPS button
        #self.GPS = Button(self.master, width = 20, padx = 3, pady = 3)
        #self.GPS["text"] = "Start GPS"
        #self.GPS["command"] = self.send

        #Create Listen button
        self.listen = Button(self.master, width = 20, padx = 3, pady = 3)
        self.listen["text"] =  "Listening iOS"
        self.listen["command"] = self.listenToiOS
        self.listen.grid(row = 1, column = 1, padx = 2, pady = 2)

    def connectToServer(self):
        "Connect to server"
        self.TCPSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.TCPSocket.connect((self.server_addr, self.server_port))
        except:
            tkMessageBox.showwarning('Connection Failed', 'Connection to \'%s\' failed.' %self.server_addr)

        try:
            self.localIP = (self.TCPSocket.getsockname()[0])
            self.localPort = (self.TCPSocket.getsockname()[1])
            print("Local port number")
            print(self.localPort)
        except:
            tkMessageBox.showwarning('Failed', 'get local port number failed.')

    def sendDataToiOS(self):
        packet = raw_input("Enter data: ")
        #packet = "setPeerToPeer"
        self.TCPSocket.send(packet)

    def listenToiOS(self):
        """Listen to incoming message"""

        self.listenSocket =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        #self.listenSocket.bind((self.localIP,self.localPort))
        self.listenSocket.bind(("",17642))
        self.listenSocket.listen(5)
        print "Listening from iOS..."

        #(clientsocket, address) = threading.Thread(target=self.listenSocket.accept).start()
        threading._start_new_thread(self.listenSocket.accept,self)
        #self.playEvent = threading.Event()
        #self.playEvent.clear()
        #(clientsocket, address) = self.listenSocket.accept()
        print "Connection Accepted..."




            #data = (connect.recv(1024))
            #print data
        #except:
         #   tkMessageBox.showwarning('Connection Failed','Listening iOS failed...')


        #connect,address = self.listenSocket.accept()


    #def receivingServerData(self):
     #   self.localSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      #  try:
       #     self.localSocket

    def handler(self):
        """Handler on explicitly closing the GUI Window."""
        if tkMessageBox.askokcancel("Quit","GPS Car is shutting off"):
            self.exitClient()

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
