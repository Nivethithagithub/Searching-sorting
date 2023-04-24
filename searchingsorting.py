#1)Implement Binary Search
def binary_search(array, target):
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
#2)Implement Merge Sort
def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result
#3)Implement Quick Sort
def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = array[0]
    left = []
    right = []
    for element in array[1:]:
        if element < pivot:
            left.append(element)
        else:
            right.append(element)
    return quick_sort(left) + [pivot] + quick_sort(right)
#4)Implement Insertion Sort
def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array
#5)Write a program to sort list of strings (similar to that of dictionary)
my_list = ['banana', 'apple', 'pear', 'orange']
sorted_list = sorted(my_list)
print(sorted_list)

my_list = ['banana', 'apple', 'pear', 'orange']
sorted_list = sorted(my_list, key=lambda s: len(s))
print(sorted_list)

    
