# An app that lets you choose and book available hotels,
# makes you pay and displays a receipt

import pandas as pd
import time

# "dtype" allows to convert only the "ID" column into strings
df_hotels = pd.read_csv('hotels.csv', dtype={'ID': str})
# Simulate the Paying app's database to validate the user's credit card
# Saved as a dictionary to make the comparison easier
df_cards = pd.read_csv('cards.csv',
                       dtype=str).to_dict(orient='records')


class Hotel:
    def __init__(self, hotel_id):
        self.id = hotel_id
        # "name" isn't added as a parameter because it's calculated from
        # the Dataframe, not given by the user as "hotel_id".
        self.name = df_hotels.loc[df_hotels['ID'] == self.id, 'NAME'].squeeze()

    def book(self):
        """Book a hotel by changing its availability to no"""
        df_hotels.loc[df_hotels['ID'] == self.id, 'AVAILABLE'] = 'no'
        # Writes the df (without index) back to the csv file
        df_hotels.to_csv('hotels.csv', index=False)

    def is_available(self):
        """Checks if the hotel is available"""
        availability = df_hotels.loc[df_hotels['ID'] == self.id,
                                     'AVAILABLE'].squeeze()
        if availability == 'yes':
            return True
        else:
            return False


class ReservationTicket:
    def __init__(self, customer_name, hotel_instance):
        self.cust_name = customer_name
        self.hotel = hotel_instance

    def generate(self):
        content = '\n' * 10 + f"""
Thank you for your reservation ! 
Here is the related information:

Name: {self.cust_name}
Hotel name: {self.hotel.name}
"""
        return content


class CreditCard:
    def ask_card_info(self):
        number = input("Please enter your credit card number (1234): ")
        time.sleep(1)
        expiration = input('Enter the expiration data (12/26): ')
        time.sleep(1)
        cvc = input('Enter the cvc code (123): ')
        time.sleep(1)
        holder = input("Enter the card holder's name (JOHN SMITH): ")
        time.sleep(3)
        card_info = {'number': number, 'expiration': expiration, 'cvc': cvc,
                     'holder': holder}
        return card_info

    def validate(self, card_info):
        if card_info in df_cards:
            return True


# Loop to restart once a hotel has been booked
while True:
    print(df_hotels.to_string(index=False))
    print('-' * len(df_hotels.columns) * 12 + '\n')

    # Loop to ask again for the hotel ID if it wasn't entered correctly
    while True:
        hotel_ID = input('Enter the id of the hotel: ')
        if hotel_ID in df_hotels['ID'].values:
            break
        else:
            print("\nInvalid hotel ID. Please enter a valid one.\n")
            time.sleep(2)

    hotel = Hotel(hotel_ID)

    if hotel.is_available():
        name = input('Enter your name: ')

        credit_card = CreditCard()
        print('\nThe room needs to be paid in advanced '
              'in order to be booked.\n')

        # Loop to ask again for the credit card info if it wasn't correct
        while True:
            card_info = credit_card.ask_card_info()

            if credit_card.validate(card_info):
                break
            else:
                print("\nThe credit card information isn't valid. "
                      "Please try again")
                time.sleep(3)
                print('\n' * 10)

        hotel.book()
        reservation_ticket = ReservationTicket(customer_name=name,
                                               hotel_instance=hotel)
        print(reservation_ticket.generate())
        time.sleep(10)
        print('\n' * 5)

    else:
        print("\nThere aren't any room available for this hotel, please "
              "choose another one")
        time.sleep(4)
        print('\n' * 5)
