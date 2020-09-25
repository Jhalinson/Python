from tkinter import *

from Practices.AboutUs import AboutUs
from Practices.People import MyContacts
import datetime
from Practices.UpdatePeople import UpdatePeople

date = datetime.datetime.now().date()


class Application(object):
    def __init__(self, master):
        self.master = master
        self.top = Frame(master, height=150, bg='white')
        self.top.pack(fill=X)
        self.botton = Frame(master, height=500, bg="#34baeb")
        self.botton.pack(fill=X)
        self.top_image = PhotoImage(file="C:\\Users\\jhali\\Desktop\\Python\\Icons\\book.png")
        self.top_image_label = Label(self.top, image=self.top_image)
        self.top_image_label.place(x=180, y=35)
        self.heading = Label(self.top, text="My PhoneBook App", font="arial 15 bold", bg="white", fg="#ebb434")
        self.heading.place(x=260, y=60)
        self.date_label = Label(self.top, text="Today's date: " + str(date), font="arial 12 bold", fg="#ebb434",
                                bg="white")
        self.date_label.place(x=450, y=10)
        #  button AddPerson
        self.add_button = Button(self.botton, text="Add New Contact", fg="#42bcf5", bg="white", font="arial 12 bold",
                                 command=self.myContacts)
        self.add_button.place(x=260, y=70)
        #  button ViewPerson
        self.update_button = Button(self.botton, text="  Update Contact  ", fg="#42bcf5", bg="white",
                                    font="arial 12 bold", command=self.updateContacts)
        self.update_button.place(x=259, y=120)
        #  button About US
        self.list_botton = Button(self.botton, text="   About US   ", fg="#42bcf5", bg="white",
                                  font="arial 12 bold", command=self.aboutUs)
        self.list_botton.place(x=275, y=170)

    def myContacts(self):
        people = MyContacts()

    def updateContacts(self):
        updatePeople = UpdatePeople()

    def aboutUs(self):
        about = AboutUs()

def main():
    root = Tk()
    app = Application(root)
    root.title("PhoneBook App")
    root.geometry("650x550+350+200")
    root.resizable(False, False)
    root.mainloop()


if __name__ == '__main__':
    main()
