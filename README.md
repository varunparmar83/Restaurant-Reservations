# Restaurant-Reservations
Restaurant Booking System with Queue Implementation
Overview
This project is a simple Restaurant Booking System implemented in Python using Tkinter for the graphical user interface (GUI). It leverages the queue data structure to manage customer bookings in a first-come-first-serve manner.

Features
Add bookings with a customer name and the number of people.
Process bookings in the order they were added (FIFO - First In, First Out).
View the current list of bookings dynamically.
Intuitive GUI for interacting with the system.
How it Works
The system uses a custom QUEUE class, which is implemented using linked nodes (NODE).

Each booking is represented as a NODE containing:

The name of the customer.
The number of people for the booking.
The QUEUE class provides:

Enqueue: Adds a booking to the queue.
Dequeue: Processes and removes the first booking from the queue.
is_empty: Checks if the queue is empty.
Print_test: Prints all bookings in the queue.
The GUI is built using Tkinter, featuring input fields for the name and the number of people, along with buttons for adding, processing, and viewing bookings.

GUI Components
Input Fields:
Name: Text input for the customer's name.
Number of People: Numeric input for the group size.
Buttons:
Add Booking: Adds a new booking to the queue.
Process Booking: Removes the first booking from the queue.
Booking List Display: Shows all current bookings dynamically
