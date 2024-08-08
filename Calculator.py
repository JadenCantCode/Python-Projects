import math
import random
import time

while True:
    print("Welcome to \"Calculator\"")
    time.sleep(3)
    print("What would you like to do?")
    time.sleep(2)
    print("""1: Use Calculator
    2: Exit""")

    while True: 
        start = input("Choice: ")
        if start == "1":
            print("You have chosen to use the calculator...")
            time.sleep(2)
            print("Correct? (Y/N)")
            time.sleep(2)
            calc = input("Choice: ")
            if calc == ("N", "n"):
                print("Returning to choice...")
                time.sleep(2)
                break


#NOT FINISHED!
