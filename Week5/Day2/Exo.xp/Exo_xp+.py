#Exercice 1
class Family():
	def __init__(self,membres,nom_de_famille):
		#self.membres=[]
		self.membres=membres
		self.nom_de_famille=nom_de_famille

	def born(self,**kwargs):
		dico={}
		for cle,valeur in kwargs.items():
			dico.update({cle:valeur})
		self.membres.append(dico)
		print(f"Félicitation à la famille {self.nom_de_famille}!")

	def is_18(self,name):
		nb=0
		for elem in self.membres:
			if elem['name']==name and elem['age']>=18:
				nb=1
				return "True"
				break
		if nb==1:
			return "False"

	def family_presentation(self):
		nom=""
		for elem in self.membres:
			print(f"{self.nom_de_famille} {elem['name']}")

liste=[
    {'name':'Michael','age':35,'gender':'Male','is_child':False},
    {'name':'Sarah','age':32,'gender':'Female','is_child':False}
	]
"""
exo=Family(liste,"CONGO")
exo.born(name="Abdoul Momine",age=12,gender="Male",is_child="False")
exo.family_presentation()
"""
#Exercice 2
class TheIncredibles(Family):
	def __init__(self,membres,nom_de_famille):
		super().__init__(membres,nom_de_famille)
		self.membres=membres
		self.nom_de_famille=nom_de_famille
		
	def use_power(self):
		n=0
		for elem in self.membres:
			a=super(TheIncredibles,self).is_18(elem['name'])
			if a=="True":
				n=1
				print(f"{elem['name']} {elem['power']}")
		if n==0:
			print(f"Ils n'ont pas plus de 18 ans.")

	def incredible_presentation(self):
		super().family_presentation()
		#super(TheIncredibles,self).born(self,'name'='Baby Jack','power'='Unknown Power')
		for elem in self.membres:
			print(f"{elem['name']} {elem['power']}")
lecture=[
    {'name':'Michael','age':35,'gender':'Male','is_child':False,'power': 'fly','incredible_name':'MikeFly'},
    {'name':'Sarah','age':32,'gender':'Female','is_child':False,'power': 'read minds','incredible_name':'SuperWoman'}
	]
"""
texte=TheIncredibles(lecture,"Drabo")
texte.born(name='Youssef',age=25,gender='Male',is_child='False',power='fly',incredible_name='MikeFly')
texte.incredible_presentation()
#texte.use_power()
"""