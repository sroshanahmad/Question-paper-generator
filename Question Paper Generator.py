from tkinter import *
import os
from tkinter.font import Font
import tkinter.messagebox


class Application():
    def __init__(self, root):
        mfont = Font(size=16)
        self.root = root
        self.f1 = Frame(root, height=80)
        self.f1.pack(fill=X)
        self.f2 = Frame(root, height=120, bg='#fcba03')
        self.f2.pack(fill=X)
        self.text = Label(self.f1, text='Welcome To', font=mfont)
        self.text.place(x=175, y=15)
        self.text = Label(self.f1, text='Question Paper Generator', font=mfont)
        self.text.place(x=120, y=45)
        self.b1 = Button(self.f2, text='Create a new Question Paper', command=self.createquestion).place(x=40, y=25)
        self.b2 = Button(self.f2, text='Open a existing Question Paper', command=self.open).place(x=225, y=25)
        self.t1 = Label(self.f2, text='Ver 1.0.0').place(x=5, y=95)

    def createquestion(self):
        self.top = Toplevel()
        self.top.geometry('450x150+960+275')
        self.top.resizable(False, False)
        self.top.title("New Question Paper")

        qfont = Font(size=10)
        self.cl = Label(self.top, text='Path of Question Paper', font=qfont).place(x=30, y=30)
        self.s = StringVar()
        self.s1 = StringVar()
        self.entry = Entry(self.top, width=35, textvariable=self.s)
        self.entry.place(x=180, y=30)
        self.s.set('C:\\Users\\srosh\\Desktop\\')
        self.cl1 = Label(self.top, text='filename & extension', font=qfont).place(x=30, y=60)
        self.entry1 = Entry(self.top, width=35, textvariable=self.s1)
        self.entry1.place(x=180, y=60)
        self.s1.set('Untitled.txt')
        self.cb1 = Button(self.top, text='Cancel', font=qfont, width=20, command=self.top.destroy).place(x=30, y=100)
        self.cb2 = Button(self.top, text='Create Question Paper', font=qfont, width=20, command=self.create).place(
            x=220, y=100)

    def create(self):
        qfont = Font(size=10)
        try:
         self.a1 = self.entry.get()
         self.a2 = self.entry1.get()
         self.file = open(self.a1 + self.a2, 'w+')
         self.top1 = Toplevel()
         self.top1.title("Question Paper Generator")
         self.top1.geometry('450x450+500+75')
         self.top1.resizable(False, False)
         self.crframe1 = Frame(self.top1, height=100)
         self.crframe1.pack()
         self.crframe2 = Frame(self.top1, height=350, )
         self.crframe2.pack(fill=X)
         self.crb1 = Button(self.crframe1, text="QP Code").grid(row=0, column=0, sticky=W + E)
         self.cre1 = Entry(self.crframe1)
         self.cre1.grid(row=0, column=1)

         self.crb2 = Button(self.crframe1, text="Exam Name").grid(row=1, column=0, sticky=W + E)
         self.cre2 = Entry(self.crframe1)
         self.cre2.grid(row=1, column=1)
         self.crb3 = Button(self.crframe1, text="Program").grid(row=2, column=0, sticky=W + E)
         self.cre3 = Entry(self.crframe1)
         self.cre3.grid(row=2, column=1)
         self.crb4 = Button(self.crframe1, text="Course code").grid(row=3, column=0, sticky=W + E)
         self.cre4 = Entry(self.crframe1)
         self.cre4.grid(row=3, column=1)
         self.crb5 = Button(self.crframe1, text="Max Marks").grid(row=0, column=2, sticky=W + E)
         self.cre5 = Spinbox(self.crframe1, from_=5, to=100)
         self.cre5.grid(row=0, column=3)
         self.crb6 = Button(self.crframe1, text="Exam Date").grid(row=1, column=2, sticky=W + E)
         self.cre6 = Entry(self.crframe1)
         self.cre6.grid(row=1, column=3)
         self.crb7 = Button(self.crframe1, text="Semester").grid(row=2, column=2, sticky=W + E)
         self.cre7 = Spinbox(self.crframe1, from_=1, to=8)
         self.cre7.grid(row=2, column=3)
         self.crb8 = Button(self.crframe1, text="Duration(mins)").grid(row=3, column=2, sticky=W + E)
         self.cre8 = Spinbox(self.crframe1, from_=30, to=180)
         self.cre8.grid(row=3, column=3)
         self.crl = Label(self.crframe2, text='ENTER QUESTIONS BELOW').place(x=100, y=7)
         self.t = Text(self.crframe2, height=250, font=qfont, wrap=WORD, width=40, padx=5, pady=10, bd=5)
         self.t.place(x=0, y=35)
         self.crb9 = Button(self.crframe2, text='Create Paper', height=5, bd=5, command=self.createfile).place(x=325,
                                                                                                               y=125)
        except FileNotFoundError:
          tkinter.messagebox.showwarning("ERROR" , "Wrong Path Given")




    def open(self):
        f = Font(size=10)
        w = StringVar()
        self.top2 = Toplevel()
        self.top2.geometry('450x125+960+275')
        self.top2.resizable(False, False)
        self.top2.title("Open Question Paper")
        self.g = Label(self.top2, text='Give Path', font=f, pady=15).grid(row=0, column=0)
        self.e1 = Entry(self.top2, textvariable=w, width=60, bd=3)
        w.set('C:\\Users\\srosh\\Desktop\\Untitled.txt')
        self.e1.grid(row=0, column=1, sticky=W + E)
        self.m = Button(self.top2, text='Open', command=self.fileopen, height=3, width=10).grid(row=3, column=1)

    def fileopen(self):
      try:
        os.startfile(self.e1.get())
        self.top2.destroy()
      except FileNotFoundError:
          tkinter.messagebox.showwarning("ERROR" , 'File Not Found')
    def createfile(self):
        # self.top1.destroy()

         self.a3 = self.cre1.get()
         self.a4 = self.cre2.get()
         self.a5 = self.cre3.get()
         self.a6 = self.cre4.get()
         self.a7 = self.cre5.get()
         self.a8 = self.cre6.get()
         self.a9 = self.cre7.get()
         self.a10 = self.cre8.get()
         self.a11 = self.t.get(1.0, END)

         self.z1 = 'Exam Name : ' + self.a4
         self.z2 = 'Course Code : ' + self.a6
         self.z3 = 'Paper Code : ' + self.a3
         self.z4 = 'Semester : ' + self.a9
         self.z5 = 'Date : ' + self.a8
         self.z6 = 'Max Marks: ' + self.a7
         self.z7 = 'Program : ' + self.a5
         self.z8 = 'Duration : ' + self.a10
         self.file.write(self.z1.ljust(10) + self.z5.rjust(50) + '\n')
         self.file.write(self.z2.ljust(10) + self.z6.rjust(50) + '\n')
         self.file.write(self.z3.ljust(10) + self.z7.rjust(50) + '\n')
         self.file.write(self.z4.ljust(10) + self.z8.rjust(50) + '\n\n\n\n')
         self.file.write(self.a11)
         self.file.close()
         tkinter.messagebox.showinfo('Done', 'The Question Paper has been generated')
         self.top1.destroy()
         self.top.destroy()


root = Tk()
app = Application(root)#CLASS
root.title("Welcome")
root.geometry('450x200+500+275')
root.resizable(False, False)

root.mainloop()
