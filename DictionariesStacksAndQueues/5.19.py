import json

def nb_of_reserved_rooms(reservations):
    return len(reservations)

def nb_of_paid_reservations(reservations):
    counter = 0
    for element in reservations:
        if element['paid'] == True:
            counter += 1
    return counter

def nb_of_unpaid_reservations(reservations):
    return  nb_of_reserved_rooms(reservations) - nb_of_paid_reservations(reservations)

def total_paid(reservations):
    total = 0
    for element in reservations:
        if element['paid'] == True:
            total += element['price_per_night'] * element['nights']
    return total

def total_unpaid(reservations):
    total = 0
    for element in reservations:
        if element['paid'] == False:
            total += element['price_per_night'] * element['nights']
    return total


if __name__=='__main__':

    with open('reservations.json', 'r') as f:
        file = json.load(f)
        reservations = file['reservations']

    print(f"Number of rooms: {nb_of_reserved_rooms(reservations)}")
    print(f"Number of paid reservations: {nb_of_paid_reservations(reservations)}")
    print(f"Number of unpaid reservations: {nb_of_unpaid_reservations(reservations)}")
    print(f"Total value of paid reservations: {total_paid(reservations)}")
    print(f"Total value of unpaid reservations: {total_unpaid(reservations)}")



