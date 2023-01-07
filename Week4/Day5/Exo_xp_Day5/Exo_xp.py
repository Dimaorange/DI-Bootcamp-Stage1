
liste=[
		[" "," "," "],
		[" "," "," "],
		[" "," "," "]
		]
def display_board(liste):
	print("")
	print("TIC TAC TOE")
	longueur=("*")*19
	print(longueur)
	nb=0
	for i in liste:
		a="| "
		b=("  ")
		c="*"
		d=" | "
		e="   *"
		print(f"{c}{b}{i[0]}{b}{a}{i[1]}{b}{d}{i[2]}{e}")
		if nb<2:
			print('* ','---| '+'---'+' |'+' ---'+' *')
		nb+=1
	print(longueur)

def saisie():
	var_n=[1,2,3]
	a=int(input("Enter row:"))
	if a in var_n:
		a-=1
	else:
		while a not in var_n:
			a=int(input("Enter row under 1 and 3:"))
		a-=1
	b=int(input("Enter column:"))
	if b in var_n:
		b-=1
	else:
		while b not in var_n:
			b=int(input("Enter column under 1 and 3:"))
		b-=1
	return a,b

def player_input():
	i=1
	a=0
	b=0
	n=""
	n1=[]
	n2=[]
	while i<=6:
		if i%2!=0:
			print("")
			print("Player x's turn...")
			print("")
			n="X"
			a,b=saisie()
			verification(a,b,n)
			n1,n2=gagnant(liste)
			check_win(n1,n2)
		else:
			print("")
			print("Player O's turn...")
			print("")
			n="O"
			a,b=saisie()
			verification(a,b,n)
			n1,n2=gagnant(liste)
			check_win(n1,n2)
		i+=1
	print("Game over!")
	
def verification(a,b,n):
	if liste[a][b].isalpha():
		print("Cette case est déja occupé !")
		a,b=saisie()
		while liste[a][b].isalpha():
			print("Cette case est déja occupé !")
			a,b=saisie()
		liste[a][b]=n
	else:
		liste[a][b]=n
	display_board(liste)

def gagnant(liste):
	numX=[]
	for elem in liste:
		i=0
		while elem!=[] and i<3:
			if elem[i]=="X":
				numX.append(i)
			i+=1
	numO=[]
	for elem in liste:
		i=0
		while elem!=[] and i<3:
			if elem[i]=="O":
				numO.append(i)
			i+=1
	return numX,numO

def check_win(n1,n2):
	succes=[[0,0,0],[1,1,1],[2,2,2],[0,1,2],[2,1,0]]
	if n1 in succes:
		print("Player X is the winner.")
		print("Game over!")
		exit()
	elif n2 in succes:
		print("Player O is the winner.")
		print("Game over!")
		exit()

def play():
	print("Welcome to TIC TAC TOE!")
	display_board(liste)	
	player_input()	

play()
"""
liste=[
		[" O"," "," X"],
		[" X"," O","  "],
		[" X"," "," O"]
		]
n1=[]
n2=[]
n1,n2=gagnant(liste)
victoire(n1,n2)
"""