# Инкапсуляция

# уровни доступа
# 1 публичный, 2 защищенный, 3 приватный
# _Class__atrr

class Bank(object):
    def __init__(self, name, age, balance):
        self.name = name
        self._validate_age(age)
        self._age = age
        self.__balance = balance

    def _validate_age(self,age):
        if age < 18:
            raise ValueError("Возраст должен быть 18+")

    def get_age(self):
        # print(self._age)
        return self._age

    def set_age(self, new_age):
        self._validate_age(new_age)
        self._age=new_age
        print(f'Возраст {self.name} изменен на {self._age} лет')
    @property
    def balance(self):
        # return self.__balance
        print(self.__balance)

    @balance.setter
    def balance(self,money):
        if money<0:
            raise ValueError("нечего грузить")
        self.__balance = money

    @balance.deleter
    def balance(self):
        print('баланс обнулен')
        del self.__balance


    def __str__(self):
        return (f'name:{self.name}\n'
                f'age:{self._age}\n'
                f'balance:{self.__balance}\n')


beka = Bank('beka', 18, 1000)
# beka.name = 'Bekbolot'
beka._age=99

# beka._Bank__balance = 111200

print(beka)
# print(dir(beka))
beka.balance
beka.balance=199
del beka.balance
# beka._age=199
# beka.set_age(19)
# print(beka)