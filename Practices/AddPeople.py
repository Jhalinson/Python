from tkinter import Toplevel, PhotoImage, Frame, X, Entry, Label, Button, N, Text, messagebox, EXCEPTION
import sqlite3

conn = sqlite3.connect("phonebook.db")
cursor = conn.cursor()


class AddPerson(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)

        self.geometry("650x650+600+200")
        self.title("Add New Person")
        self.resizable(False, False)
        self.top = Frame(self, height=150, bg='white')
        self.top.pack(fill=X)
        self.bottom = Frame(self, height=500, bg="#fcba03")
        self.bottom.pack(fill=X)
        self.top_image = PhotoImage(file="C:\\Users\\jhali\\Desktop\\Python\\Icons\\people.png")
        self.top_image_label = Label(self.top, image=self.top_image)
        self.top_image_label.place(x=180, y=35)
        self.heading = Label(self.top, text="Add New Person", font="arial 15 bold", bg="white", fg="#34baeb")
        self.heading.place(x=260, y=60)
        # All labels and inputs
        # name label
        self.label_name = Label(self.bottom, text="Name:", font="arial 15 bold", fg="black", bg="#e6e2da")
        self.label_name.place(x=49, y=40)
        # name input
        self.entry_name = Entry(self.bottom, width=30, bd=4)
        self.entry_name.insert(0, "Enter Name")
        self.entry_name.place(x=170, y=42)

        # surname label
        self.last_surname = Label(self.bottom, text="Surnames:", font="arial 15 bold", fg="black", bg="#e6e2da")
        self.last_surname.place(x=49, y=90)
        # surname  input
        self.entry_surname = Entry(self.bottom, width=30, bd=4)
        self.entry_surname.insert(0, "Enter Surnames")
        self.entry_surname.place(x=170, y=92)

        # email label
        self.email_label = Label(self.bottom, text="Email:", font="arial 15 bold", fg="black", bg="#e6e2da")
        self.email_label.place(x=49, y=140)
        # email  input
        self.entry_email = Entry(self.bottom, width=30, bd=4)
        self.entry_email.insert(0, "Enter Email")
        self.entry_email.place(x=170, y=142)

        # phone number label
        self.phone_number_label = Label(self.bottom, text="Phone #:", font="arial 15 bold", fg="black", bg="#e6e2da")
        self.phone_number_label.place(x=49, y=190)
        # phone number  input
        self.entry_phone_number = Entry(self.bottom, width=30, bd=4)
        self.entry_phone_number.insert(0, "Enter Phone #")
        self.entry_phone_number.place(x=170, y=192)

        # address label
        self.address_label = Label(self.bottom, text="Address:", font="arial 15 bold", fg="black",
                                   bg="#e6e2da")
        self.address_label.place(x=49, y=240)
        # address input
        self.entry_address = Text(self.bottom, width=35, height=10)
        self.entry_address.place(x=170, y=242)

        # button
        add_button = Button(self.bottom, text="Add Person", command=self.add_people)
        add_button.place(x=170, y=450)

    def add_people(self):
        name = self.entry_name.get()
        surname = self.entry_surname.get()
        email = self.entry_email.get()
        phone = self.entry_phone_number.get()
        address = self.entry_address.get(1.0, "end-1c")
        if name and surname and email and phone and address != "":
            # query_create = "CREATE TABLE contacts ( person_id INTEGER PRIMARY KEY, person_name TEXT NOT NULL,
            # person_surname TEXT NOT NULL, person_email TEXT NOT NULL UNIQUE, person_phone TEXT NOT NULL UNIQUE,
            # person_address TEXT NOT NULL UNIQUE );" query="INSERT INTO contacts (person_id, person_name,
            # person_surname, person_email, person_phone, person_address) VALUES()"
            try:
                # query_create = "CREATE TABLE contacts ( person_id INTEGER PRIMARY KEY, person_name TEXT NOT NULL,
                # " \ "person_surname TEXT NOT NULL, person_email TEXT NOT NULL UNIQUE, person_phone TEXT NOT " \
                # "NULL UNIQUE, person_address TEXT NOT NULL UNIQUE ); " cursor.execute("DROP TABLE contacts;")
                # cursor.execute(query_create)
                # data = cursor.execute("SELECT * FROM contacts")
                # for i in data:
                #     print(i)
                # messagebox.showinfo("Success", "Table  added")
                query = "INSERT INTO 'contacts' (person_name, person_surname, person_email, person_phone, " \
                        "person_address) VALUES(?,?,?,?,?)"
                cursor.execute(query, (name, surname, email, phone, address))
                messagebox.showinfo("Success", "Contact added")
                conn.commit()
                self.destroy()
            except EXCEPTION as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showerror("Error", "Fill all the fields", icon="warning")
