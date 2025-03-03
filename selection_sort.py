def selection_sort(arr: list[int]) -> list[int]:
    """
    Сортировка выбором
    O(n**2)
    :param arr: массив
    :return: отсортированный массив
    """
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[min_index], arr[i] = arr[i], arr[min_index]
    return arr

s = [400, 200, 100, 40, 50]
print(selection_sort(s))