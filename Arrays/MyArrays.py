# Create a module MyArrays containing functions  to operate on an array of numbers:
#   1) A function that returns the second largest element in an array
#   2) A function that returns the difference between the largest and smallest values in an array
#   3) A function that returns the median of numbers in an array.
#   4) A function that returns a two-element array containing the smallest and largest values in an array
#   5) A function that returns array elements as a string, separated by the minus sign
# Do not use built-in functions. 
# The median is the middle value in the ordered sequence of numbers:
# https://en.wikipedia.org/wiki/Median#/media/File:Finding_the_median.png

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
    largest, smallest = arr[0], arr[0]
    for i in arr:
        if i > largest:
            largest = i
        elif i < smallest:
            smallest = i
    return largest - smallest

# from 3.11.py
def bubblesort(array):
    array = array.copy() # to not change the original array
    lenght = len(array)
    for _ in range(lenght):
        for i in range(lenght-1):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
    return array


def median(arr):
    arr_sorted = bubblesort(arr)
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
