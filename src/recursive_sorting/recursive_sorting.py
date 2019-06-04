# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    merged_arr = []

    for i in range(len(arrA) + len(arrB)):
        if len(arrA) == 0:
            merged_arr += arrB
            break
        elif len(arrB) == 0:
            merged_arr += arrA
            break
        elif arrA[0] > arrB[0]:
            merged_arr.append(arrB.pop(0))
        else:
            merged_arr.append(arrA.pop(0))
    return merged_arr

# TO-DO: implement the Merge Sort function below USING RECURSION


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left = merge_sort(arr[0:mid])  # Dividing the array elements
        right = merge_sort(arr[mid:])  # into 2 halves

        # Merge sorted pieces together
        arr = merge(left, right)

    return arr

# STRETCH: implement an in-place merge sort algorithm


print(merge_sort([3, 4, 7, 8, 10]))


def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
