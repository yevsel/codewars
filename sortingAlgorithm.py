

class SortArray:

    def descending_order(arr):
        array = arr
        for i in range(len(array)-1):
            for j in range(len(array)-1):
                if array[j] < array[j+1]:
                    array[j], array[j+1] = array[j+1], array[j]
        return array

    def ascending_order(arr):
        array = arr
        for i in range(len(array)-1):
            for j in range(len(array)-1):
                if array[j] > array[j+1]:
                    array[j], array[j+1] = array[j+1], array[j]
        return array


my_array = [5, 4, 2, 7, 8, 2, 1]

print(SortArray.descending_order(my_array))


print(SortArray.ascending_order(my_array))
