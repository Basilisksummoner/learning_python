# Задачка с CodeWars для закрепа циклов for
# Условие:
# Given a non-negative integer, 3 for example, 
# return a string with a : 
# "1 sheep...2 sheep...3 sheep...". Input will always be valid, i.e. no negative integers.


# Мое решение
def count_sheep(n):
    result = ''
    for x in range(1, n+1):
        result += f'{x} sheep...'
    return result

print(count_sheep(3))  # input любое число (none negative)