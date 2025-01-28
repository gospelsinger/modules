def bubble_sort(arr):
    for j in range(len(arr)-1, 0, -1):
        for i in range(j):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]


# Пример использования:
my_list = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(my_list)
print("Отсортированный список:", my_list)

my_list2 = [5, 4, 3, 2, 1]
bubble_sort(my_list2)
print("Отсортированный список:", my_list2)