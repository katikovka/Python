"""
Напишите функцию cacluate, которая может принимать любое количество чисел и возвращать кортеж.
Первое значение кортежа - это среднее значение всех параметров, а второе значение - все числа, превышающие среднее значение.
Второе значение оформите в виде списка.
"""


def calculate(nums):
    summary = 0
    for num in nums:
        summary += int(num)

    medium = summary // len(nums)

    num_above_average = []
    for num in nums:
        if int(num) > medium:
            num_above_average.append(num)

    result = (medium, num_above_average)
    return result


numbers = (input('Введите все числа: ')).split()
print(calculate(numbers))