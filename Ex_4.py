# Задача 4 . Требуется посчитать сумму чётных чисел, расположенных между числами 1 и N включительно.


def SumEven(array):
    sum = 0
    for n in array:
        if n % 2 == 0:
            sum += n
    return sum
dicunt = int(input('Введите число N.\n'))
print(SumEven(range(dicunt + 1)))
