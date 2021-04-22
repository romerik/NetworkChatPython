#coding:utf-8
import socket
import threading

listeClient=dict()

def listeningClient(serverByClient):
    while True:
        reponse=serverByClient.recv(99999999).decode("utf8")
        if reponse:
            destinataire,message = reponse.split("»")
            destinateur = list(listeClient.keys())[list(listeClient.values()).index(serverByClient)]
            if destinataire=="All people":
                message =destinateur+"(For all people)" + "»" + message
                for i in listeClient:
                    if i!=destinateur:
                        listeClient[i].sendall(message.encode("utf8"))
            else:
                message =destinateur + "»" + message
                try:
                    listeClient[destinataire].sendall(message.encode("utf8"))
                except:
                    pass
    serverByClient.close()

class ClientThread(threading.Thread):
    def __init__(self,client,ip,address):
        threading.Thread.__init__(self)
        self.client=client
        self.ip,self.address=(ip,address)
        print("Connecion by {} {}".format(self.ip,self.address))

    def run(self):
        data = self.client.recv(1024)
        data = data.decode("utf8")
        for i in listeClient:
            listeClient[i].sendall(data.encode("utf8"))
            nom =  i+"«"
            self.client.sendall(nom.encode("utf8"))
        listeClient[data]=self.client
        print(listeClient)
        listeningClient(self.client)


host,port=('',4444)
server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
server.bind((host,port))
print("---------------------Loading server-----------")

while True:
    server.listen(100)
    newClient,(ip,address)=server.accept()
    newThread=ClientThread(newClient,ip,address)
    newThread.start()
