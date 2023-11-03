import pandas as pd

# "dtype" allows to convert only the "ID" column intro strings
df = pd.read_csv('hotels.csv', dtype={'ID': str})


class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        # "name" isn't added as a parameter because it's calculated from
        # the Dataframe, not given by the user as "hotel_id".
        self.name = df.loc[df['ID'] == self.hotel_id, 'NAME'].squeeze()

    def book(self):
        """Book a hotel by checking its availability to no"""
        df.loc[df['ID'] == self.hotel_id, 'AVAILABLE'] = 'no'
        # Writes the df (without index) back to the csv file
        df.to_csv('hotels.csv', index=False)

    def is_available(self):
        """Checks if the hotel is available"""
        availability = df.loc[df['ID'] == self.hotel_id,
                              'AVAILABLE'].squeeze()
        if availability == 'yes':
            return True
        else:
            return False


class ReservationTicket:
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self):
        content = f"""
Thank you for your reservation ! 
Here is the related information:

Name: {self.customer_name}
Hotel name: {self.hotel.name}
"""
        return content


print(df.to_string(index=False))
print('-' * len(df.columns) * 12 + '\n')
hotel_ID = input('Enter the id of the hotel: ')
hotel = Hotel(hotel_ID)

if hotel.is_available():
    name = input('Enter your name: ')
    hotel.book()
    reservation_ticket = ReservationTicket(customer_name=name,
                                           hotel_object=hotel)
    print(reservation_ticket.generate())
else:
    print('Hotel is not free')
