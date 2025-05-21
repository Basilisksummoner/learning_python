in Python we use **snake_case**

1) `Python Data Types`
    В питоне типы данных можно разделиить на `2`
    `Mutable` и `Immutable`

    К `immutable` относятся:
    1. str = 'Hello World'
    2. int = 5
    3. float = 3.14
    4. bool = True, False
    5. tuple или кортеж = (10,20)
    6. frozenset = ([1,2,3])

    К `mutable` (изменяемые):
    1. list = [1,2,3]
    2. dict = {'name': 'Jhon'}  # ключ: значение
    3. set = {1,2,3}
    4. bytearray

2. `String concats`
  ("string" + "string")

3. `Formatting strings`
    print(f"Hello, {user_name}!")
    You can do calculations, and many things in {}

4. `Functions`
    Basically logic, that does something
  
    def function_name(parameters):  #мб несколько, пишем через ,
  
    How to use a function?
    function_name(parameters that we want)

    Function parameters
    function_name(var_name)

    Function have to return some value
    return key word

    Чтобы сохранить функцию в глобальном скопе нужно присвоить ее перменной
    var_b = fucntion_b()


    Аргументы нужны чтобы писать дальнейшую логику функции

    Можно не передавать аргументы, если функция 
    делает что-то конкретное и фиксированное
  
    Но аргументы делают функцию универсальным инструментом, 
    который можно использовать повторно с разными данными

5. `Scope`
  
    Local vars - created within a func func_name(var, var)
    can be used only inside a function

    Global vars - any other vars outside a func

6. `User input`
    user_input = input("Enter a value\n")
  
    Input always a string!
  
    We can use Typecasting
    str(var) = var превратиться в str
    int(var) = var станет int

    .lower() - переводит всё в маленькие буквы
    .upper() - переводит всё в CAPS

7. `Conditionals`
  
    Expressions that evaluate to either true or False
      a == b (check if a equals b)
      a != b (check if a doesnt equals b)
      a > b, a < b (greater than or less than)
      a >= b, a <= b (greater equals than or less equals than)

    If/elif/else
    if a == b: если а равно b (не присваивание)
    elif a =! b: не равно
    else:  иначе

    Важный лайфхак!
    if var_a not in ()
    вместо if var_a in ()
      

8. `While loops`
    while True
    func_name()
    if условие
      break # для выхода из цикла

9. `for loops`
for x in (1,2,3)
    
      for x in range
      Как работет range? (start,stop,step)
      start нижняя граница 
      stop верхняя гранциа за её вычетом т.е если 10 то будет 9
      step на сколько прыгаем 1,2,3 и т.д
      range(1,10,1) - пробежит от 1 до 9и 