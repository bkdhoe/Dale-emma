
import time
import threading
import random
import string


def fight(START, HIT, WIN, ROUNDS):
    print("\n"+START+" Make sure CAPS LOCK is on. Type quickly, no spaces.")
    input("Press ENTER KEY when ready to fight!")
    
### battleCycle(TYPE, TIMES, TIMES2, TOTAL, CLOCK, S, HIT) ##########
    CYCLES = 0
    while CYCLES < ROUNDS:
        A = random.choice(string.ascii_uppercase)
        B = random.randrange(1, 9)
        battleCycle(str(A), str(B), B, B, 4, "s", HIT)
        CYCLES += 1
    
################################################################
    
    if health > 0:
        print(WIN)
    if health <= 0:
        print("Game Over.")
    
def battleCycle(TYPE, TIMES, TIMES2, TOTAL, CLOCK, S, OTRO):
    global health
    global takeDamage
    if health > 0:
        def takeDamage():
            global health
            health -= 1
            if timeout == 1:
               print("\n")
            print(OTRO)
            if timeout == 1 and health != 0:
                print("Finish the above command.")
            if health == 0:
                time.sleep(1)
                print("\nYou die.")
        timeout = 1
        t = threading.Timer(CLOCK, takeDamage)
        t.start()
        k = input("\nType '" +TYPE+ "' " +TIMES+ " time"+S+". Then press ENTER KEY. ")
        if len(k) == TOTAL  and k.count(TYPE) == TIMES2:
            print("SUCCESS")
            t.cancel()
            timeout = 0
        else:
            t.cancel()
            timeout = 0
            takeDamage()
        time.sleep(1) 
health = 4

## fight("Encounter", "When you're hit", "When you win")

########################################################################################

