"""
Дан массив, в котором среди прочих элементов есть слово odd(нечётный). Определите, есть ли в списке число, которое
является индексом элемента odd. Напиши функцию, которая будет возвращать True или False, соответственно.

print(odd_ball(["even", 4, "even", 7, "even", 55, "even", 6, "even", 10, "odd", 3, "even"])) - True
print(odd_ball(["even", 4, "even", 7, "even", 55, "even", 6, "even", 9, "odd", 3, "even"])) - False
print(odd_ball(["even", 10, "odd", 2, "even"])) - True
"""


def odd_ball(arr):
    return arr.index("odd") in arr


print(odd_ball(["even", 10, "odd", 2, "even"]))

"""
Напишите функцию find_sum(n), где аргумент функции - это конечный элемент последовательности включительно.
Функция должна вернуть сумму всех чисел последовательности кратных 3 или 5. Попробуйте решить задачу двумя способами.
Один из способов в одну строчку кода.

find_sum(5) - return 8 (3 + 5)
find_sum(10) - return 33 (3 + 5 + 6 + 9 + 10)
"""


def find_sum(n):
    arr = [i for i in range(1, n + 1)]
    new_arr = []
    for item in arr:
        if item % 3 == 0 or item % 5 == 0:
            new_arr.append(item)
    return sum(new_arr)


def find_sum2(n):
    return sum(item for item in range(1, n + 1) if item % 3 == 0 or item % 5 == 0)


print(find_sum2(10))

"""
Дан список имён. Выберите в новый список только те имена, которые состоят из 4-х букв.
names = ["Ryan", "Kieran", "Mark", "John", "David", "Paul"] ---> names = ["Ryan", "Mark", "John", "Paul"]
"""


def get_names(names):
    return [name for name in names if len(name) == 4]


print(get_names(["Ryan", "Kieran", "Mark", "John", "David", "Paul"]))
