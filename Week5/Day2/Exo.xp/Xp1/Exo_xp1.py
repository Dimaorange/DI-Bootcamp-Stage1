"""
#Exercice 1
class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Siamese(Cat):
    pass

chien=Bengal("Rex",5)
chat=Chartreux("Boby",8)
path=Siamese("Millou",3)
all_cats=[chien,chat,path]

sara_pets=Pets(all_cats)
sara_pets.walk()
"""
#Exercice 2
class Dog():
    def __init__(self,name,age,weight):
        self.name=name
        self.age=age
        self.weight=weight

    def bark(self):
        return f"{self.name} aboie"

    def run_speed(self):
        return self.name,self.weight/self.age*10

    def fight(self,other_dog):
        a,b=self.run_speed()
        if b*self.weight > (other_dog.weight/other_dog.age*10)*other_dog.weight:
            return self.name,"a gagné le combat"
        else:
            return other_dog.name,"a gagné le combat"

"""
chien=Dog("Rex",5,12)
chat=Dog("Bob",6,3)
path=Dog("Millou",3,9)
other_dog=Dog("Boby",8,15)
print(chien.bark())
print(path.run_speed())
print(chat.fight(other_dog))
"""