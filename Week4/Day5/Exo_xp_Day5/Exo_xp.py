
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
		g="  "
		print(f"*{g}{i[0]}{g}|{g}{i[1]}{g}|{g}{i[2]}{g}*")
		if nb<2:
			print('*','---'+' | '+'---'+' |'+' ---'+' *')
		nb+=1
	print(longueur)

def saisie():
	var_n=["1","2","3"]
	a=input("Enter row:")
	if a in var_n:
		a=int(a)
		a-=1
	else:
		while a not in var_n :
			a=input("Enter row under 1 and 3:")
		a=int(a)
		a-=1
	b=input("Enter column:")
	if b in var_n:
		b=int(b)
		b-=1
	else:
		while b not in var_n:
			b=input("Enter column under 1 and 3:")
		b=int(b)
		b-=1
	return a,b

def player_input():
	import random as r
	i=1
	a=0
	b=0
	n=""
	players=["X","O"]
	v=r.choice(["X","O"])
	if v=="X":
		s="O"
	else:
		s="X"
	while i<=9:
		if i%2!=0:
			print("")
			print(f"Player {v}'s turn...")
			print("")
			n=v
			a,b=saisie()
			verification(a,b,n)
			check_win(liste,n)
		else:
			print("")
			print(f"Player {s}'s turn...")
			print("")
			n=s
			a,b=saisie()
			verification(a,b,n)
			check_win(liste,n)
		i+=1
	print("Draw game")
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
"""
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

def check_win(numX,numO):
	succes=[["00","01","02"],[0,1,2],[2,1,0]]
	if numX in succes:
		print("Player X is the winner.")
		print("Game over!")
		exit()
	elif numO in succes:
		print("Player O is the winner.")
		print("Game over!")
		exit()
"""
def check_win(liste,n):
	if liste[0][0]==liste[0][1]==liste[0][2]==n:
		print(f"Player {n} is the winner.")
		print("Game over!")
		exit()
	elif liste[1][0]==liste[1][1]==liste[1][2]==n:
		print(f"Player {n} is the winner.")
		print("Game over!")
		exit()
	elif liste[2][0]==liste[2][1]==liste[2][2]==n:
		print(f"Player {n} is the winner.")
		print("Game over!")
		exit()
	elif liste[0][0]==liste[1][0]==liste[2][0]==n:
		print(f"Player {n} is the winner.")
		print("Game over!")
		exit()
	elif liste[0][1]==liste[1][1]==liste[2][1]==n:
		print(f"Player {n} is the winner.")
		print("Game over!")
		exit()
	elif liste[0][2]==liste[1][2]==liste[2][2]==n:
		print(f"Player {n} is the winner.")
		print("Game over!")
		exit()
	elif liste[0][0]==liste[1][1]==liste[2][2]==n:
		print(f"Player {n} is the winner.")
		print("Game over!")
		exit()
	elif liste[0][2]==liste[1][1]==liste[2][0]==n:
		print(f"Player {n} is the winner.")
		print("Game over!")
		exit()
	else:
		pass

def play():
	print("Welcome to TIC TAC TOE!")
	display_board(liste)	
	player_input()	

play()