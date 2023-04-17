class Cat():
    def __init__(self, im9, pol, vozrast):
        self.name = im9
        self.gender = pol
        self.age = vozrast

    def get_name(self):
        return self.name

    def get_gender(self):
        return self.gender

    def get_age(self):
        return self.age


class Klient():
    def __init__(self, имя, фамилия, город, баланс):
        self.name = имя
        self.fam = фамилия
        self.sity = город
        self.cach = баланс

    def __str__(self):
        return f'{self.name} {self.fam}. {self.sity}. Баланс: {self.cach} руб.'

    def info(self):
        return [self.name, self.fam, self.sity]



class Dog(Cat):
    def get_pet(self):
        return [self.name, self.age]

# class Dog(Cat):
#     def get_pet(self):
#         return f'{self.get_name()} {self.get_age()}'
