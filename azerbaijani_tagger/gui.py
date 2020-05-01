import codecs
import os
import threading
import time
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import Listbox, HORIZONTAL
from tkinter.ttk import Progressbar

HEIGHT = 500
WIDTH = 600


def STEMoutput():
    newWindow = tk.Toplevel(width=700, height=500)
    newWindow.resizable(True,True)
    src = ScrolledText(newWindow)
    src.pack(expand=1,fill='both')
    src.configure(state='normal')
    with open("data.txt", 'r', encoding="utf-8-sig") as text:
        my_text = text.read()
    src.insert(tk.INSERT ,my_text)
    src.configure(state='disabled')


def pasteTagtext():
    with open("hmmoutput.txt", 'r', encoding="utf-8-sig") as text:
        my_text = text.read()
    return my_text


def pasteStemtext():
    with open("data.txt", 'r', encoding="utf-8-sig") as text:
        my_text = text.read()
    return my_text



def acc():
    newWindow = tk.Toplevel(width=1100, height=500)
    newWindow.resizable(False, False)
    frame4=tk.Frame(newWindow, bg='white', bd=5, height=600, width=200)
    frame4.pack( side='left')
    frame5=tk.Frame(newWindow, bg='red', bd=5, height=300, width=220)
    frame5.pack(side='right')
    frame6=tk.Frame(newWindow, bg='green', bd=5, height=300, width=200)
    frame6.pack(side='left')
    label1=tk.Label(newWindow,font=16, text="Paste the original text")
    label1.place(relx=0.05, rely=0.05)
    src1 = ScrolledText(frame4, height=10, width=40)
    src1.pack()
    src1.configure(state='normal')
    src2 = ScrolledText(frame5, height=10, width=40)
    src2.pack()
    src2.configure(state='normal')
    label2 = tk.Label(newWindow, font=16, text="Check this text")
    label2.place(relx=0.8, rely=0.05)
    Sbutton = tk.Button(newWindow, text="Check Stemmer", font=20, width=15,command=lambda: src2.insert(tk.INSERT,pasteStemtext()))
    Sbutton.place(relx=0.85, rely=0.8)
    Tbutton = tk.Button(newWindow, text="Check Tagger", font=20, width=15, command=lambda: src2.insert(tk.INSERT,pasteTagtext()))
    Tbutton.place(relx=0.65, rely=0.8)
    txt=tk.Text(frame6,height=5,width=21)
    txt.place(relx=0.04,rely=0.35)
    label3=tk.Label(frame6, font=16, text="Result")
    label3.place(relx=0.35, rely=0.15)
    Rbutton = tk.Button(frame6, text="Run", font=20, width=15,command=lambda: txt.insert(tk.INSERT,check(src1.get('1.0', tk.END),src2.get('1.0', tk.END))))
    Rbutton.place(relx=0.12, rely=0.8)

def check(tekst1,tekst2):
    fout1 = codecs.open("manual.txt", mode='w', encoding="utf-8")
    fout1.write(tekst1)
    fout1.close()
    fout2 = codecs.open("auto.txt", mode='w', encoding="utf-8")
    fout2.write(tekst2)
    fout2.close()
   # time.sleep(1)
    os.system('python chech.py')
    time.sleep(1)
    with open("accuracy.txt", 'r', encoding="utf-8-sig") as text:
        my_text = text.read()
    return my_text

def TAGoutput():
    newWindow=tk.Toplevel(width=700, height=500)
    newWindow.resizable(True,True)
    src = ScrolledText(newWindow)
    src.pack(expand=1,fill='both')
    src.configure(state='normal')
    with open("hmmoutput.txt", 'r', encoding="utf-8-sig") as text:
        my_text = text.read()
    src.insert(tk.INSERT ,my_text)
    src.configure(state='disabled')



def stemming(tekst):
    fout = codecs.open("stemtest.txt", mode='w', encoding="utf-8")
    fout.write(tekst)
    fout.close()
    threading.Thread(target=hg).start()
    threading.Thread(target=progress).start()
    time.sleep(6)
    STEMoutput()

def tagging(tekst):
    tekst=tekst.split()
    my_words=[]
    for word in tekst:
       newWord=""
       punct=""
       for char in word:
           if char in '!,?.:;':
               punct=char
               char=''
           newWord+=char
       if(newWord!=""):
            my_words.append(newWord)
       if (punct!=""):
             my_words.append(punct)
    fout = codecs.open("tagtest.txt", mode='w', encoding="utf-8")
    print(my_words)
    for i in my_words:
        fout.write(i+" ")
    fout.close()
    time.sleep(2)
    threading.Thread(target=progress).start()
    threading.Thread(target=hmm).start()
    time.sleep(2)
    TAGoutput()
    root.update()

root= tk.Tk()
def hg():
    os.system('python main.py')
def hmm():
    os.system('python hmmdecode.py')




canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()
frame1 = tk.Frame(root, bg='gray', bd=5)
frame1.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.5)

frame2 = tk.Frame(root, bg='#80c1ff', bd=5)
frame2.place(relx=0.1, rely=0.62, relwidth=0.8, relheight=0.1)

frame3= tk.Frame(root, bg='green', bd=5)
frame3.place(relx=0.35, rely=0.8, relwidth=0.3, relheight=0.08)





background_label = tk.Label(root, font=16, text= "Welcome, Please choose the operation")
background_label.place(relwidth=1, relheight=0.1)
src=ScrolledText(frame1)
src.pack()


Stembutton = tk.Button(frame2, text="Stem it!", font=40, command=lambda: stemming(src.get('1.0', tk.END)) )
Stembutton.place(relx=0.7, relheight=0.07, relwidth=0.2, x=50, y=270)
Stembutton.pack(side='left')


Tagbutton = tk.Button(frame2, text="Tag it!", font=40, command=lambda: tagging(src.get('1.0', tk.END)) )
Tagbutton.place(relx=0.7, relheight=0.07, relwidth=0.2, x=50, y=270)
Tagbutton.pack(side='right')

Accbutton = tk.Button(frame3, text="Check for Accuracy", font=40, command=lambda: acc() )
Accbutton.place(relx=0.7, relheight=0.07, relwidth=0.2, x=50, y=270)
Accbutton.pack(side='bottom')

pb = Progressbar(frame2, orient = HORIZONTAL,
            max = 100, mode = 'determinate')
pb.pack(side='top')


def progress():
    maxvalue=100
    val=0
    for i in range(15):
        pb['value'] += i
        time.sleep(.3)




root.mainloop()