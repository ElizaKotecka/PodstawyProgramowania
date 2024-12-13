# Create a program that sorts elements of an array containing integer numbers. 
# Apply the Bubble Sort sorting algorithm. 
# Define a function bubblesort(array) that returns the sorted array. 
# Try to sort and print any three arrays.

def bubblesort(arr):
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


arr = [1, 6, 3, 7, 3, 1]
print(f'Array: {arr}')
print(f'Sorted array: {bubblesort(arr)}')