# Create a program that sorts elements of an array containing integer numbers. 
# Apply the Bubble Sort sorting algorithm. 
# Define a function bubblesort(array) that returns the sorted array. 
# Try to sort and print any three arrays.

def bubblesort(array):
    lenght = len(array)
    for _ in range(lenght):
        for i in range(lenght-1):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
    return array


arr = [1, 6, 3, 7, 3, 1]
print(f'Array: {arr}')
print(f'Sorted array: {bubblesort(arr)}')