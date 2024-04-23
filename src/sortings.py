# from element_search import load_transaction_blocks

def bubble_sort(array):
    for _ in range(len(array)):
        counter = 0

        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]

                counter += 1

        if counter == 0:
            return array


def selection_sort(array):
    for j in range(len(array) - 1):
        min_index = j
        for i in range(j + 1, len(array)):
            if array[i] < array[min_index]:
                min_index = i
        array[j], array[min_index] = array[min_index], array[j]

    return array
