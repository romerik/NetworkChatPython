# NetworkChatPython
=======
#This application is used to be able to communicate when you are in the same network. There is the server.py application which must be started on a single computer which will be considered as the server. Once the server has started, you can run the client.py client application on as many workstations as you want (100 maximum). At runtime, each client application enters the server's IP address in the Server IP input and the default port must not be modified unless it is modified in the server code. Customers also enter their nickname and immediately connected will see the list of connected in the drop-down list to the right of the send button. It is also in this drop-down list that we choose to whom we want to send a message. By default the message is sent to everyone who is connected. The interface is intuitive enough to be well understood.

#For a good execution, you must have tkinter, threading and socket installed on your computer. The commands are:
pip3 install tkinter
pip3 install socket
pip3 install threading
