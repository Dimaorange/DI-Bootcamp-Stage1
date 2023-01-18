class Pagination():
	def __init__(self,items=[],pageSize=10):
		self.items=items
		self._pageSize=int(pageSize)
		self.currentPage=1
		self.totalPages=7 

	def getVisibleItems(self):
		if len(self.items[0])%self._pageSize==0:
			nb=len(self.items[0])//self._pageSize
		else:
			nb=int(len(self.items[0])//self._pageSize+1)
		if self.currentPage<=1:
			dico=[]
			n=0
			while n<int(self._pageSize):
				dico.append(self.items[0][n])
				n+=1
			print(dico)
		else:
			i=0
			for cmpt in list(range(2,nb+1)):
				if cmpt<nb:
					if cmpt==self.currentPage:
						dico=[]
						i=int(cmpt*self._pageSize)-int(self._pageSize)
						while i<int(self._pageSize*cmpt):
							dico.append(self.items[0][i])
							i+=1
						print(dico)
					else:
						continue
				else:
					dico=[]
					i=int(cmpt*self._pageSize)-int(self._pageSize)
					while i<len(self.items[0]):
						dico.append(self.items[0][i])
						i+=1
					print(dico)
				break

	def prevPage(self):
		self.currentPage-=1
	def nextPage(self):
		self.currentPage+=1
	def firstPage(self):
		self.currentPage=1
	def lastPage(self):
		if len(self.items)%self._pageSize==0:
			self.currentPage=len(self.items[0])//self._pageSize
		else:
			self.currentPage=int(len(self.items[0])//self._pageSize+1)
	def goToPage(self,Pagenum):
		self.currentPage=int(Pagenum)

alphabetList ="abcdefghijklmnopqrstuvwxyz".split(' ')
p = Pagination(alphabetList, 4)
p.firstPage()
p.getVisibleItems() 
p.nextPage()
p.getVisibleItems()
p.lastPage()
p.getVisibleItems()
p.goToPage(3)
p.getVisibleItems()
p.prevPage()
p.getVisibleItems()