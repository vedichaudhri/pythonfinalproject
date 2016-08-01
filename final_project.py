import turtle as t

CLefthand = t.Turtle()
CRighthand = t.Turtle()
PRighthand = t.Turtle()
PLefthand = t.Turtle()

def GetHandsInPosition():
	CLefthand.goto(-120, 80)
	CRighthand.goto(120,80)
	PLefthand.goto(-120, -80)
	PRighthand.goto(-120, 80)
	CLefthand.settiltangle(180)
	CRighthand.settiltangle(180)
	PRighthand.settiltangle(0)
	PLefthand.settiltangle(0)

def reset_hands():
	values_on_hand = [1, 1, 1, 1]
	CLeft = 1
	CRight = 1
	PLeft = 1
	PRight = 1

def pick_turn():
	turn = 0
	while (turn != "y" or turn != "c" or turn != "f"):
		turn = input("Do you want to start? Press Y. If you want the computer to start, press C. Or press F to flip a coin ")
		print(turn)
		pass

def pick_turn2():
	turn2 = 0
	while turn2 == 0:
		turn2 = input("Do you want to start? Press Y. If you want the computer to start, press C. Or press F to flip a coin :")
		print("You choose " + turn2)