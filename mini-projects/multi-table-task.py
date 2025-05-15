# Задача с CodeWars
# Условие
# Your goal is to return multiplication table for number 
# that is always an integer from 1 to 10.
# For example, a multiplication table (string)


# Моё решение
def multi_table(number):
    for i in range(1,11):
        x = i * number
        print(f'{str(i)} * {str(number)} = {str(x)}')