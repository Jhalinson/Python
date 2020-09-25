from tkinter import Toplevel, PhotoImage, Label, X, Frame, Entry, Button, Text, messagebox
import sqlite3

conn = sqlite3.connect('phonebook.db')
cursor = conn.cursor()


class UpdatePeople(Toplevel):

    def __init__(self, person_id):
        Toplevel.__init__(self)

        # window to update
        self.geometry("650x650+600+200")
        self.title("Update Person")
        self.resizable(False, False)
        # query update
        query = "Select * FROM contacts where person_id='{}'".format(person_id)
        print(person_id)
        result = cursor.execute(query).fetchone()
        print(result)
        self.person_id = person_id
        person_name = result[1]
        person_surname = result[2]
        person_email = result[3]
        person_phone = result[4]
        person_address = result[5]

        self.top = Frame(self, height=150, bg='white')
        self.top.pack(fill=X)
        self.bottom = Frame(self, height=500, bg="#fcba03")
        self.bottom.pack(fill=X)
        self.top_image = PhotoImage(file="C:\\Users\\jhali\\Desktop\\Python\\Icons\\update.png")
        self.top_image_label = Label(self.top, image=self.top_image)
        self.top_image_label.place(x=180, y=35)
        self.heading = Label(self.top, text="Update Person", font="arial 15 bold", bg="white", fg="#34baeb")
        self.heading.place(x=260, y=60)

        # All labels and inputs
        # name label
        self.label_name = Label(self.bottom, text="Name:", font="arial 15 bold", fg="black", bg="#e6e2da")
        self.label_name.place(x=49, y=40)
        # name input
        self.entry_name = Entry(self.bottom, width=30, bd=4)
        self.entry_name.insert(0, person_name)
        self.entry_name.place(x=170, y=42)

        # surname label
        self.last_surname = Label(self.bottom, text="Surnames:", font="arial 15 bold", fg="black", bg="#e6e2da")
        self.last_surname.place(x=49, y=90)
        # surname  input
        self.entry_surname = Entry(self.bottom, width=30, bd=4)
        self.entry_surname.insert(0, person_surname)
        self.entry_surname.place(x=170, y=92)

        # email label
        self.email_label = Label(self.bottom, text="Email:", font="arial 15 bold", fg="black", bg="#e6e2da")
        self.email_label.place(x=49, y=140)
        # email  input
        self.entry_email = Entry(self.bottom, width=30, bd=4)
        self.entry_email.insert(0, person_email)
        self.entry_email.place(x=170, y=142)

        # phone number label
        self.phone_number_label = Label(self.bottom, text="Phone #:", font="arial 15 bold", fg="black", bg="#e6e2da")
        self.phone_number_label.place(x=49, y=190)
        # phone number  input
        self.entry_phone_number = Entry(self.bottom, width=30, bd=4)
        self.entry_phone_number.insert(0, person_phone)
        self.entry_phone_number.place(x=170, y=192)

        # address label
        self.address_label = Label(self.bottom, text="Address:", font="arial 15 bold", fg="black",
                                   bg="#e6e2da")
        self.address_label.place(x=49, y=240)
        # address input
        self.entry_address = Text(self.bottom, width=35, height=10)
        self.entry_address.insert(1.0, person_address)
        self.entry_address.place(x=170, y=242)

        # button
        add_button = Button(self.bottom, text="Update Person", command=self.update_people)
        add_button.place(x=170, y=450)

    def update_people(self):
        person_id = self.person_id
        name = self.entry_name.get()
        surname = self.entry_surname.get()
        email = self.entry_email.get()
        phone = self.entry_phone_number.get()
        address = self.entry_address.get(1.0, "end-1c")
        query = "UPDATE contacts set person_name = '{}', person_surname = '{}', person_email = '{}', person_phone = " \
                "'{}', person_address = '{}' where person_id = '{}'".format(name, surname, email, phone, address,
                                                                            person_id)
        try:
            cursor.execute(query)
            conn.commit()
            messagebox.showinfo("Success", "Contact Updated")
            self.destroy()
        except Exception as e:
            print(e)
