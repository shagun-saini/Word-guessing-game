#Word guessing game project.
import random

words=["Articles","World","Fruits","Vegetables","Antartic","Ameliorate",
       "Finding","Dream","Developer","Particular","Searching","Individual"]

guessing_game=random.choice(words)
while True:
  guesing_word=input("Write the guessing word")

  if guesing_word==guessing_game:
    print("Congratulation, your guessing word is correct")
    break
  else:
    print("Sorry") 