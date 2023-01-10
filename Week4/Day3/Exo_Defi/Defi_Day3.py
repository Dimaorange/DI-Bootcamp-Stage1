#Defi 1
#1.
# utilisé import RE
name=input("Entre votre nom:\n")
#2.
nam=[]
for i in name:
	if i in nam:
		continue
	else:
		nam.append(i)
dico={}
for n in nam:
	bat=[]
	i=0
	for ma in name:
		if n==ma:
			bat.append(i)
		i+=1
	dico.update({n:bat})
print(dico)

#Def 2.
elem={"water":"$6",
 "Pineapple":"$8", 
 "Mangoes":"$3",
 "Orange":"$4",
 "Bananas":"$2", 
 "Spoon":"$7",
 "Fan":"$15",
 "Apple":"$5",
 }
deco={}
wallet="$"+input("Entre le montant de votre argent:\n")
for cle,valeur in elem.items():
	if elem[cle]<=wallet:
 		deco.update({cle:valeur})
if deco!={}:
	print(list(deco))
	print(sorted(deco))
else:
	print("Nothing")