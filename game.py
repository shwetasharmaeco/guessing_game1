# print(identity_matrix(5))
from random import randint
name = input("What is your name > ").title()
print ("Hi" + " " + name)

print ("I am thinking a number between 1 to 100 \n Can you guess it?")


comp_num= randint(1,101)
count=1
while True:
   
    try:
        guess= int(input("What is your guess > "))
        if guess==comp_num:
            print(f"Well done {name}! You found my number in {count} tries")
            restart=input("would you like to play again: Y or N> ").upper()	
            if  restart=="Y":
            	comp_num= randint(1,101)
            	continue
            else:
            	print("Thanks for playing, see you next time")
            	break
        elif guess<1 or guess>100:
        	print("Only numbers between 1-100 allowed")
        elif guess < comp_num:
            print("Your guess is too low, try again.")
            count+=1
        elif guess > comp_num:
            print("Your guess is too high, try again.")
            count+=1
        
        
    except:
        print("Only numbers between 1-100 allowed")

	
