import time

answer_A = ["A", "a"]
answer_B = ["B", "b"]

def intro():
    print("Hello! Welcome to the game of doors!")
    time.sleep(1)
    print("The aim of the game is to make it "
        "through the doors and answer the questions "
        "in order to make it out...")
    doors_1()

def doors_1():
    print("You see two doors in front of you. Door 1 is blue, "
          "door 2 is red. Which door do you pick? 1 or 2?")
    choice = input(">>>")
    if choice == "1":
        print("I hope you know your capitals..."
              "what is the capital of Japan?")
        time.sleep(1)
        print("A. Tokyo or B. Hiroshima?")
        choice = input(">>>")
        if choice in answer_A:
            doors_2a()
        if choice in answer_B:
            print("Incorrect! Game over")
    elif choice == "2":
        print("Time for some maths..."
              "what is the square root of 12.25?")
        time.sleep(1)
        print("A. 4.5 or B. 3.5")
        choice = input(">>>")
        if choice in answer_B:
            doors_2b()
        elif choice in answer_A:
            print("Wrong! End of game.")
        else:
            print("Not an option. Game over.")
    else:
        print("1 or 2?")
        doors_1()

def doors_2a():
    print("Well done, you were correct. Again, "
          "you see two doors in front of you. "
          "Do you pick door 1 or 2?")
    choice = input(">>>")
    if choice == "1":
        print("Question time! How many sides does an octagon have?")
        time.sleep(1)
        print("A. 16 or B. 8?")
        choice = input(">>>")
        if choice in answer_A:
            print("Better luck next time!")
        elif choice in answer_B:
            doors_3a()
        else:
            print("NOT AN OPTION. END OF GAME")
    if choice == "2":
        print("A tough one...what is the smallest country in "
              "the world (by landmass)?")
        time.sleep(1)
        print("A. Monaco or B. Vatican City?")
        choice = input(">>>")
        if choice in answer_A:
            print("Nope! Game over.")
        elif choice in answer_B:
            doors_3b()

def doors_2b():
    print("Correct!")
    time.sleep(1)
    print("But you were chased back to the start by a dwarf with an axe.")
    doors_1()

def doors_3a():
    print("The final door. The final question.")
    time.sleep(1)
    print("What is the name of the nearest galaxy to us?")
    time.sleep(1)
    print("A. Andromeda or B. Alpha Cenautri")
    choice = input(">>>")
    if choice in answer_A:
        print("Correct! You completed the game!")
    elif choice in answer_B:
        print("You fell at the final hurdle. Better luck next time...")
    else:
        print("Not an option. Idiot.")

def doors_3b():
    print("Well done, you answered correctly!")
    time.sleep(1)
    print("But you've hit a dead end...back to the start you go.")
    doors_1()

print(intro())
