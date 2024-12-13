# Define a function compare(array1, array2) 
# that returns True if both arrays are the same or False otherwise. 
# Two arrays are the same if they have the same number of elements 
# and values of elements in cells of arrays with the same index are equal. 
# Then create a program and try to compare the following arrays:

def compare(array1, array2):
    if len(array1) == len(array2):
        for elem in range(len(array1)):
            if array1[elem] == array2[elem]:
                continue
            else:
                return False
        return True
    return False

def main():
    arr1 = ["water","book","sky"]
    arr2 = ["water","book","sky"]
    arr3 = [5,3,1]
    arr4 = [5,3,1]
    arr5 = [True,False]
    arr6 = [True,False,True]
    arr7 = [3,2,1]
    arr8 = [3,2]

    print(f'Array1: ', end= '')
    for elem in arr7:
        print(f'{elem}', end = ' ')

    print()

    print(f'Array2: ', end= '')
    for elem in arr8:
        print(f'{elem}', end = ' ')
    
    print()

    if compare(arr7, arr8):
        print('Comparison: arrays are the same')
    else:
        print('Comparison: arrays are not the same.')


if __name__ == '__main__':
    main()


    