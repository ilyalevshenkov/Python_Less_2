# Задача 3. Задайте список из (2*N+1) элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных ИНДЕКСАХ. 
# Пять ИНДЕКСОВ хранятся в списке, который вы сами заполняете.
# Пример списка ИНДЕКСОВ [2, 2, 3, 1, 8]
# Ввод: 4
# [-4, -3, -2, -1, 0, 1, 2, 3,4]


def MultiplyElements(array_factors,indices):
    result = 1
    for x in indices:
        result *= array_factors[x]
    return result

dicunt = int(input('Введите число N.\n'))
diapazon = [n for n in range(-dicunt, dicunt + 1)]
print(diapazon)
dicunt = map(int,input('Чтобы перемножить ведите индексы элементов через пробел.\n').split())
print(MultiplyElements(diapazon,dicunt))