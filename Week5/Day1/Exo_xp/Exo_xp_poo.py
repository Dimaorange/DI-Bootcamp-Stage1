"""
#Exercice 1
class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age
        
cat1=Cat("Rex",6)
cat2=Cat("Boby",2)
cat3=Cat("Millou",8)

def Trouver(cat1,cat2,cat3):
	if cat1.age>=cat2.age:
		pass
	else:
		cat1=cat2
	if cat3.age>cat1.age:
		cat1=cat3
	return cat1
	
print(f"Le chat le plus âgé est {Trouver(cat1,cat2,cat3).name} et a {Trouver(cat1,cat2,cat3).age} ans.")

#Exercice 2
class Dog():
	def __init__(self,name,height):
		self.name=name
		self.height=height

	def bark(self):
		print(f"{self.name} goes woof!")

	def jump(self):
		print(f"{self.name} jumps {self.height*2} cm high!")

davids_dog=Dog("Rex",50)
davids_dog.bark()
davids_dog.jump()
sarahs_dog=Dog("Teacup",20)
sarahs_dog.bark()
sarahs_dog.jump()

if davids_dog.height<sarahs_dog.height:
	print(sarahs_dog.name)
else:
	print(davids_dog.name)
"""
#Exercice 3 a revoir
class Song():
	def __int__(self,lyrics):
		self.name=lyrics
		#print(f"{self.lyrics}")

	def sing_me_a_song(self,lyr):
		print(f"{self.name}")
stairway=Song()
stairway.sing_me_a_song(["There’s a lady who 's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])

#Exercice 4
class Zoo():
	def __int__(self,Zoo_name):
		self.animals=[]
		self.name=Zoo_name

	def add_animals(self,new_animal):
		if new_animal not in animals:
			animals=animals.append(new_animal)

	def get_animal(self):
		for animal in animals:
			print(animal)

	def sell_animal(self,animal_sold):
		if animal_sold in animals:
			animals.remove(animal_sold)

	def sort_animals(self):
		animals=sorted(animals)
		
