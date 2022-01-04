import time
#options
option_A = ['A', 'a']
option_B = ['B', 'b']
option_C = ['C', 'c']
#objects
shotgun = 0
first_aid_kit = 0
#story
def intro():
    print("The year is 2167. The month unknown. The day unknown."
          "\nEarth has fallen into a zombie apocalypse, with very "
          "\nfew humans left. You are one of them. You have lost "
          "\nyour friends, in an area dominated by zombies and "
          "\nneed to escape.")
    time.sleep(1)
    print("You're walking down an alley, and a zombie appears around"
          "\na corner, but hasn't seen you yet...")
    time.sleep(1)
    print("Do you: "
          "\nA. slowly turn and walk away"
          "\nB. run away as fast as you can"
          "\nC. attack the zombie")
    choice = input(">>>")
    if choice in option_A:
        walk_away()
    elif choice in option_B:
        run_away()
    elif choice in option_C:
        print("You attack the zombie with no weapon and are eaten.")
    else:
        print("Required")
        intro()

def walk_away():
    print("Smart choice. The zombie doesn't notice you sneak off."
          "\nHowever you walk straight into the path of another!"
          "\nThe zombie sprints at you as fast as it can, and "
          "\nyou fall back in panic. Luckily you notice a shotgun "
          "\nlying beside you...")
    time.sleep(1)
    print("What do you do?")
    time.sleep(1)
    print("A. pick up the shotgun"
          "\nB. leave it and try to scramble to your feet to run")
    choice = input(">>>")
    if choice in option_A:
        shotgun = 1
    elif choice in option_B:
        shotgun = 0
    else:
        print("Required")
        walk_away()
    if shotgun > 0:
        print("You manage to get the shotgun and pull the trigger just as"
              "\nthe zombie looms over you, and kill it. Blood spattered over"
              "\nyour face, you rest for a moment then you get to your feet "
              "\nand start to jog. You see a safe house and dart towards it.")
        time.sleep(1)
        safe_house()
    else:
        print("You try to run away but can't run fast enough. The zombie "
              "\ngrabs you and rips off your limbs.")


def run_away():
    print("You turn and sprint away from the zombie, however he hears you"
          "\nand begins to chase after you. You're running as fast as you can"
          "\nas you approach a junction...")
    time.sleep(1)
    print("Do you:"
          "\nA. turn left"
          "\nB. turn right")
    choice = input(">>>")
    if choice in option_A:
        print("You run into a swarm of zombies and become trapped! "
              "\nThe zombies smother and kill you")
    elif choice in option_B:
        print("You see a safe house and sprint towards it, picking a shotgun"
              "up you see on the floor on the way.")
        safe_house()
    else:
        print("Required")
        run_away()

def safe_house():
    print("You make it to the safe house. A noise comes from the back of the "
          "\nhouse so you go to examine. The house is not so safe after all,"
          "\na zombie has broken in through the back!")
    time.sleep(1)
    print("Do you:"
          "\nA. shoot the zombie"
          "\nB. pick up the axe on the wall")
    choice = input(">>>")
    if choice in option_A:
        print("Your shotgun is empty! You can't defend yourself and the "
              "\nzombie kills you.")
    elif choice in option_B:
        print("You grab the axe and swing as the zombie charges. You kill "
              "\nthe zombie and manage to get out of the safe house and to "
              "\nsafety.")
    else:
        print("Required")
        safe_house()

print(intro())