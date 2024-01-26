# Personal Learning Project

This project was developed as part of my journey to learn Python. It is intended for personal use and as a learning exercise. You're welcome to explore the code, and free to use it as inspiration for your own learning projects.
<br>
<br>
I'd like to thank Ardit Sulce, whose excellent course I had the opportunity to follow on Udemy.com ('Python Mega Course: Learn Python in 60 Days, Build 20 Apps').
<br>
<br>

## Hotel Booking and Reservation System

A Python command-line based app that allows users to choose and book available hotels, make payments, and receive a reservation receipt. 
The program uses pandas for data manipulation and reading CSV files to manage hotel information, credit card details, and user credentials.

## Usage

1. **Run the Python program:**
    ```bash
    main.py
    ```

2. **Follow the command-line prompts to select a hotel, provide your details, and complete the reservation process.**

## Features

- **Hotel Class:** Represents a hotel with methods to book and check availability.
- **ReservationTicket Class:** Generates a reservation ticket with customer information.
- **SpaTicket Class:** Inherits from ReservationTicket and generates a spa reservation ticket.
- **CreditCard Class:** Manages credit card information, prompts users for details, and validates the card.
- **Authentication Class:** Inherits from CreditCard and provides a login system with credit card number and password.
