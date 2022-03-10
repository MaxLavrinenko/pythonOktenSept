# написать функцию на замыкания которая будет в себе хранить лист дел, вам нужно реализовать два метода
# - первый записывает в эту переменную запись
# - второй возвращает все записи
#
# запишите 5 тудушек
# и выведете все
# def notebook():
#     todoList: list[str] = []
#
#     def addTodo(new: str) -> None:
#         nonlocal todoList
#         todoList.append(new)
#
#     def readTodo() -> list[str]:
#         print(todoList)
#         return todoList
#
#     return addTodo, readTodo
#
#
# addTodo, readTodo = notebook()
# addTodo('wake up')
# addTodo('eat')
# addTodo('ddos russians')
# addTodo('read news')
# addTodo('sleep')
# readTodo()

########

# 2) протипизировать первое задание

# 3) создать функцию которая будет возвращать сумму разрядов числа в виде строки (тоже с типизацией)
#

def expanded(num: int) -> None:
    n = str(num)
    l = list(n)
    print(l)

    for i in l:
        print(i)
    # for i in n:
    #     if (num != 0):
    #         p = num % 10
    #         l.append(p)
    #         num = num // 10
    # print(l)

expanded(1234)

# Пример:
#
# expanded_form(12) # return '10 + 2'
# expanded_form(42) # return '40 + 2'
# expanded_form(70304) # return '70000 + 300 + 4'
