#coding=utf-8


class TestClass():

    def __new__(cls, name):
        print('__new__ called.')
        # return super().__new__(cls, name)

    def __init__(self, name):
        print('__init__ called.')
        self.name = name
        # return self.name

    def __get__(self):
        self.name = 'kjkjjerke'
        print('2222')
        return self.name


if __name__ == '__main__':
    a = TestClass('a')
    # print(a.name)
    # print(a.__dict__)
    # print(a.__get__())
    #
    # b = TestClass.__new__(TestClass, 'b')
    # # print(b.name)
