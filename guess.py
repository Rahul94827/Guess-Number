
import random

def ab(guess,comp):
  
  if guess<comp:
    print("Too low\n")
  if guess>comp:
    print("Too high\n")
    
    
print("Welcome to the number guessing game")
difficulty=input("I'm thinking of a number between 1 and 100.Choose a difficulty. Type 'easy' or 'hard'\n")

comp=random.randint(0,101)
flag=True
easy_flag=10
hard_flag=5
while flag:
  if difficulty=='easy':
    print(f"You have {easy_flag} attempts left to guess the number")
    guess=int(input("Guess a number :"))
    
    ab(guess,comp)
    easy_flag-=1
    if guess==comp:
      print(f"You got it the answer is {guess}")
      break
    if easy_flag==0:
      print(f"You failed to guess,the correct answer is {comp}")
      flag=False
    print("Guess again\n")
  else:
  
    print(f"You have {hard_flag} attempts left to guess the number")
    guess=int(input("Guess a number :"))
    
    ab(guess,comp)
    hard_flag-=1
    if guess==comp:
      print(f"You got it the answer is {guess}")
      break
    if hard_flag==0:
      print(f"You failed to guess,the correct answer is {comp}")
      flag=False
    print("Guess again\n") 
