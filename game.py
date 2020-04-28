"""A number-guessing game."""
from random import randint
name = input("What is your name > ").title()
print ("Hi" + " " + name)

print ("I am thinking a number between 1 to 100 \n Can you guess it?")


comp_num= randint(1,101)
print(comp_num)

count=0
while True:
	guess= int(input("What is your guess > "))
	if guess==comp_num:
		print(f"Well done {name}! You found my number in {count} tries")
		break
	elif guess < comp_num:
		print("Your guess is too low, try again.")
		count+=1
	elif guess > comp_num:
		print("Your guess is too high, try again.")
		count+=1
	else:
		print ("Invalid command/number")
