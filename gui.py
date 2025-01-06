from tkinter import *
from tkinter import messagebox
from datetime import datetime 
from data_structure import NODE, QUEUE


class GUI():
    def __init__(self, root):
        self.queue = QUEUE()
        self.root = root
        self.root.title('Restaurant Booking')
        self.root.geometry('600x500')
        self.root.configure(bg="#f0f8ff")  # Light blue background

        # Heading
        self.heading = Label(self.root, text="Restaurant Booking System", font=('Helvetica', 26, 'bold'), bg="#f0f8ff", fg="#2e8b57")
        self.heading.pack(pady=20)

        # Frame 1: Name Input
        self.frame1 = Frame(self.root, bg="#f0f8ff")
        self.frame1.pack(padx=20, pady=10)

        self.name_label = Label(self.frame1, text='Enter Name:', font=('Helvetica', 14), bg="#f0f8ff")
        self.name_label.grid(row=0, column=0, padx=10, pady=5)

        self.name_value = StringVar()
        self.name_enter = Entry(self.frame1, textvariable=self.name_value, font=('Helvetica', 14), width=25)
        self.name_enter.grid(row=0, column=1, padx=10, pady=5)

        # Frame 2: People Count
        self.frame2 = Frame(self.root, bg="#f0f8ff")
        self.frame2.pack(padx=20, pady=10)

        self.people_label = Label(self.frame2, text="Number of People:", font=('Helvetica', 14), bg="#f0f8ff")
        self.people_label.grid(row=0, column=0, padx=10, pady=5)

        self.people_count = IntVar()
        self.people_count.set(0)
        self.people_enter = Entry(self.frame2, textvariable=self.people_count, font=('Helvetica', 14), width=10)
        self.people_enter.grid(row=0, column=1, padx=10, pady=5)

        # Frame 3: Buttons
        self.frame3 = Frame(self.root, bg="#f0f8ff")
        self.frame3.pack(pady=20)

        self.button_add = Button(self.frame3, text="Add Booking", command=self.add_booking, font=('Helvetica', 12, 'bold'), bg="#4682b4", fg="white", padx=10, pady=5)
        self.button_add.grid(row=0, column=0, padx=15)

        self.button_process = Button(self.frame3, text="Process Booking", command=self.process_booking, font=('Helvetica', 12, 'bold'), bg="#4682b4", fg="white", padx=10, pady=5)
        self.button_process.grid(row=0, column=1, padx=15)

        self.button_view = Button(self.frame3, text="View Bookings", command=self.view_bookings, font=('Helvetica', 12, 'bold'), bg="#4682b4", fg="white", padx=10, pady=5)
        self.button_view.grid(row=0, column=2, padx=15)

        # Feedback Area
        self.bookings = Label(self.root, text="No bookings yet!", font=('Helvetica', 14), bg="#f0f8ff", fg="#ff4500", relief="ridge", width=50, height=8)
        self.bookings.pack(pady=25)

    def add_booking(self):
        try:
            name = self.name_value.get()
            people = self.people_count.get()

            if name == "" or people <= 0:
                return messagebox.showwarning(title="Input Error", message="Please enter a valid name and number of people!")

            booking_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Current timestamp

            self.queue.Enqueue(name, people, booking_time)
            messagebox.showinfo(title="Success", message=f"Your booking is successfully added at {booking_time}!")
            self.name_value.set("")
            self.people_count.set(0)
            self.view_bookings()
        except Exception as e:
            messagebox.showwarning(title="Error", message=str(e))

    def process_booking(self):
        if self.queue.is_empty():
            return messagebox.showinfo(title="No Bookings", message="No bookings to process!")
        self.queue.Dequeue()
        messagebox.showinfo(title="Success", message="Booking processed successfully!")
        self.view_bookings()

    def view_bookings(self):
        self.show_bookings()

    def show_bookings(self):
        if self.queue.is_empty():
            self.bookings.config(text="No bookings in queue!")
        else:
            self.bookings.config(text='\n'.join(self.queue.Print_test()))
