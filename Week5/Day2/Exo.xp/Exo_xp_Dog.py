from Exo_xp1 import Dog
class PetDog(Dog):
	def __init__(self,name,age,weight,trained=False):
		super().__init__(name,age,weight)
		self.trained=trained

	def Train(self):
		print(f'{super(PetDog,self).bark()}')#print(self.bark())
		self.trained=True

	def Play(self,*args):
		other_dog_name=""
		for elem in args:
			other_dog_name=other_dog_name+" "+elem.name
		"""self.dog_name=""
		self.dog_name+=(self.name+",\t")
		"""
		print(f"{other_dog_name} {self.name} tous jouent ensemble")

	def Do_a_trick(self):
		if self.trained==True:
			display=["does a barrel roll","stands on his back legs","shakes your hand","plas dead"]
			n=r.choice(display)
			print(f"{self.name} {n}")

boutk=PetDog("Rex",3,9)
#boutk.Train()
#print(chien.bark())
chat=PetDog("Bob",6,3)
path=PetDog("Millou",3,9)
other_dog=PetDog("Boby",8,15)
liste=[boutk,chat,path,other_dog]
#boutk.Play(chat,path,other_dog)
chat.Do_a_trick()