# type 01 - search for target
def binary_search_iterative(arr, target):
    l = 0
    r = len(arr)-1
    while l <= r:
        mid = (l+r)//2
        if arr[mid] < target :
            l = mid + 1
        elif arr[mid] > target:
            r = mid - 1
        else:
            return mid
    # End Condition: left > right
    return -1

# type 01 - recursive
def binary_search_helper(arr, target, l , r):
    if l <= r:
        mid = (l+r)//2
        if arr[mid] < target:
            binary_search_helper(arr, target, mid+1, r)
        elif arr[mid] > target:
            binary_search_helper(arr, target, l, mid-1)
        else:
            return mid
    else:
        return -1

def binary_search_recursive(arr, target):
    return binary_search_helper(arr, target, 0, len(arr)-1)

# The function calls the bisect_left() function of the bisect module which finds
# the position of the element in the sorted array arr where x should be inserted to
# maintain the sorted order. If the element is already present in the array, this
# function will return its position.
import bisect

def binary_search_with_bisect(arr, target):
    index = bisect.bisect_left(arr, target)
    # element found
    if arr[index] == target:
        return index
    else:
        return -1





