# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(len(arr)):
        smallest_index = i
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(i + 1, len(arr)):
            if(arr[smallest_index] > arr[j]):
                smallest_index = j
        # TO-DO: swap
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
    return arr


test = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
print(selection_sort(test))


# TO-DO:  implement the Bubble Sort function below

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if (arr[j] > arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr


print(bubble_sort(test))

# STRETCH: implement the Count Sort function below


def count_sort(arr, maximum=-1):

    return arr
