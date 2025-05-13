# Это простой конвертатор дней в часы, в котором я тренил свое понимание
# простых функций и conditionals


def day_converter(days_num): # Объявляю функцию, в которую передаю аргумент days_num
  if days_num > 0:                 # В функции будут соверашться вычисления
    calc_answer = days_num*24           
    print(                                
      f'In {days_num} days there is {calc_answer} hours '
    )
  elif days_num == 0:
    print('In zero days there is zero hours ;)')
  else:
    print('Wrong inputs')


def user_input():       # Функция собирающая user_input
  days = input('Please enter number of days:\n')
  if days.lower() == 'exit':
    return 'exit'
  try:                        # Error Handling
    return int(days)
  except ValueError:
    print("That's not a valid number!")
    return None


while True:                # Бесконечный цикл с возможностью выхода если user введёт exit
  user_num = user_input()
  if user_num == 'exit':
    break
  elif user_num is not None:
    day_converter(user_num)
  