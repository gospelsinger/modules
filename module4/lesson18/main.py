def selection_sort(arr):
    for i in range(len(arr)-1):
        min_position = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_position]:
                min_position = j
        arr[i], arr[min_position] = arr[min_position], arr[i]


# Пример использования:
my_list = [64, 34, 25, 12, 22, 11, 90]
selection_sort(my_list)
print("Отсортированный список:", my_list)

my_list2 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
selection_sort(my_list2)
print("Отсортированный список:", my_list2)

my_list3 = [12, 6, 4, 7, 9, 15, 14, 8, 11, 1, 10, 2, 13, 5, 3]
selection_sort(my_list3)
print("Отсортированный список:", my_list3)