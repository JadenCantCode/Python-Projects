import time
import random

elY = ["Jaden: Rock","Jaden: Paper","Jaden: Scissors"]

print("Welcome to \"Totally Fair\" Rock Paper Scissors")
time.sleep(3)
print("You will be playing against Jaden")
time.sleep(3)
print("What is your name?")
time.sleep(2)
Name = input("Name: ")
print("Processing...")
time.sleep(3)
print("Would you like to start playing now,", Name+"?")
time.sleep(2)

while True:
    YN = input("Yes/No: ")
    if YN == "Yes":
        while True:
            print("Lets start!")
            time.sleep(2)
            print("Rock, Paper or Scissors. The choice is yours")
            time.sleep(2)
            Y = input("Answer: ")
            time.sleep(1)
            print("Rock")
            time.sleep(0.5)
            print("Paper")
            time.sleep(0.5)
            print("Scissors")
            time.sleep(0.5)
            print("Shoot!")
            time.sleep(0.1)
            print(Name+": "+Y)
            if Y == "Rock":
                print("Jaden: Paper")
                time.sleep(2)
                print("You lost!")
                exit()
            elif Y == "Paper":
                print("Jaden: Scissors")
                time.sleep(2)
                print("You lost!")
                exit()
            elif Y == "Scissors":
                print("Jaden: Rock")
                time.sleep(2)
                print("You lost!")
                exit()
            else:
                elY_random = random.choice(elY)
                print(elY_random)
                time.sleep(3)
                print("Jaden: What?")
                time.sleep(2)
                print("Jaden: Would you like to do that again?")
                while True:
                    again = input("Yes or No: ")
                    if again == "Yes":
                        break
                    elif again == "No":
                        print("Jaden: Okay :(")
                        exit()
                    else:
                        print("Choose either Yes or No(Case sensitive)")
    elif YN == "No":
        print("Okay :(")
        exit()
    else:
        print("Choose either Yes or No(Case sensitive)")