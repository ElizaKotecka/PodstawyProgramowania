
#   1) A function that returns the second largest element in an array
#   2) A function that returns the difference between the largest and smallest values in an array
#   3) A function that returns the median of numbers in an array.
#   4) A function that returns a two-element array containing the smallest and largest values in an array
#   5) A function that returns array elements as a string, separated by the minus sign

def second_largest(arr):
    largest, second_largest = arr[0], arr[0]
    for i in arr:
        if i > largest:
            second_largest = largest
            largest = i
        elif i > second_largest:
            second_largest = i
    return second_largest

def difference(arr):
    smallest, largest = smallest_largest(arr)
    return largest - smallest

def median(arr):
    # arr_sorted = bubblesort(arr)
    arr_sorted = sorted(arr) #zwraca posortowaną kopię
    lenght = len(arr_sorted)
    if lenght % 2 == 0:
        return (arr_sorted[lenght//2-1] + arr_sorted[lenght//2]) / 2
    else:
        return arr_sorted[lenght//2]

def smallest_largest(arr):
    largest, smallest = arr[0], arr[0]
    for i in arr:
        if i > largest:
            largest = i
        elif i < smallest:
            smallest = i
    return [smallest, largest]

def arr_to_str(arr):
    result = ''
    for i in arr:
        result += str(i) + '-'
    return result[:-1]








# # from 3.11.py
# def bubbleSort(arr):
#     arr = arr.copy() # to not change the orginal array
#     n = len(arr)
#     # outer loop - how many passes have been completed; n-1 - za ostatnim razem zostaje jeden element do posortowania (na początku) i tablica posortowana
#     for i in range(n-1):
#         # inner loop for comparing and swaping elements;
#         # n-i: ostatnie i elementow jest posortowane,
#         # -1: żeby nie porównywało osttaniego nieposorotwanego z posorotowanym po nim (przy i=0 zapobiega błędowi porownania ostatniego elementu z nieistniejacym po nim [j+1])
#         for j in range(n-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#     return arr