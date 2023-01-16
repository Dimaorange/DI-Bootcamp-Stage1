class Pagination():
	
	def __init__(self,items=[],pageSize=10):
		self.items=items
		self.pageSize=int(pageSize)

	def getVisibleItems(self):
		dico=[]


	def firstPage(self):
		nb=0
		dico=[]
		while nb<self.pageSize:
			dico.append(self.items[0][nb])
			nb+=1
		return dico

	"""def prevPage(self):
					pass
			
				def nextPage(self):
					nb=0
					while nb<self.pageSize:
						self.items.remove(self.items[0])
						nb+=1
					return self.getVisibleItems()
			
			
				def lastPage(self):
					if len(self.items)%self.pageSize==0:
						nb=0
						i=1
						dico=[]
						while nb<self.pageSize:
							dico.append(self.items[-i])
							i+=1
							nb+=1
					else:
						r=len(self.items)%self.pageSize
						nb=0
						i=r
						dico=[]
						while nb<r:
							dico.append(self.items[-i])
							i-=1
							nb+=1
					print(dico)"""

alphabetList ="abcdefghijklmnopqrstuvwxyz".split(' ')
p = Pagination(alphabetList, 4)
p.getVisibleItems() 
#p.nextPage()
#p.lastPage()