from tkinter import *

class floodManagement:

    def __init__(self, master):
        self.master=master
        master.title('Food at Flood - FaF')

        self.left = Frame(master,width=800, height=720, bg='black')
        self.left.pack()

        self.heading = Label(self.left, text="Food at Flood", font=('arial 40 bold'), fg='black', bg='white')
        self.heading.place(x=250, y=0)

        self.submit = Button(self.left, text="Help!!  :)", width=20, height=2, bg='steelblue',font = ('arial 20 bold'),\
                             command=self.buttonclick)
        self.submit.place(x=250, y=340)

    def buttonclick(self):
        import querypage

root=Tk()
obj=floodManagement(root)
root.mainloop()
