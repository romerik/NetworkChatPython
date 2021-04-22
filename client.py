#coding:utf-8
import socket, tkinter, threading
from tkinter import messagebox,ttk

root = tkinter.Tk()
root['bg']="green"
root.title("Application client")
connectionSuccess=tkinter.StringVar()

hote=""
port=0
socketClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def listening():
    try:
        while True:
            data=socketClient.recv(99999999).decode("utf8")
            if len(data.split("»"))==1:
                tmp = data.split("«")
                for i,name in enumerate(tmp):
                    if name.split()=="":
                        tmp.__delitem__(i)
                print("TMP = {}".format(tmp))
                ConnectedClient.extend(tmp)
                for i,name in enumerate(ConnectedClient):
                    if name.split()=="" or len(name)==0:
                        ConnectedClient.__delitem__(i)
                print("CLIENT = {}".format(ConnectedClient))
                listClient["values"]=ConnectedClient
            else:
                destineur,data = data.split("»")
                messages.configure(state='normal')
                messages.insert(1.0,f"\n{destineur} : {data}")
                messages.configure(state='disabled')
    except:
        pass
def sendingMessage():
    destinataire = listClient.get()
    if destinataire.split()=="":
        listClient.focus_set()
    else:
        message = text.get("1.0","end")
        data = destinataire + "»" + message
        try:
            socketClient.sendall(data.encode("utf8"))
            messages.configure(state='normal')
            messages.insert(1.0,f"\nMe (to {destinataire}) : {message}")
            messages.configure(state='disabled')
        except:
            pass

def DisplayConnect():
    if connectionSuccess.get()=="You are connected" or connectionSuccess.get()=="Connection failed":
        connectionSuccess.set("")
    if entryIpVar.get().strip()=="" or entryPortVar.get().strip()=="" or pseudoClient.get().strip()=="":
        if entryIpVar.get().strip()=="":
            entryIp.focus_set()
        elif entryPortVar.get().strip()=="":
            entryPort.focus_set()
        else:
            entrypseudoClient.focus_set()
    else:
        if(len(connectionSuccess.get()) <= 13):
            if(len(connectionSuccess.get()) ==0):
                connectionSuccess.set("Connecting")
            connectionSuccess.set(connectionSuccess.get()+".")
            labelConnect.after(100,DisplayConnect)
        else:
            hote = entryIpVar.get()
            port = entryPortVar.get()
            try:
                socketClient.connect((hote,int(port)))
                connectionSuccess.set("You are connected")
                socketClient.sendall(entrypseudoClient.get().encode("utf8"))
                th1 = threading.Thread(target=listening)
                th1.start()
            except:
                connectionSuccess.set("Connection failed")


entryIpVar=tkinter.StringVar()
entryPortVar=tkinter.StringVar()
pseudoClient=tkinter.StringVar()
entryIpVar.set("localhost")
entryPortVar.set("4444")

labelIp=tkinter.Label(root,text="Server Ip Adress :",bg="gray")
labelIp.grid(row=0,column=0,pady=10)

labelpseudoClient = tkinter.Label(root,text="Your pseudo:",bg="gray")
labelpseudoClient.grid(row=0,column=2,pady=15)

entryIp=tkinter.Entry(root,textvariable=entryIpVar)
entryIp.grid(row=0,column=1,pady=10)

labelPort=tkinter.Label(root,text="Server Port Number :",bg="gray")
labelPort.grid(row=1,column=0,pady=10)

entryPort=tkinter.Entry(root,textvariable=entryPortVar)
entryPort.grid(row=1,column=1,pady=10)

entrypseudoClient = tkinter.Entry(root,textvariable=pseudoClient)
entrypseudoClient.grid(row=1,column=2,pady=15)

buttonConnect = tkinter.Button(root,text="Connect to server",bg="orange",command=DisplayConnect)
buttonConnect.grid(row=2,column=0)

labelConnect = tkinter.Label(root,textvariable=connectionSuccess,bg="green",width=20)
labelConnect.grid(row=2,column=1)

labelWrite = tkinter.Label(root,text="Write a message:",bg="green",fg="white")
labelWrite.grid(row=3,column=0,pady=10)

text = tkinter.Text(root,width=25,height=5)
text.grid(row=3,column=1,pady=10)

send = tkinter.Button(root,text="Send to",bg="orange", command=sendingMessage)
send.grid(row=3,column=2,padx=15)

ConnectedClient=["All people"]
listClient=ttk.Combobox(root,values=ConnectedClient,state="readonly")
listClient.current(0)

listClient.grid(row=3,column=3,padx=15)

labelNom = tkinter.Label(root,text="Serveur:",font=('times', 15, 'bold'),fg="white",bg="gray")
labelNom.grid(row=5,column=0,pady=10)

serverWelcome = tkinter.Message(root,text="Welcome to you . Now you can chat with your pair",bd=5,fg="blue",font=('times', 10, 'italic'),width=800,justify="left")
serverWelcome.grid(row=5,column =1,sticky="WE",columnspan=3,pady=10)

messages = tkinter.Text(root,bg="green",width=100,height=25,fg="white")
messages.configure(state='disabled')
messages.grid(column=2)
root.mainloop()