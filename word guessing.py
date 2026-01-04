#Word guessing game project.
import random

words=["Articles","World","Fruits","Vegetables","Antartic","Ameliorate",
       "Finding","Dream","Developer","Particular","Searching","Individual"]

guessing_game=random.choice(words)
Failed=0
while True:
  guesing_word=input("Write the guessing word").strip()

  if guesing_word==guessing_game:
    print("Congratulation, your guessing word is correct")
    Failed+=1
    print("Failed",Failed)
    break
  else:
    print("Sorry") 