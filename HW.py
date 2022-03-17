#
# 1) Створити абстрактний клас Printable який буде описувати абстрактний метод print()
from abc import ABC, abstractmethod


class Printable(ABC):
    @abstractmethod
    def print(self):
        pass


#
#
# # 2) Створити класи Book та Magazine в кожного в конструкторі змінна name, та який наслідуются від класу Printable
class Book(Printable):
    def __init__(self, name: str):
        self.name = name

    def print(self):
        return print(self.name)


class Magazine(Printable):
    def __init__(self, name: str):
        self.name = name

    def print(self):
        return print(self.name)


#
book1 = Book('book1')
# book1.print()
magazine1 = Magazine('magazine1')


# magazine1.print()


# 3) Створити свій кастомний Exception
# class MyCustomException(Exception):
#     pass
#
#
# try:
#     num = input('enter number: ')
#     if not num.isdigit():
#         raise MyCustomException
# except MyCustomException:
#     num = 0
#     print('You tape not int, num = ', num)
# except Exception as err:
#     print('pupupu', err)
# else:
#     print('all ok!')
# finally:
#     print('finish')

# 4) Створити клас Main в якому буде:
# - змінна класу printable_list яка буде зберігати книжки та журнали
# - метод add за допомогою якого можна додавати екземпляри класів в список і робити перевірку чи то що передають є класом Book або Magazine інакше кидати свою кастомну помилку
# - метод show_all_magazines який буде виводити всі журнали викликаючи метод print абстрактного классу
# - метод show_all_books який буде виводити всі книги викликаючи метод print абстрактного классу
# 5)всі методи класу Main запускати в try except, приклад:
# try:
#     Main.add(Magazine('Magazine1'))
#     Main.add(Book('Book1'))
#     Main.add(Magazine('Magazine3'))
#     Main.add(Magazine('Magazine2'))
#     Main.add(Book('Book2'))
#
#     Main.show_all_magazineі()
#     print('-' * 40)
#     Main.show_all_bookі()
# except NonBookMagazineException:
#     print('Це не журнал або книжка')
# except Exception as err:
#     print(err)
class Test:
    def __init__(self, name):
        self.name = name


class MyCustomException(Exception):
    pass


class Main:
    printable_list = []

    @classmethod
    def add(cls, new):
        if not isinstance(new, (Book, Magazine)):
            raise MyCustomException
        cls.printable_list.append(new)

    @classmethod
    def show_all_books(cls):
        for i in cls.printable_list:
            if isinstance(i, Book):
                i.print()

    @classmethod
    def show_all_magazins(cls):
        for i in cls.printable_list:
            if isinstance(i, Magazine):
                i.print()


try:
    Main.add(Magazine('Magazine1'))
    Main.add(Book('Book1'))
    Main.add(Magazine('Magazine3'))
    Main.add(Magazine('Magazine2'))
    Main.add(Book('Book2'))

    Main.show_all_books()
    print('-' * 40)
    Main.show_all_magazins()

    Main.add(Test('test'))

except MyCustomException:
    print('Це не журнал або книжка')
except Exception as err:
    print(err)
