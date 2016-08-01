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

#setting_gloabal variables
values_on_hand = [1, 1, 1, 1]
CLeft = 1
CRight = 1
PLeft = 1
PRight = 1
Level = ""
own_hand = "" #no
opponents_hand "" #no
moves = "" #no
moves_not_to_make = []

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

def game_over():

def easy():

def medium():

def hard():

def finish_computers_turn():

def how_to_win_computer (values_on_hands):

def are_hands_available_for_move(move):

def do_move(move):

def generate_list_of_moves_not_to_make():

def display_instructions():

def choosing_hands():

def flip_coin():

def update_numbers():

def show_about_to_win_meme ():

def show_about_to_win_costume():

def winning_screen():

def loosing_screen():
