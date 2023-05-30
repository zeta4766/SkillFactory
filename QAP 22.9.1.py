def check(num): #Проверка корректности ввода последовательности чисел
    for i in num:
        if not i.isdigit():
            return False
    else:
        return True


def merge_sort(L):  # "разделяй"
    if len(L) < 2:  # если кусок массива меньше 2,
        return L[:]  # выходим из рекурсии
    else:
        middle = len(L) // 2  # ищем середину
        left = merge_sort(L[:middle])  # рекурсивно делим левую часть
        right = merge_sort(L[middle:])  # и правую
        return merge(left, right)  # выполняем слияние


def merge(left, right):  # "властвуй"
    result = []  # результирующий массив
    i, j = 0, 0  # указатели на элементы

    # пока указатели не вышли за границы
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # добавляем хвосты
    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result


def binary_search(array, element, left, right):
    if left > right:  # если левая граница превысила правую,
        return False  # значит элемент отсутствует

    middle = (right + left) // 2  # находим середину
    if array[middle] == element:  # если элемент в середине,
        return middle  # возвращаем этот индекс
    elif element < array[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(array, element, left, middle - 1)
    else:  # иначе в правой
        return binary_search(array, element, middle + 1, right)

while True: #Пока пользователь не введёт корректные данные, программа не будет выполняться
    print('Введите последовательность чисел, разделённых пробелами:')
    numbers = input().split()
    print('Введите число:')
    n = input()
    if not (check(numbers) or n.isdigit()):
        print('Данные введены неправильно')
        continue
    else:
        numbers = [int(i) for i in numbers] #Если данные корректны - превратим их в числа
        n = int(n)
        break
if n not in numbers:    #Если такого числа нет в списке - добавим, чтобы бинарный поиск его нашёл
    numbers.append(n)
numbers = merge_sort(numbers)   #Сортировка списка слиянием
result = binary_search(numbers, n, 0, len(numbers)-1)   #Элемент уже есть в списке - ищем бинарным поиском
print('Отсортированный список:', *numbers)
if result and result != len(numbers):
    print('Номер позиции элемента в отсортированном списке:', result) #Номер, не индекс
else:
    print('Элемент не входит в границы списка')
