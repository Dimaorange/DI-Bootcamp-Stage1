liste1=["7","T","h","i","s","$","#","^"]
liste2=["i","s","%"," ","M","a","t","r"]
liste3=["3","i","x","#"," "," ","%","!"]
liste=[liste1,liste2,liste3]
mot=""
for elem in liste:
	nb=0
	for i in elem:
		if i.isalpha():
			mot=mot+i
		else:
			nb+=1
			if nb==2:
				mot=mot+" "
				nb=0
print(mot)
