def find_min(array):
    minimum = array[0]
    for elem in array:
        if elem < minimum:
            minimum = elem
    print("The minimum of the list is: ", minimum)


def find_avg(array):
    total = 0
    for elem in array:
        total += elem
    print("The average of the list is: ", total/len(array))

# Example
arr = [6, 7, 2, 1, 8]
find_min(arr)
find_avg(arr)
