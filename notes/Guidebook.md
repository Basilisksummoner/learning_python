in Python we use **snake_case**

1) `Python Data Types`
    strings = 'String'
    int = 1,2,3
    float = 3.14
    bool = True, False

    `Type annotations`
    var_name: str = 'Hello'   указываем что var_name конкретно string
    age: int = 22
    !!!Аннотации типов ничего не делают в проге, т.е даже если в age вписать string
    всё будет работать!!!

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