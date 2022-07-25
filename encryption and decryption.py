
from cProfile import label
from cgitb import reset
from distutils.util import change_root
from email import message
from tkinter import *
import base64
from tokenize import String
from  tkinter import messagebox

screen = Tk()

# size of screen
screen.geometry("820x820") 
screen.title("Message Encryption and Decryption")

# background color change 
screen.configure(bg="light blue")

def encrypt():
    password=code.get()
    if password=="210169":
        screen1=Toplevel(screen)
        screen1.title("Encrypt")
        screen1.geometry("400x250")
        screen1.configure(bg="orange")

        message=text1.get(1.0,END)  #how many text user has enter
        encode_message = message.encode("ascii") # If user type any messsage then it will encode 
        base64_bytes = base64.b64encode(encode_message)    #This is the main line for encode
        encrypt = base64_bytes.decode("ascii")


        Label(screen1,text="Text is Encrypted",font='impack 14').place(x=5,y=6)
        text2 = Text(screen1,font='30',bd=4,wrap=WORD)
        text2.place(x=2,y=50,width=390,height=180)
        text2.insert(END,encrypt)

    elif(password==""):
        messagebox.showerror("Error","Please Enter your Password")
    elif(password!="210169"):
        messagebox.showerror("Oops","Invalid key")
        
def decrypt():
    password=code.get()
    if password=="210169":
        screen2=Toplevel(screen)
        screen2.title("Decrypt")
        screen2.geometry("400x250")
        screen2.configure(bg="orange")

        message=text1.get(1.0,END)  #how many text user has enter
        encode_message = message.encode("ascii") # If user type any messsage then it will decode
        base64_bytes = base64.b64decode(encode_message)    #This is the main line for decode
        encrypt = base64_bytes.decode("ascii")


        Label(screen2,text="Text Is Decrypted",font='impack 14').place(x=5,y=6)
        text2 = Text(screen2,font='30',bd=4,wrap=WORD)
        text2.place(x=2,y=50,width=390,height=180)
        text2.insert(END,encrypt)

    elif(password==""):
        messagebox.showerror("Error","Please Enter your Password")
    elif(password!="210169"):
        messagebox.showerror("Oops","Invalid key")


def reset():
    text1.delete(1.0,END)
    code.set("")


#label
Label (screen,text="Encryption and Decryption Password: 210169", bg="light grey").place(x=5,y=6)

# text 
text1=Text(screen, font='20')
text1.place(x=150,y=100,width=510,height=125)
#label
Label(screen,text="Entery Your Password", font='14').place(x=340,y=280)
#Entry visit
code=StringVar()
Entry(textvariable=code,bd=4,font="25",show="*").place(x=320,y=320)

#button
Button(screen,text="Encrypt",font="arial 15",bg='green',fg='white',command=encrypt).place(x=300,y=400)
Button(screen,text="Decrypt",font="arial 15",bg='grey',fg='white',command=decrypt).place(x=450,y=400)
Button(screen,text="Reset",font="arial 15",bg='orange',fg='white',command=reset).place(x=380,y=460)

mainloop()
 
