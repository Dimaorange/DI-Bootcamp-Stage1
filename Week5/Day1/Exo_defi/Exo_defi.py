#Mode d'emploi
class Farm():
	def __init__(self,name):
		self.animals={}
		self.name=name

	def add_animal(self,name,nb=1):
		self.name=name
		if self.name in self.animals.keys():
			self.animals[self.name]+=nb
		else:
			self.animals[self.name]=nb
												
	def get_info(self):
		affich=f"{self.name}'s Farm\n"
		for cle in self.animals.keys():
			affich=affich+f"{cle} :{self.animals[cle]}\n"
		return affich+"\t" +"E-I-E-I-0!"
		


	#Agrandir la ferme
	def get_animal_types(self):
		self.name=list(self.animals.keys())
		self.name=set(self.name)
		self.name=list(sorted(self.name))
		return self.name

	def get_short_info(self):
		a=self.get_animal_types()
		liste=""
		i=0
		while i<len(a):
			if i==0:
				liste=a[i]
			else:
				liste=liste+", "+a[i]
			i+=1
		print(f"La ferme McDonald's possède {liste}")


macdonald = Farm("McDonald")
macdonald.add_animal('cow',5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())
macdonald.get_short_info()