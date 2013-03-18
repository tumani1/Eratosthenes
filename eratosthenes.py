import math

class Eratosthenes(object):
    def __init__(self, value, *args, **kwargs):
        if not isinstance(value, int):
            raise TypeError("Value is not Integer")

        self.__value = value
        self.__value_list = [True] * self.__value
        self.__flag = True

    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, value):
        if not isinstance(value, int):
            raise TypeError("Value is not Integer")

        self.__value = value
        self.__value_list = [True] * self.__value
        self.__flag = True
    
    @value.deleter
    def value(self):
        raise AttributeError("This value not delete")

    def __repr__(self):
        return "Eratosthenes value %s" % (self.__value)

    __str__ = __repr__    

    def __algo(self):
        for i in range(2, int(math.sqrt(self.__value))):
            for j in range(i * 2, self.__value, i):
                self.__value_list[j] = False

    def result(self):
        if self.__flag:
            self.__algo()
            self.__value_list = [i for i in range(2, self.__value) if self.__value_list[i]]
            self.__flag = False

        return self.__value_list

def main():
    ex = Eratosthenes(20)
    print ex.value
    print ex.result()

    ex.value = 30
    print ex.value
    print ex.result()

    print ex
    print ex.__algo()

    print dir(ex)

    ex = Eratosthenes("sqxws")

if __name__ == "__main__":
    main()
