from tkinter import Toplevel, PhotoImage, Label, X, Frame, Entry, Button, Text, messagebox, BOTH


class AboutUs(Toplevel):

    def __init__(self):
        Toplevel.__init__(self)
        # window about us
        self.geometry("550x550+550+200")
        self.title("About Us")
        self.resizable(False, False)


        #frame
        self.top = Frame(self, height=550, width=550,  bg='#ffa500')
        self.top.pack(fill=BOTH)

        self.bottom = Frame(self, height=500, bg="#fcba03")
        self.bottom.pack(fill=X)
        self.top_image = PhotoImage(file="C:\\Users\\jhali\\Desktop\\Python\\Icons\\about.png")
        self.top_image_label = Label(self.top, image=self.top_image)
        self.top_image_label.place(x=180, y=35)
        self.heading = Label(self.top, text="About Us", font="arial 15 bold", bg="#ffa500", fg="black")
        self.heading.place(x=260, y=60)

        self.text = Label(self.top, text="This is about us page"
                          "\n This application is made for educational purpose"
                          "\n You can contact us (Jp3 Team) on"
                          "\n Facebook - https://facebook.com/jp3programmers"
                          "\n Instagram - jp3_programmers", font="arial 14 bold", bg="#ffa500", fg="white" )
        self.text.place(x=40, y=100)