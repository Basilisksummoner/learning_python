# Задачка с CodeWars для закрепа conditionals
# Условие
# You are given the length and width of a 4-sided polygon. 
# The polygon can either be a rectangle or a square.
# If it is a square, return its area. If it is a rectangle, return its perimeter.


#Мое решение
def area_or_perimeter(l , w):
  if l == w:
    area = l**2
    return area 
  else:
    perimeter = (l+w)*2
    return perimeter