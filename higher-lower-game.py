from art import logo, vs;
from game_data import data;
import os;
import random;

def clear():
   if os.name == 'nt':
      os.system('cls')
   else:
      os.system('clear')

def print_else(clear_function, logo, score):
   clear()
   print(logo)
   print(f"Sorry, that's wrong. Final score: {score}")
         
score = 0
flag = True

compareB = random.choice(data)


while flag:
   clear()
   print(logo)

   compareA = compareB
   compareB = random.choice(data)
   if compareA == compareB:
      compareB = random.choice(data)

   if score > 0:
      print(f"You're right! Current score: {score}")

   print(f"\nCompare A: {compareA['name']}, a {compareA['description']}, from {compareA['country']}\n")
   print(vs)
   print(f"\nAgainst B: {compareB['name']}, a {compareB['description']}, from {compareB['country']}\n")

   answer = input("Who has more followers? Type 'A' or 'B': ")

   followersA = compareA['follower_count']
   followersB = compareB['follower_count']

   if answer == "A":

      if followersA > followersB:
         score += 1
         continue
      else:
         print_else(clear(),logo, score)
         flag = False

   else:

      if followersB > followersA:
         score += 1
      else:
         print_else(clear(),logo, score)
         flag = False
