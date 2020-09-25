from tkinter import Toplevel, Frame, PhotoImage, Label, X, Listbox, Scrollbar, VERTICAL, N, S, Button, messagebox

from Practices.AboutUs import AboutUs
from Practices.AddPeople import AddPerson
import sqlite3

from Practices.DisplayPeople import DisplayPeople
from Practices.UpdatePeople import UpdatePeople

conn = sqlite3.connect('phonebook.db')
cursor = conn.cursor()


class MyContacts(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)

        self.geometry("650x650+600+200")
        self.title("My Contacts")
        self.resizable(False, False)
        self.top = Frame(self, height=150, bg='white')
        self.top.pack(fill=X)
        self.bottom = Frame(self, height=500, bg="#fcba03")
        self.bottom.pack(fill=X)
        self.top_image = PhotoImage(file="C:\\Users\\jhali\\Desktop\\Python\\Icons\\people.png")
        self.top_image_label = Label(self.top, image=self.top_image)
        self.top_image_label.place(x=180, y=35)
        self.heading = Label(self.top, text="My PhoneBook App", font="arial 15 bold", bg="white", fg="#34baeb")
        self.heading.place(x=260, y=60)
        # scroll bar vertical
        self.scroll = Scrollbar(self.bottom, orient=VERTICAL)
        # list box for data
        self.list_box = Listbox(self.bottom, width=70, height=27)
        self.list_box.grid(row=0, column=0, padx=(30, 0))
        self.scroll.config(command=self.list_box.yview)
        self.list_box.config(yscrollcommand=self.scroll.set)

        persons = cursor.execute("SELECT * FROM contacts").fetchall()
        count = 0
        for person in persons:
            self.list_box.insert(count,
                                 str(person[0]) + " " + person[1] + " " + person[2] + " " + person[3] + " " + person[
                                     4] + " " + person[5])
            count += 1
        # scroll grid
        self.scroll.grid(row=0, column=1, sticky=N + S)

        # buttons
        add_button = Button(self.bottom, text="Add", width=12, font="Sans 12 bold", command=self.addPeople)
        add_button.grid(row=0, column=2, padx=30, pady=10, sticky=N)

        update_button = Button(self.bottom, text="Update", width=12, font="Sans 12 bold", command=self.updateContacts)
        update_button.grid(row=0, column=2, padx=30, pady=50, sticky=N)

        display_button = Button(self.bottom, text="Display", width=12, font="Sans 12 bold",
                                command=self.displayContacts)
        display_button.grid(row=0, column=2, padx=30, pady=90, sticky=N)

        delete_button = Button(self.bottom, text="Delete", width=12, font="Sans 12 bold",
                                command=self.deletePerson)
        delete_button.grid(row=0, column=2, padx=30, pady=130, sticky=N)

    def addPeople(self):
        add_page = AddPerson()
        self.destroy()

    def updateContacts(self):
        selected_item = self.list_box.curselection()
        person = self.list_box.get(selected_item)
        person_id = person.split(" ")[0]
        update_page = UpdatePeople(person_id)
        self.destroy()

    def displayContacts(self):
        selected_item = self.list_box.curselection()
        person = self.list_box.get(selected_item)
        person_id = person.split(" ")[0]
        display_page = DisplayPeople(person_id)
        self.destroy()

    def deletePerson(self):
        selected_item = self.list_box.curselection()
        person = self.list_box.get(selected_item)
        person_id = person.split(" ")[0]

        query = "DELETE FROM contacts where person_id = '{}'".format(person_id)
        string_for_mbox = "Are you sure you wanna delete ", person.split(" ")[1], "?"
        answer = messagebox.askquestion("Warning", string_for_mbox)
        if answer == 'yes':
            try:
                cursor.execute(query)
                conn.commit()
                messagebox.showinfo("Success", "The record was deleted")
                self.destroy()
            except Exception as e:
                messagebox.showerror("Info", str(e))

