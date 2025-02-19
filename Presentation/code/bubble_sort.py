def bubble_sort(array):
    unsorted_until_index = len(array) - 1
    sorted = False
    
    while not sorted:
        sorted = True
        for i in range(unsorted_until_index):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                sorted = False
        unsorted_until_index -= 1
    
    return array


print(bubble_sort([65, 55, 45, 35, 25, 15, 10]))
