def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    grater = [i for i in array[1:] if i > pivot]
    return quick_sort(less) + [pivot] + quick_sort(grater)

print(quick_sort([14, 33, 41, 15, 77, 83, 32]))