#Word guessing game project.
import random

words=["Articles","World","Fruits","Vegetables","Antartic","Ameliorate",
       "Finding","Dream","Developer","Particular","Searching","Individual"]

guessing_game=random.choice(words)
word_failed=0
while True:
  guessing_word=input("Write the guessing word").strip()

  if guessing_word==guessing_game:
    print("Congratulation, your guessing word is correct")
    break
  else:
    print("Sorry") 
    word_failed+=1
    print("Failed",word_failed)