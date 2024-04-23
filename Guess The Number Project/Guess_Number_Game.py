#!/usr/bin/env python
# coding: utf-8

# In[7]:


# This is Guess The Number Game

import random

# Prompt the user the range of the guessing number
top_of_range = input("Type a number: ")

# Input integer handling
if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    
    if top_of_range <= 0:
        print("Please type a number larger than 0 next time")
        quit()
        
else:
    print("Please type a number next time")
    quit()
    

# Randomize the number
random.number = random.randint(0, top_of_range)

# Start guessing the randomize number
while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    
    if user_guess.isdigit():
        user_guess = int(user_guess)
    
    else:
        print("Please type a number next time")
        continue
        
    if user_guess == random.number:
        print("You got it!")
        break
        
    elif user_guess > random_number:
        print("You were above the number!")
        
    else:
        print("You were below the number!")
        

        
# Show the number of guesses it took the guess the number
print("You got it in," guesses, "guesses")    
print(random.number)


# In[ ]:




