"""
This is a python based game which is a spoof of the King Arthur and Holy Grail stories.
There is decision making, randomness, and risk of death.
This game takes places in a fictional world containing geographic and topological features. (hills, mountains, rivers, lake, etc.)
I hope you enjoy it. Good luck and God speed!

(i am editing this line via github.)
"""
#		What types of input? raw_data, random input taken from an integer range, random input taken from a list, ?
#		What types of output? console, standard output on screen.

# Import modules
import random

# dragon alive or dead status
#dragon_alive = True

# Define global variables
# dice roll d6
#d6 = random.randint(1, 6)
#print d6
# dice roll d20
#d20 = random.randint(1, 20)
#print d20


# Define functions which will be used.
# First start function
def start():
	print "You are a brave adventurer, starting out in the world."
	print "You want to travel around this land seeking fame and fortune."
	print "It is time to claim what is yours!"
	print "Would you like to go: \n'west' to the Fledd Mountains,\n'east' to the Dragon's lair, or \n'southwest' to the Badlands?"
	
	choice = raw_input("> ")
	if choice == "west":
		fledd()
	elif choice == "east":
		dragon()
	elif choice == "southwest":
		badlands()
	else:
		dead("You stumble around the area until you starve.")

# Second start function
def start2():
	#global dragon_alive
	print "You are back to where you were before."
	print "Would you like to go: \n'east' to the Dragon's lair, 'west' to the Fledd mountains, or \n'southwest' to the Badlands?"
	choice = raw_input("> ")
	if choice == "east": #and dragon_alive:
		dragon()
	elif choice == "southwest":
		badlands()
	elif choice == "west":
		fledd()
	else:
		dead("You stumble around the area until you starve.")
		
# Third start function		
def start3():
	print "Would you like to go: \n'east' to the High plains, or \n'south' to the Land of Black Knights?"
	choice = raw_input("> ")
	if choice == "east":
		highplains()
	elif choice == "south":
		knights()
	else:
		dead("You stumble around the area until you starve.")
		
# Fourth start function		
def start4():
	#global dragon_alive
	print "Would you like to go: \n'northeast' to the Dragon's lair, \n'south' to the Land of Black Knights or\n'east' to Troll Town?"
	choice = raw_input("> ")
	if choice == "northeast": #and dragon_alive:
		dragon()
	elif choice == "south":
		knights()
	elif choice == "east":
		trolltown()
	else:
		dead("You stumble around the area until you starve.")
		
# Fifth start function
def start5():
	print "Would you like to go 'east' to the lake, or\'south' to the Land of Black Knights?"
	if choice == "east":
		lake()
	elif choice == "south":
		knights()
	else:
		dead("You wear out your welcome with the trolls and they eat you.")

# Fledd Mountains Function
def fledd():
	print "These mountains are impassable, you must turn around."
	print "Would you like to go back? 'y' or 'n'."
	choice = raw_input("> ")
	if choice == "y":
		print "You are now back where you started."
		start2()
	else:
		dead("You remain here until you starve to death.")
		
# Dragon's Lair function
def dragon():
	#if dragon_alive:
	print "This is the great mountain lair of the fearsome dragon!"
	print "Would you like to go back? y or n"
	choice = raw_input("> ")
	if choice ==  "y":
		print "You are now back where you started."
		start2()
	else:
		print "You have awakened the dragon, prepare to fight!"
		dicerolldragon()
	#if not dragon_alive:	
	print "Would you like to head 'south' to the lake, or \n'west' back to where you came from?"
	choice = raw_input("> ")
	if choice == "west":
		start2()
	elif choice == "south":
		lake()
	else:
		dead("You wander around the dragon's lair until you starve.")

# Make this into a function to be called.
# Now do a d6 dice roll for battle.
def dicerolldragon():
	#global dragon_alive
	d6dragon = random.randint(1, 6)
	print "The dragon has rolled a: %d" % d6dragon
	d6you = random.randint(1, 6)
	print "You have rolled a: %d" % d6you
	if d6dragon > d6you:
		dead("The dragon got to you first and scorched you with fire.")
	elif d6dragon == d6you:
		print "You have both attacked at the same time resulting in a draw."
		dicerolldragon()
	else:
		print "You have slain the beast with one mighty blow!"
		#return not dragon_alive
		
def badlands():
	print "You have entered the badlands. Be wary of bandits!"
	randencounter = random.randint(1, 6)
	if randencounter >= 3:
		randbandit()
		dicerollbandit()
	else:
		print "The area seems clear of danger."
		print "Would you like to continue on 'east' to the High plains, or \n'south' to the Land of the Black Knights?"
		choice = raw_input("> ")
		if choice == "east":
			highplains()
		elif choice == "south":
			knights()
		else:
			dead("You wander around the badlands till you die of thirst.")
			
# random attack of creature.			
def dicerollbandit():
	d6bandit = random.randint(1, 6)
	d6you = random.randint(1, 6)
	if d6bandit == d6you:
		print "You continue to travel through this harsh and unforgiving terrain."
		start3()
	elif d6bandit > d6you:
		print "A figure jumps out from behind a large rocky outcropping and surprises you."
		dicerollbandit2()
	else:
		print "You spot the figure hiding behind a large rocky outcropping."
		print "What do you want to do? 'attack' or 'flee' back the way you came."
		choice = raw_input("> ")
		if choice == "attack":
			dicerollbandit2()
		elif choice == "flee":
			start2()
		else:
			death("Your hesitation has cost you your life.")
			
# Second dice roll interaction with bandit. There has got to be a better way to set up the functions so that I don't keep repeating myself.
def dicerollbandit2():
	d6bandit = random.randint(1, 6)
	print "The attacker has rolled a: %d" % d6bandit
	d6you = random.randint(1, 6)
	print "You have rolled a: %d" % d6you
	if d6bandit > d6you:
		dead("The attacker got to you first and cut you down.")
	elif d6bandit == d6you:
		print "You have both attacked at the same time resulting in a draw."
		dicerollbandit2()
	else:
		print "You have slain the attacker with one mighty blow!" 
		start3()
		
def dicerollknight():
	d6knight = random.randint(1, 6)
	print "The attacker has rolled a: %d" % d6knight
	d6you = random.randint(1, 6)
	print "You have rolled a: %d" % d6you
	if d6knight > d6you:
		dead("The attacker got to you first and cut you down.")
	elif d6knight == d6you:
		print "You have both attacked at the same time resulting in a draw."
		dicerollknight()
	else:
		print "You have slain the attacker with one mighty blow!" 
		print "Would you like to go 'north' to Troll Town, or \n'east' to the lake?"
		choice = raw_input("> ")
		if choice == "north":
			trolltown()
		elif choice == "east":
			lake()
		else:
			dead("You wander around until you starve.")
			
def highplains():
	print "You have reached the High plains."
	print "This area is the headwaters of the rivers which flow into the lake."
	print "You feel that there is a growing magical energy in this area."
	# try setting up a random spawn of a monster here.
	# something like: generate a random number, then use that as a key to query a list, then use that list item to call the monster's function.
	randmonster()
	print "Would you like to 'attack' or 'flee'?"
	choice = raw_input("> ")
	if choice == "attack":
		dicerollmonster1()
	elif choice == "flee":
		start3()
	else:
		dead("Your hesitation has cost you your life.")

def dicerollmonster1():
	d6monster = random.randint(1, 6)
	print "The monster has rolled a: %d" % d6monster
	d6you = random.randint(1, 6)
	print "You have rolled a: %d" % d6you
	if d6monster > d6you:
		dead("The monster got to you first and destroyed you.")
	elif d6monster == d6you:
		print "You have both attacked at the same time resulting in a draw."
		dicerollmonster1()
	else:
		print "You have slain the beast with one mighty blow!"
		start4()

def dicerollmonster2():
	d6monster = random.randint(1, 6)
	print "The monster has rolled a: %d" % d6monster
	d6you = random.randint(1, 6)
	print "You have rolled a: %d" % d6you
	if d6monster > d6you:
		dead("The monster got to you first and destroyed you.")
	elif d6monster == d6you:
		print "You have both attacked at the same time resulting in a draw."
		dicerollmonster2()
	else:
		print "You have slain the beast with one mighty blow!"
		start5()	
		
def knights():
	print "You have reached the land of the Black Knights."
	print "Be wary, these knights are not friendly, they may attack at random."
	print "You still feel a growing magical energy in this area."
	diceroll = random.randint(1, 6)
	#print diceroll # for testing purposes
	if diceroll <= 3:
		print "The streets are quiet. You proceed with caution."
		print "You continue on to the lake."
		lake()
	elif diceroll == 4:
		print "You have stepped into a teleportation trap. You return to the High plains."
		highplains()
	else:
		randknight()
		print "Would you like to 'attack' or 'flee'?"
		choice = raw_input("> ")
		if choice == "attack":
			dicerollknight()
		elif choice == "flee":
			start3()
		else:
			dead("Your hesitation has cost you your life.")

def trolltown():
	print "You have entered Troll Town."
	print "The trolls here are eyeing you with suspicion, and a glint of hatred fills their eyes."
	print "A well dressed and well armed troll approaches you."
	trollchief()

# The enchanted lake
def lake():
	print "You have arrived at a large and beautiful lake."
	print "You feel an intense magical energy all around you."
	print "There is a strange feeling of danger, but it is not distinct."
	waterytart()

# List of Monsters to be randomly spawned.
# Monster 1, Monster 2, Monster 3
def randmonster():
	monsters = ['orc', 'kobold', 'werewolf']
	print "A random %r has crossed paths with you." % (random.choice(monsters)) 
	return(random.choice(monsters))

# Random list of human enemies to be randomly spawned.
# Bandit 1, Bandit 2, Bandit 3
def randbandit():
	bandits = ['thief', 'assassin', 'barbarian']
	print "A random %r has been spotted by you." % (random.choice(bandits))
	return (random.choice(bandits))
	
# Knight 1, Knight 2, Knight 3	
def randknight():
	knights = ['Black Knight captain', 'Black Knight corporal', 'Black Knight general']
	print "A %r has challenged you." % (random.choice(knights))
	return(random.choice(knights))
	
# Maiden of the Lake
def waterytart():
	print "Suddenly, woman's voice arises from the lake."
	print "You have disturbed my sleep, mortal. What is it you desire?\n'power'? \n'wealth'? \n'peace'? \n'war'?"
	choice = raw_input("> ")
	if choice == "power":
		dead("You are just another corrupt mortal. Die!")
	elif choice == "wealth":
		dead("You are just another greedy mortal. Die!")
	elif choice == "war":
		dead("You are just another vengeful and violent mortal. Die!")
	else:
		print "You are a worthy mortal. You have earned my favor."
		print "---A watery tart throws a sword at you!---"
		winner()
		print "Would you like to play again? 'y' or 'n'."
		choice = raw_input("> ")
		if choice == "y":
			start()
		else:
			exit(0)
			
def trollchief():
	print "The troll chief would like to challenge you to a guessing game."
	print "Do you accept? 'y' or 'n'."
	choice = raw_input("> ")
	if choice == 'y':
		numguessgame()
	else:
		print "Awww, you're no fun!"
		trolltown()
		
def numguessgame():
	guessestaken = 0
	randnum = random.randint(1, 100)
	print "The troll king says, 'I'm thinking of a number between 1 and 100.'"
	print "'You must guess the number in 5 attempts in order to pass.'"
	print "'If you fail, you will fight a random creature.'"
	print "'If you pass you will be teleported to the lake.'"
	while guessestaken < 6:
		print "What is your guess?"
		guess = int(raw_input())
		guessestaken += 1
		
		if guess < randnum:
			print "Your guess is too low."
			
		elif guess > randnum:
			print "Your guess is too high."
			
		elif guess == randnum:
			print "You have guessed the number."
			print "You may pass!"
			lake()
			break
		else:
			randmonster()
			print "Would you like to 'attack' or 'flee'?"
			choice = raw_input("> ")
			if choice == "attack":
				dicerollmonster2()
			elif choice == "flee":
				start4()
			else:
				dead("Your hesitation has cost you your life.")
			
	if guessestaken >= 6:
		randmonster()
		print "Would you like to 'attack' or 'flee'?"
		choice = raw_input("> ")
		if choice == "attack":
			dicerollmonster2()
		elif choice == "flee":
			start4()
		else:
			dead("Your hesitation has cost you your life.")
		
# Dead function
def dead(reason):
	print reason, "\nYou have passed through the field of reeds, and are of this earth no more."
	# Insert an option to restart the game from the beginning, or just quit the game.
	print "Would you like to play again? 'y' or 'n'."
	choice = raw_input("> ")
	if choice == "y":
		start()
	else:
		exit(0)

# Winner screen
def winner():
	print "*****************************************************************"
	print "You have acquired the great sword \'Rex Calibur\'."
	print "You have been crowned King of the Land for the remainder of your days."
	print "You go on to do many great things in the world."
	print "You are the Champion of the People!"
	print "*****************************************************************"
	
start()
# 