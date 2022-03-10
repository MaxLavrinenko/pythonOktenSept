# ...создать декоратор который будет считать сколько раз была запущена функция
# и будет выводит это значение после каждого запуска функции
#
# def decorator(func):
#     count = 0
#
#     def inner():
#         nonlocal count
#         count += 1
#         print('-' * 20)
#         func()
#         print('-' * 20)
#         print('Count = ', count)
#
#     return inner
#
#
# @decorator
# def greeting():
#     print('Hello')
#
#
# @decorator
# def greeting2():
#     print('Hi')
#
#
# greeting()
# greeting()
# greeting2()

#
# кому это очень легко то сделайте функцию на замыкания которая будет возвращать декоратор который
# будет считать общее количество запущенных  функций декорированных этим декоратором
count = 0
def decorator(func):

    def addcount():
        global count
        count += 1

    def inner():
        addcount()
        global count
        print('-' * 20)
        func()
        print('-' * 20)
        print('Count of use this decorator= ', count)
    return inner

@decorator
def greeting():
    print('Hello')


@decorator
def greeting2():
    print('Hi')


greeting()
greeting()
greeting2()