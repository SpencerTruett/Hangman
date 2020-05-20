import time
import random

print( "Time to play hangman!")

print("Start guessing...")
time.sleep(0.5)


with open('sowpods.txt') as f:
	words = list(f)

word = random.choice(words).strip().lower()


guesses = ''

turns = 10


#check if the turns are more than zero
while turns > 0:         

    failed = 0             
   
    for char in word:      

        if char in guesses:    

            print(char, end = ' ')

        else:

            print("_ ", end = ' ')     

            failed += 1    


    if failed == 0:        
        print("    You won")

        break              

    guess = input("   Guess a letter:") 

    guesses += guess                    


    if guess not in word:  

        turns -= 1        

        print("Wrong")    

        print ("You have", + turns, 'more guesses' )

        if turns == 0:           
            print("The word was " + word)
            print("You Lose")