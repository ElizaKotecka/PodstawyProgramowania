# Sorts an array of numbers using the bubble sort algorithm.


def bubbleSort(arr):
    n = len(arr)
    # outer loop - how many passes have been completed; n-1 - za ostatnim razem zostaje jeden element do posortowania (na początku) i tablica posortowana
    for i in range(n-1):
        # inner loop for comparing and swaping elements;
        # n-i: ostatnie i elementow jest posortowane,
        # -1: żeby nie porównywało osttaniego nieposorotwanego z posorotowanym po nim (przy i=0 zapobiega błędowi porownania ostatniego elementu z nieistniejacym po nim [j+1])
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

if __name__ == '__main__':
    car_fuel_consumption = [7.2, 6.8, 7.5, 7.0, 7.1, 6.9, 7.3]
    bank_transactions = [-150, -20, 300, -45, -60, 500, -120]

    print(bubbleSort(car_fuel_consumption))
    print(bubbleSort(bank_transactions))
