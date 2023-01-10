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

#Exercice 3 a revoir
class Song():
	def __init__(self,lyrics):
		self.name=lyrics

	def sing_me_a_song(self,lyrics):
		for elem in lyrics:
			self.name=elem
			print(f"{self.name}")

stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])
stairway.sing_me_a_song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])
