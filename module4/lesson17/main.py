def insertion_sort(arr):
    for i in range(1, len(arr)):
        elem = arr[i]
        j = i
        while j > 0 and arr[j-1] > elem:
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = elem


# Пример использования:
my_list = [64, 34, 25, 12, 22, 11, 90]
insertion_sort(my_list)
print("Отсортированный список:", my_list)

my_list2 = list(range(99, 0, -2))
insertion_sort(my_list2)
print("Отсортированный список:", my_list2)