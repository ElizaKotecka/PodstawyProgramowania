# Sorts an array of numbers using the bubble sort algorithm.


def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1): #outer loop - how many passes have been completed
        for j in range(n-i-1): #inner loop for comparing and swaping elements; -1 ensures that j+1 is within bounds;
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

if __name__ == '__main__':
    car_fuel_consumption = [7.2, 6.8, 7.5, 7.0, 7.1, 6.9, 7.3]
    bank_transactions = [-150, -20, 300, -45, -60, 500, -120]

    print(bubbleSort(car_fuel_consumption))
    print(bubbleSort(bank_transactions))
