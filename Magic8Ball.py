import os
import time
import random
from tkinter import *
f = open("records.txt", "a")
x = 1
answer = ["Yeap", "Nope", "Maybe", "I don't know", "Doubtful", "Certainly", "Now is not the best time for me to tell you"]
while (x == 1):
    os.system("cls")
    print("You can only ask question with YES and NO answer only.\n")
    question = input("What is your question?\n")
    print("(Thinking...)")
    time.sleep(1)
    ans = answer[random.randint(0,6)]
    print(ans)
    time.sleep(1)
    f.write(question)
    f.write(ans +"\n")
    repeat = input("\nRepeat? Yes, No?")
    if (repeat == "y" or repeat == "Yes"):
        x = 1
    if ( repeat == "n" or repeat == "No"):
        x = 0

f.close()