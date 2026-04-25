'''
Hotel Reservation System - Spring 2026

Author: Aashna Sharma

This program is a hotel reservation system where it prompts the user for information
such as room type, age, nights stayed, and first and last name and stores them in a dictionary.
It then calculates the nightly rate based on if there is a college or senior discount and calculates the total cost.

I have neither given or received unauthorized assistance on this assignment.
Signed: Aashna Sharma
'''
import random

def calculate_discounted_rate(rate, age):
    '''Calculates and returns the discounted nightly rate based on the guest's age.'''
    if age < 22:
        rate = rate - (rate * 0.10)
    elif age > 64:
        rate = rate - (rate * 0.15)
    return rate


def calculate_reservation_total(room_type, nights, age):
    '''Calculates and returns the total reservation cost.'''
    stand_rate = determine_standard_rate(room_type)
    disc_rate = calculate_discounted_rate(stand_rate, age)
    subtotal = disc_rate * nights
    tax = subtotal * 0.06
    total = subtotal + tax
    return total


def determine_standard_rate(room_type):
    '''Returns the standard rate based on room type.'''
    room_rates = {
        "single": 100.0,
        "double": 125.0,
        "king": 150.0,
        "suite": 200.0
    }
    return room_rates[room_type]


def create_reservation(all_reservations):
    '''Prompts user for reservation info and returns it.'''
    print('--------------------------------------------------')
    print('\nCreating new reservation...')

    first_name = input("What is the guest's first name?")
    last_name = input("What is the guest's last name?")

    room_type = ''
    rooms = ['single', 'double', 'king', 'suite']
    while room_type not in rooms:
        room_type = input("What room type do you want? Single, double, king, or suite? ").lower()

    num_nights = int(input("How many nights?"))
    age = int(input("What is the age of the primary guest?"))
    
    r_id = get_new_reservation_id(all_reservations)
    reservation = [first_name, last_name, room_type, num_nights, age]
    all_reservations[r_id] = reservation
    
    total_cost = calculate_reservation_total(room_type, num_nights, age)
    print(f"The cost of this reservation for {first_name} {last_name} is ${total_cost:.2f}.")
    print(f"The reservation ID is {r_id}")
    print('--------------------------------------------------')

    return all_reservations


def view_reservations(all_reservations):
    '''Prints all reservations.'''
    if len(all_reservations) != 0:
        print("Current reservations:\n")
        for r_id in all_reservations:
            reservation = all_reservations[r_id]
            first_name, last_name, room_type, num_nights, age = reservation
            print(f"Reservation ID: {r_id}")
            print(f"Guest: {first_name} {last_name} (age {age})")
            print(f"Room type: {room_type}")
            print(f"Number of nights: {num_nights}\n")
    else:
        print("No reservations found.")


def save_reservations(all_reservations):
    '''Saves reservations to a file.'''
    try:
        with open("reservations.txt", "w") as file:
            for r_id in all_reservations:
                reservation = all_reservations[r_id]
                first_name, last_name, room_type, num_nights, age = reservation
                file.write(f"{r_id} {first_name} {last_name} {room_type} {num_nights} {age}\n")
        print("Data saved successfully.")
    except:
        print("There was an error saving the data.")


def load_reservations():
    '''Loads reservations from file.'''
    all_reservations = {}
    
    try:
        with open("reservations.txt", "r") as file: 
             for line in file:
                parts = line.strip().split()
                r_id = parts[0]
                first_name = parts[1]
                last_name = parts[2]
                room_type = parts[3]
                num_nights = int(parts[4])
                age = int(parts[5])

                all_reservations[r_id] = [first_name, last_name, room_type, num_nights, age]

        print("Data loaded successfully")
    except:
        print("There was an error loading the data.")
        return {}

    return all_reservations

def get_new_reservation_id(all_reservations):
    '''Creates a new ID for the reservation, returns if the ID isn't already in all reservations'''
    while True:
        num = random.randint(100, 999)
        new_id = f"PHS-734-{num}"
        if new_id not in all_reservations:
            return new_id
    
def edit_reservation(all_reservations):
    '''Prompts user for a reservation ID and updates the room type and number of nights. Parameter is all_reservations.
        Returns possibly modified dictionary'''
    
    r_id = input("Enter the reservation ID you wish to edit: ")
    if r_id not in all_reservations:
        print("That reservation ID does not exist.")
        return all_reservations
    
    print("Modifying reservation:")
    
    rooms = ['single', 'double', 'king', 'suite']
    room_type = ''
    while room_type not in rooms:
        room_type = input("What type of room (single, double, king, suite)? ").lower()
        
    num_nights = int(input("How many nights? "))
    
    all_reservations[r_id][2] = room_type
    all_reservations[r_id][3] = num_nights
    
    total_cost = calculate_reservation_total(room_type, num_nights, all_reservations[r_id][4])
    print(f"\nThe updated cost of this reservation is ${total_cost:.2f}")
    
    return all_reservations
    
def delete_reservation(all_reservations):
    '''Asks user for the reservation ID and deletes it from the dictionary if valid. Parameter is all_reservations.
        Returns possibly modified dictionary'''
    r_id = input("Enter reservation ID: ")
    
    if r_id not in all_reservations:
        print("That reservation ID does not exist.")
        return all_reservations
    
    del all_reservations[r_id]
    print("That reservation has been deleted.")
    
    return all_reservations
        

def print_menu():
    print("Select an option from the following menu:")
    print("1. Create a reservation")
    print("2. View reservations")
    print("3. Edit reservations")
    print("4. Delete reservations")
    print("5. Save reservations")
    print("6. Load reservations")
    print("7. Exit the program")


def main():
    print("Welcome to the Python hotel reservation system!\n")

    all_reservations = {}

    while True:
        print_menu()
        try:
            num = int(input("What is your selection?"))
        except:
            print("Invalid choice. Please try again.")
            continue

        if num == 1:
            all_reservations = create_reservation(all_reservations)
        elif num == 2:
            view_reservations(all_reservations)
        elif num == 3:
            all_reservations = edit_reservation(all_reservations)
        elif num == 4:
            all_reservations = delete_reservation(all_reservations)
        elif num == 5:
            save_reservations(all_reservations)
        elif num == 6:
            all_reservations = load_reservations()
        elif num == 7:
            print("Now exiting program. Thanks for visiting!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    main()
