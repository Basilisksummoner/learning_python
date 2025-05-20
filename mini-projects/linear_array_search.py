def array_search(A:list,N:int, x:int):  # Передаем три аргумента
    """Осуществляет поиск числа x в массиве A
        от 0 до N-1 индекса включительно.
        Возвращает инедкс элемента x в массиве A
        или -1 если такого нет
    """
    for k in range(N):
        if A[k] == x:
            return k
    return -1

def array_search_test():
    A1 = [1,2,3,4,5]
    m = array_search(A1,5,8)
    if m == -1:
        print('test#1 - ok')
    else:
        print('test#1 - fail')

    A2 = [-1,-2,-3,-4,-5]
    m = array_search(A2,5,-3)
    if m == 2:
        print('test#2 - ok')
    else:
        print('test#2 - fail')

    A3 = [10,20,30,10,10]
    m = array_search(A3,5,10)
    if m == 0:
        print('test#3 - ok')
    else:
        print('test#3 - fail')

array_search_test()