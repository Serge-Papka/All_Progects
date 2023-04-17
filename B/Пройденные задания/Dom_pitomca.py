from Cats import Cat, Klient
from Cats import Dog

cat1 = Cat("Барон", "Мальчик", 2)
cat2 = Cat("Сэм", "Мальчик", 2)
print (cat1.get_name() , end= ', ')
print (cat1.get_gender() , end= ', ')
print (cat1.get_age() , end= ', \n')
print (cat2.get_name() , end= ', ')
print (cat2.gender , end= ', ')
print (cat2.get_age() , end= ', \n')

Dog1 = Dog("Мухтар", "Мальчик", 0)
print (Dog1.get_pet())

Klient1= Klient("Иван", "Петров", "Москва",50)
Klient2= Klient("Пер", "Мавп", "Клин",150)
Klient3= Klient("Вася", "Сидоров", "Омск",30)

Coorp  = [Klient1, Klient2, Klient3]
for i in Coorp:
    print (i.info(), end= ' ')

