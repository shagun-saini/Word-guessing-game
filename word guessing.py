#Word guessing game project.
import random
while True:

 words=["Articles","World","Fruits","Vegetables","Antartic","Ameliorate",
       "Finding","Dream","Developer","Particular","Searching","Individual"]

 guessing_game=random.choice(words)

 guesing_word=input("Write the guessing word")

 if(guessing_game==words):
    print("Congratulation, your guessing word is correct")
    break
 else:
    print("Sorry")