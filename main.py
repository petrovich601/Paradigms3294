
# Задача №1
# Дан список целых чисел numbers. Необходимо написать в императивном стиле процедуру для
# сортировки числа в списке в порядке убывания. Можно использовать любой алгоритм сортировки.

# Императивный стиль
arr = [4, 7, 2, 11, 1, 3, 2]
n = len(arr)
for i in range(n):
    for j in range(n - i - 1):
        if arr[j] < arr[j + 1]:
            tmp = arr[j + 1]
            arr[j + 1] = arr[j]
            arr[j] = tmp
print(arr)

# Декларативный стиль
def my_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] < arr[j + 1]:
                tmp = arr[j + 1]
                arr[j + 1] = arr[j]
                arr[j] = tmp
    return arr

my_array = [4, 7, 2, 12, 1, 3, 34]
new_array = my_sort(my_array)
print(new_array)