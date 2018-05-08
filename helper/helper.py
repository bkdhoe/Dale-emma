import time
import random
import threading
import string

HEALTH = 4

def print_title():
    print("\n" * 10)
    print("                                                     ******************************")
    print("                                                     ******************************")
    print("                                                     ****                      ****")
    print("                                                     ****    Brian Donahoe     ****")
    print("                                                     ****      Presents        ****")
    print("                                                     ****                      ****")
    print("                                                     ******************************")
    print("                                                     ******************************")
    print("")
    time.sleep(3)
    print(
        "                   _____   _                ____            _                                                                             ")
    print(
        "                  |_   _| | |__     ___    |  _ \    __ _  | |   ___            ___   _ __ ___    _ __ ___     __ _   _                   ")
    print(
        "                    | |   | '_ \   / _ \   | | | |  / _` | | |  / _ \  _____   / _ \ | '_ ` _ \  | '_ ` _ \   / _` | (_)                  ")
    print(
        "                    | |   | | | | |  __/   | |_| | | (_| | | | |  __/ |_____| |  __/ | | | | | | | | | | | | | (_| |  _                   ")
    print(
        "                    |_|   |_| |_|  \___|   |____/   \__,_| |_|  \___|          \___| |_| |_| |_| |_| |_| |_|  \__,_| (_)                  ")
    print(
        "                                                                                                                                          ")
    print(
        "  ____                             _                                 ____                  _                      _                          ")
    print(
        " | __ )    __ _   ___    ___    __| |     ___    _ __       __ _    |  _ \    ___   _ __  | | __   ___      ___  | |_    ___    _ __   _   _ ")
    print(
        " |  _ \   / _` | / __|  / _ \  / _` |    / _ \  | '_ \     / _` |   | |_) |  / _ \ | '__| | |/ /  / _ \    / __| | __|  / _ \  | '__| | | | |")
    print(
        " | |_) | | (_| | \__ \ |  __/ | (_| |   | (_) | | | | |   | (_| |   |  _ <  |  __/ | |    |   <  | (_) |   \__ \ | |_  | (_) | | |    | |_| |")
    print(
        " |____/   \__,_| |___/  \___|  \__,_|    \___/  |_| |_|    \__,_|   |_| \_\  \___| |_|    |_|\_\  \___/    |___/  \__|  \___/  |_|     \__, |")
    print(
        "                                                                                                                                       |___/ ")
    time.sleep(2)
    print("")
    input("                                                        Press ENTER KEY to begin.                      \n\n")


def fight(start, hit, win, rounds):
    print("\n" + start + " Make sure CAPS LOCK is on. Type quickly, no spaces.")
    input("Press ENTER KEY when ready to fight!")

    ### battleCycle(type, time, time2, total, clock, S, HIT) ##########
    cycles = 0
    while cycles < rounds:
        a = random.choice(string.ascii_uppercase)
        b = random.randrange(1, 9)
        battle_cycle(str(a), str(b), b, b, b, "s", hit)
        cycles += 1

    ################################################################

    if HEALTH > 0:
        print(win)
    if HEALTH <= 0:
        print("Game Over.")


def battle_cycle(type, tm, tm2, total, clock, s, otro):
    global HEALTH
    global TAKE_DAMAGE
    if HEALTH > 0:
        def take_damage():
            global HEALTH
            HEALTH -= 1
            if timeout == 1:
               print("\n")
            print(otro)
            if timeout == 1 and HEALTH != 0:
                print("Finish the above command.")
            if HEALTH == 0:
                time.sleep(1)
                print("\nYou die.")
        timeout = 1
        t = threading.Timer(clock, take_damage)
        t.start()
        k = input("\nType '" + type + "' " + tm + " tm" + s + ". Then press ENTER KEY. ").upper()
        if len(k) == total and k.count(type) == tm2:
            print("SUCCESS")
            t.cancel()
            timeout = 0
        else:
            t.cancel()
            timeout = 0
            take_damage()
        time.sleep(1)
