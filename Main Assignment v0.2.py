# *---- Imports ----*

import random
import sys

# *---- Functions ----*

def printscore():
	"""This function prints the score after a correct guess"""
	with open("score.txt", 'r') as f:
		scores = [line.strip().split(" ") for line in f]

	scoressorted = sorted(scores, key=lambda x: int(x[1]))

	for elem in scoressorted:
		print(str(elem))

def correctguess(tries, name):
	"""This function handles the correct guess"""
	print("Congratulations you did it in ", tries, " try")
	#Once guessed, loop will break if answer is no
	file = open("score.txt","a")
	a = name
	b = " "
	c = str(tries)
	file.write(a+b+c+"\n")
	file.close()
	print("High Scores:")
	printscore()

def main():
	"""When running this script is the main module thabd handles the guessing game logic"""

	#Prints welcome message
	print("Welcome To Lily's Guessing Game")
	print("If you want to leave type close")

	name = input("If you want to continue and play then please enter your prefered username: ")  
	"""Asks for input if input == close then sys.exit"""
	if  name == "close":
		print("Thank you for playing!")
		sys.exit()

	#Creates random number between an interval
	x = random.randint(0, 20)

	print("The number will be between 0 and 20")

	# Initializing the number of guesses.
	count = 0


	while  True:
		count += 1
		# taking guessing number as input
		guess = (input("Guess a number:- "))
	
		if  guess == "close":
			print("Thank you for playing!")
			sys.exit()
	
		#catch if not an integer
		try:
			guess = (int(guess))
		except:
			print("Please enter an integer")
			continue	
		#Condition testing
		if x == guess:
			correctguess(count, name)
			#Set count to 0 after correct guess
			count = 0
			answer = (input("Do you want to play again? Type yes if you'd like to: "))
			if answer == "yes":
				x = random.randint(0, 20)
				continue
			else:
				print("Thank you for playing!")
				sys.exit()
				
		elif x > guess:
			print("You guessed too small!")
		elif x < guess:
			print("You Guessed too high!")
  
# ---- Mainmethod ----
if __name__ == "__main__":
    main()

