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
"""
#Exercice 4
class Zoo():
    def __init__(self,Zoo_name):
        self.animals=[]
        self.name=Zoo_name

    def add_animals(self,new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)
        return self.animals

    def get_animal(self):
        for animal in self.animals:
            print(animal)

    def sell_animal(self,animal_sold):
        try:
            self.animals.remove(animal_sold)
        except:
            print(f"{animal_sold} n'existe pas.")

    def sort_animals(self):
        self.animals=sorted(self.animals)
        elem=[]
        diction={}
        for i in enumerate(self.animals):
            elem.append(i)
            dico=dict(elem)
            diction=dico
            dictionnaire={}
        for cle1,valeur in diction.items():
            if cle1 not in dictionnaire.items():
                el=[]
                for cle,valeur in dico.items():
                    el.append(diction[cle1])
                    if dico[cle][0]==diction[cle1][0] and cle!=cle1:
                        el.append(dico[cle])
                dictionnaire.update({cle1:el})
        print(dictionnaire)

            
animal_name=Zoo("Mamifère")
animal_name.add_animals("chevre")
animal_name.add_animals("boeuf")
animal_name.add_animals("lapine")
animal_name.add_animals("mouton")
animal_name.add_animals("chevraux")
animal_name.add_animals("buffle")
animal_name.add_animals("lapin")
#animal_name.sell_animal("mouton")
#animal_name.get_animal()
animal_name.sort_animals()
"""