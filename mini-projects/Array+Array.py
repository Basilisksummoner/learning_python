# Задача с CodeWars
# Условие
# I'm new to coding and now I want to get the sum of two arrays... 
# Actually the sum of all their elements. I'll appreciate for your help.
# P.S. Each array includes only integer numbers. Output is a number too.


# Мое решение
def array_plus_array(arr1, arr2):
    return sum(arr1) + sum(arr2)

a = [1,2,3]
b = [1,2,3]
print(array_plus_array(a,b))