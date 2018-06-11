import socket
import select
import threading
import string
import random
import Tkinter as tiki
from ScrolledText import *


ENCODING = 'utf-8'
HOST = '127.0.0.1'
PORT = 9999
BUFSIZE = 1024
NICKNAME = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5)) + ' -> '
sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print "Connecting to server"
sckt.connect((HOST, PORT))

motherContainer = tiki.Tk(className=" Poor man's IRC")
motherContainer.minsize(width=300,height=200)
textFrame = ScrolledText(motherContainer, wrap="word", width=60, height=30, font=("Consolas", 11), undo=False,
                         state=tiki.DISABLED)
textFrame.pack(padx=1, pady=1, fill="both", expand=True)
userMessageLabel = tiki.Label(motherContainer, text="=>", font=("Consolas", 10))
userMessageLabel.pack(side=tiki.LEFT)
userMessage = tiki.StringVar()
userMessage.set('')
userInput = tiki.Entry(motherContainer, textvariable=userMessage, font=("Consolas", 11))
userInput.pack(padx=1, pady=1, fill="both", expand=True)


def incoming(connection):
    while True:
        (readable, writable, erroneous) = select.select([connection], [], [connection], 0.1)
        if readable or erroneous:
            message = connection.recv(BUFSIZE).decode(ENCODING)
            if not message:
                print "Disconnected"
                return
            textFrame.config(state=tiki.NORMAL)
            textFrame.insert(tiki.END,message + '\n')
            textFrame.config(state=tiki.DISABLED)


def sendMessage(event=None):
    message = NICKNAME + userMessage.get()
    if NICKNAME + userMessage.get() == NICKNAME + "nox":
        sckt.close()
        motherContainer.quit()
    else:
        userMessage.set("")
        textFrame.config(state=tiki.NORMAL)
        textFrame.insert(tiki.END, message + '\n')
        textFrame.config(state=tiki.DISABLED)
        sckt.send(message.encode(ENCODING))


def close(event=None):
    userMessage.set("nox")
    sendMessage()


userInput.bind("<Return>", sendMessage)
motherContainer.protocol("WM_DELETE_WINDOW", close)
print "Starting incoming thread"
t1 = threading.Thread(target=incoming, args=[sckt])
t1.daemon = True
t1.start()
motherContainer.mainloop()

