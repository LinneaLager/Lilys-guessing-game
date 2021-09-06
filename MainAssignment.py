#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def PrintScore():

	with open("score.txt", 'r') as f:
		Scores = [line.strip().split(" ") for line in f]

	ScoresSorted = sorted(Scores, key=lambda x: int(x[1]))

	for elem in ScoresSorted:
		print(str(elem)) 

def main():
	"""When running this script is the main module"""
	if __name__ == "__main__":
		main()

import random
import sys

print("Welcome To Lily's Guessing Game")
print("If you want to leave type close")

name = input("If you want to continue and play then please enter your prefered username: ")  
if  name == "close":
	print("Thank you for playing!")
	sys.exit()

x = random.randint(0, 20)

#Creates random number between
#an interval

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
	# Condition testing
	if x == guess:
		print("Congratulations you did it in ",
			count, " try")
		# Once guessed, loop will break if answer is no
		file = open("score.txt","a")
		a = name
		b = " "
		c = str(count)
		file.write(a+b+c+"\n")
		file.close()
		#set count to 0 after correct guess
		count = 0
		print("High Scores:")
		PrintScore()
		answer = (input("Do you want to play again? Type yes or no: "))
		if answer == "yes":
			x = random.randint(0, 20)
			continue
		elif answer == "no":
			print("Thank you for playing!")
			sys.exit()
			
	elif x > guess:
		print("You guessed too small!")
	elif x < guess:
		print("You Guessed too high!")
	


# In[ ]:




