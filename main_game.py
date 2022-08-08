import os
import random
import time
from colorama import Fore, Style


def red(a):
    print(Fore.RED + "\033[1m{} \033[1m".format(a))


def cyan(a):
    print(Fore.CYAN + "\033[1m{} \033[1m".format(a))


def yellow(a):
    print(Fore.YELLOW + "\033[1m{} \033[1m".format(a))


def green(a):
    print(Fore.GREEN + "\033[1m{} \033[1m".format(a))


def player1_lost(p1, p2):
    death = random.randint(1, 3)
    print(Style.RESET_ALL)
    if death == 1:
        cyan("_________________________________________________________________")
        print(f"I did not expected that!! {p2} knocked out {p1} with a vital blow....{p2} wins :o")
        print(Style.RESET_ALL)
    elif death == 2:
        cyan("_________________________________________________________________")
        print(f"With an upper cut {p2} throws {p1} out of the ring... {p2} wins :)")
        print(Style.RESET_ALL)
    else:
        cyan("_________________________________________________________________")
        print(f"{p2} clinches victory!! :) as {p1} could'nt stand up and lies on the ground :( ")
        print(Style.RESET_ALL)


def player2_lost(p1, p2):
    death = random.randint(1, 3)
    print(Style.RESET_ALL)
    if death == 1:
        yellow("_________________________________________________________________")
        print(f"I did not expected that!! {p1} knocked out {p2} with a vital blow....{p1} wins :o")
        print(Style.RESET_ALL)
    elif death == 2:
        yellow("_________________________________________________________________")
        print(f"With an upper cut {p1} throws {p2} out of the ring.... {p1} wins :)")
        print(Style.RESET_ALL)
    else:
        yellow("_________________________________________________________________")
        print(f"{p1} clinches victory!! :) as {p2} could'nt stand up and lies on the ground :(")
        print(Style.RESET_ALL)


def resign1_lost(p1, p2):
    cyan("_________________________________________________________________")
    print(f"{p1} withdrew, {p2} wins")
    print(Style.RESET_ALL)


def resign2_lost(p1, p2):
    yellow("_________________________________________________________________")
    print(f"{p2} withdrew, {p1} wins")
    print(Style.RESET_ALL)


def damage_max_p2():
    ask = random.randint(1, 3)
    if ask == 1:
        print(f"{p2} lands a game-ending hit on {p1} dealing {impact} damage!")
    elif ask == 2:
        print(f"{p2} lands a dangerous hit on {p1} dealing {impact} damage!")
    else:
        print(f"{p2} lands a painful hit on {p1} dealing {impact} damage!")


def damage_min_p2():
    ask = random.randint(1, 2)
    if ask == 1:
        print(f"{p2} lands an ordinary blow on {p1} dealing mere {impact} damage!")
    elif ask == 2:
        print(f"{p2} lands a weak hit on {p1} dealing {impact} damage!")


def damage_max_p1():
    ask = random.randint(1, 3)
    if ask == 1:
        print(f"{p1} lands a game-ending hit on {p2} dealing {impact1} damage!")
    elif ask == 2:
        print(f"{p1} lands a dangerous hit on {p2} dealing {impact1} damage!")
    else:
        print(f"{p1} lands a painful hit on {p2} dealing {impact1} damage!")


def damage_min_p1():
    ask = random.randint(1, 2)
    if ask == 1:
        print(f"{p1} lands an ordinary blow on {p2} dealing mere {impact1} damage!")
    elif ask == 2:
        print(f"{p1} lands a weak hit on {p2} dealing {impact1} damage!")

def defence_player2():
    ask = random.randint(1, 2)
    if ask == 1:
        print(f"{p2} tries to defend")
    elif ask == 2:
        print(f"{p2} is trying to play defensive")

def defence_player1():
    ask = random.randint(1, 2)
    if ask == 1:
        print(f"{p1} tries to defend")
    elif ask == 2:
        print(f"{p1} is trying to play defensive")

os.system('cls')
time.sleep(1.5)
red("\t\t\t\t\t\t\t\t\tWELCOME TO")
time.sleep(3)
os.system('cls')
red("\n\n\n\n\t\t\t\t\t\t\t\t\tFIGHT TO DEATH!!\n\n\n\n\n")
print(Style.RESET_ALL)
time.sleep(1)
input("Press enter to continue...")
os.system('cls')
green("\t\t\t\t\t\t\t\t\tINSTRUCTIONS\n\n")
print(Style.RESET_ALL)
print("1. This is a 2 player game....\n"
      "2. You will have 3 options...\n\t"
      "a) punch - This will deal damage based on your response time and if the enemy tries to defend\n\t"
      "b) defend - This will reduce your enemy's next attack\n\t"
      "c) end - You can end the game if you think you cant win now and victory will be handed over to the enemy\n"
      "3. Type as fast as you can to deal more damage\n"
      "4. The game is totally unbiased....enjoy ;)\n\n\n")
time.sleep(3)
input("Press enter to continue...")
os.system('cls')
play = 'y'

while (play == 'y' or play == 'Y'):
    health1 = 100
    health2 = 100
    attack1 = 'punch'
    attack2 = 'punch'
    p1 = input("Enter player1 name:\n")
    p2 = input("Enter player2 name:\n")
    pc = random.randint(1, 2)
    while attack1 != 'end' or attack1 != 'END' or attack2 != 'end' or attack2 != 'END':
        if pc == 2:  # player2
            cyan("_________________________________________________________________")
            start = time.time()
            attack1 = input(f"{p2}, what do you want to do?\npunch, defend, end\n")
            print(Style.RESET_ALL)
            end = time.time()
            elapsed = end - start
            if attack1 == 'end':
                resign2_lost(p1, p2)
                break
            elif attack1 == 'punch' or attack1 == 'PUNCH':
                if elapsed <= 3 and attack2 != 'defend':
                    impact = random.randint(20, 60)
                    remain1 = health1 - impact
                    health1 = remain1

                    if impact > 45:
                        damage_max_p2()
                    elif impact < 25:
                        damage_min_p2()
                    else:
                        print(f"{p2} lands normal hit on {p1} dealing {impact} damage")

                    if health1 <= 0:
                        print(f"{p1} is left with 0 health")
                        player1_lost(p1, p2)
                        break

                    else:
                        print(f"{p1} is left with {health1} hp")

                elif elapsed > 3 or attack2 == 'defend' or attack2 == 'DEFEND':
                    impact = random.randint(10, 40)
                    remain1 = health1 - impact
                    health1 = remain1

                    if impact < 25:
                        damage_min_p2()
                    else:
                        print(f"{p2} lands normal hit on {p1} dealing {impact} damage")

                    if health1 <= 0:
                        print(f"{p1} is left with 0 health")
                        player1_lost(p1, p2)
                        break

                    else:
                        print(f"{p1} is left with {health1} hp")

                else:
                    impact = random.randint(10, 55)
                    remain1 = health1 - impact
                    health1 = remain1

                    if impact > 45:
                        damage_max_p2()
                    elif impact < 25:
                        damage_min_p2()
                    else:
                        print(f"{p2} lands normal hit on {p1} dealing {impact} damage")

                    if health1 <= 0:
                        print(f"{p1} is left with 0 health")
                        player1_lost(p1, p2)
                        break

                    else:
                        print(f"{p1} is left with {health1} hp")

            elif attack1 == 'defend':
                attack1 = 'defend'
                defence_player2()
            else:
                print("BAD CHOICE!!.....Your are skipped :/")
            yellow("_________________________________________________________________")
            start1 = time.time()  # player1
            attack2 = input(f"{p1}, what do you want to do?\npunch,defend,end\n")
            print(Style.RESET_ALL)
            end1 = time.time()
            elapsed1 = end1 - start1
            if attack2 == 'end':
                resign1_lost(p1, p2)
                break

            elif attack2 == 'punch' or attack2 == 'PUNCH':
                if elapsed1 <= 3 and attack1 != 'defend':
                    impact1 = random.randint(20, 60)
                    remain2 = health2 - impact1
                    health2 = remain2

                    if impact1 > 45:
                        damage_max_p1()
                    elif impact1 < 25:
                        damage_min_p1()
                    else:
                        print(f"{p1} lands normal hit on {p2} dealing {impact1} damage")

                    if health2 <= 0:
                        print(f"{p2} is left with 0 health")
                        player2_lost(p1, p2)
                        break

                    else:
                        print(f"{p2} is left with {health2} hp")


                elif elapsed1 > 3 or attack1 == 'defend' or attack1 == 'DEFEND':
                    impact1 = random.randint(10, 40)
                    remain2 = health2 - impact1
                    health2 = remain2

                    if impact1 < 25:
                        damage_min_p1()
                    else:
                        print(f"{p1} lands normal hit on {p2} dealing {impact1} damage")

                    if health2 <= 0:
                        print(f"{p2} is left with 0 health")
                        player2_lost(p1, p2)
                        break

                    else:
                        print(f"{p2} is left with {health2} hp")


                else:
                    impact1 = random.randint(10, 55)
                    remain2 = health2 - impact1
                    health2 = remain2

                    if impact1 > 45:
                        damage_max_p1()
                    elif impact1 < 25:
                        damage_min_p1()
                    else:
                        print(f"{p1} lands normal hit on {p2} dealing {impact1} damage")

                    if health2 <= 0:
                        print(f"{p2} is left with 0 health")
                        player2_lost(p1, p2)
                        break

                    else:
                        print(f"{p2} is left with {health2} hp")


            elif attack2 == 'defend':
                attack2 = 'defend'
                defence_player1()

            else:

                print("BAD CHOICE!!...You are skipped :/")
        else:
            yellow("_________________________________________________________________")
            start1 = time.time()  # player1
            attack2 = input(f"{p1}, what do you want to do?\npunch,defend,end\n")
            print(Style.RESET_ALL)
            end1 = time.time()
            elapsed1 = end1 - start1
            if attack2 == 'end':
                resign1_lost(p1, p2)
                break

            elif attack2 == 'punch' or attack2 == 'PUNCH':
                if elapsed1 <= 3 and attack1 != 'defend':
                    impact1 = random.randint(20, 60)
                    remain2 = health2 - impact1
                    health2 = remain2

                    if impact1 > 45:
                        damage_max_p1()
                    elif impact1 < 25:
                        damage_min_p1()
                    else:
                        print(f"{p1} lands normal hit on {p2} dealing {impact1} damage")

                    if health2 <= 0:
                        print(f"{p2} is left with 0 health")
                        player2_lost(p1, p2)
                        break

                    else:
                        print(f"{p2} is left with {health2} hp")


                elif elapsed1 > 3 or attack1 == 'defend' or attack1 == 'DEFEND':
                    impact1 = random.randint(10, 40)
                    remain2 = health2 - impact1
                    health2 = remain2

                    if impact1 < 25:
                        damage_min_p1()
                    else:
                        print(f"{p1} lands normal hit on {p2} dealing {impact1} damage")

                    if health2 <= 0:
                        print(f"{p2} is left with 0 health")
                        player2_lost(p1, p2)
                        break

                    else:
                        print(f"{p2} is left with {health2} hp")


                else:
                    impact1 = random.randint(10, 55)
                    remain2 = health2 - impact1
                    health2 = remain2

                    if impact1 > 45:
                        damage_max_p1()
                    elif impact1 < 25:
                        damage_min_p1()
                    else:
                        print(f"{p1} lands normal hit on {p2} dealing {impact1} damage")

                    if health2 <= 0:
                        print(f"{p2} is left with 0 health")
                        player2_lost(p1, p2)
                        break

                    else:
                        print(f"{p2} is left with {health2} hp")

            elif attack2 == 'defend':
                attack2 = 'defend'
                defence_player1()
            else:
                print("BAD CHOICE!!...You are skipped :/")
            cyan("_________________________________________________________________")
            start = time.time()  # player2
            attack1 = input(f"{p2}, what do you want to do?\npunch,defend,end\n")
            print(Style.RESET_ALL)
            end = time.time()
            elapsed = end - start
            if attack1 == 'end':
                resign2_lost(p1, p2)
                break
            elif attack1 == 'punch' or attack1 == 'PUNCH':
                if elapsed <= 3 and attack2 != 'defend' :
                    impact = random.randint(20, 60)
                    remain1 = health1 - impact
                    health1 = remain1

                    if impact > 45:
                        damage_max_p2()
                    elif impact < 25:
                        damage_min_p2()
                    else:
                        print(f"{p2} lands normal hit on {p1} dealing {impact} damage")

                    if health1 <= 0:
                        print(f"{p1} is left with 0 health")
                        player1_lost(p1, p2)
                        break

                    else:
                        print(f"{p1} is left with {health1} hp")

                elif elapsed > 3 or attack2 == 'defend' or attack2 == 'DEFEND':
                    impact = random.randint(10, 40)
                    remain1 = health1 - impact
                    health1 = remain1

                    if impact < 25:
                        damage_min_p2()
                    else:
                        print(f"{p2} lands normal hit on {p1} dealing {impact} damage")

                    if health1 <= 0:
                        print(f"{p1} is left with 0 health")
                        player1_lost(p1, p2)
                        break

                    else:
                        print(f"{p1} is left with {health1} hp")

                else:
                    impact = random.randint(10, 55)
                    remain1 = health1 - impact
                    health1 = remain1

                    if impact > 45:
                        damage_max_p2()
                    elif impact < 25:
                        damage_min_p2()
                    else:
                        print(f"{p2} lands normal hit on {p1} dealing {impact} damage")

                    if health1 <= 0:
                        print(f"{p1} is left with 0 health")
                        player1_lost(p1, p2)
                        break

                    else:
                        print(f"{p1} is left with {health1} hp")

            elif attack1 == 'defend':

                attack1 = 'defend'

                defence_player2()

            else:

                print("BAD CHOICE!!.....Your are skipped :/")

    play = input("Do you want to play again? y/n\n")
    if play == 'y' or play == 'Y':
        os.system('cls')

    else:
        break
print(Style.RESET_ALL)
green("THANK YOU ;)")
print(Style.RESET_ALL)