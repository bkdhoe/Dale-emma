import time
import threading
import sys
import random
from helper import helper

weapon = 0

# Title Screen
helper.print_title()

# Game Begins

direction = ''
correct = 1
guesses = 0

print("\nOnly type in the capitalized word, in all caps. Caps Lock is suggested.\nYou are in a forest. Looking at a tree. With amnesia.")
while direction != correct or guesses <= 1:
    rand = random.choice([True, False])
    correct = "RIGHT" if rand else "LEFT"

    time.sleep(1)
    direction = input("You are lost, try to escape the woods. Go LEFT or RIGHT? ").upper()

    if direction == correct and guesses == 0:
        guesses += 1
        print("\nYou think the forest is getting brighter, and are the trees farther apart??")
    elif direction == correct and guesses == 1:
        print("\nYou made it out of the woods!")
        guesses += 1
    else:
        print("\nDoes that tree look familiar?? Keep trying.")
        
# Out of Woods

time.sleep(1)
direction = input("Now go toward the RIVER or the MOUNTAINS? ").upper()
time.sleep(1)
if direction == "RIVER":
    h = input("\nThe sun is begining to set, do you SPEED up your pace, or stay STEADY as you approach the river? ").upper()
    time.sleep(1)
    if h == "STEADY":
        print(
            "\nYou see a gleam in the grass. You approach and see a sword lying in the ground. +1 sword to your inventory!")
    direction = input("You see a fishing village. Go toward VILLAGE or INLAND? ").upper()
    time.sleep(1)
    while direction == "VILLAGE":
        direction = input(
            "\nA group of individuals in attered clothes are waiting at the edge of the village. Do you choose to ENTER or GO BACK? ").upper()
        time.sleep(1)
        if direction == "ENTER":
            direction = input("\nThe people fear you, staying out of your reach.").upper()
            time.sleep(1)
        elif direction == "GO BACK":
            direction = input("\nYou see a fishing village. Go toward VILLAGE or INLAND? ").upper()
            time.sleep(1)
elif direction == "MOUNTAINS":
    direction = input(
        "\nThe sun is begining to set, do you SPEED up your pace, or stay STEADY as you approach the mountains? ").upper()
    time.sleep(1)
    if direction == "STEADY":
        print(
            "\nYou see a gleam in the grass. You approach and see a sword lying in the ground. +1 sword to your inventory!")
        weapon += 1
    elif direction == "SPEED":
        print("")
    f = input("You see a ravine path cut through the mountains. Take the PATH or CLIMB the rough terrain? ").upper()
    time.sleep(1)
    if f == "PATH" or "CLIMB":
        g = input("\nA bush near you shakes, and out pops a bandit with a cudgel. Do you FIGHT or RUN? ").upper()
        time.sleep(2)

        # Fight Scenarios

        # FIGHT STEADY
        if g == "FIGHT" and weapon > 0:
            input("\nBe prepared to type quickly. Press ENTER KEY when ready to fight!")

            def kill():
                while True:
                    print(
                        "\n" * 4 + "You take too long to attack, the last thing you see is the bandit's club coming toward your head.\nGame Over.\n")
                    time.sleep(1)
                    sys.exit("Game Over. Thank you for playing 'The Dale-emma'.")

            t = threading.Timer(5, kill)
            t.start()
            k = input("\nType 5 'X''s. Then press ENTER KEY. ").upper()
            if len(k) == 5 and k.count("X") == 5:
                t.cancel()
                print("\nHIT")
                time.sleep(1)
            else:
                while True:
                    t.cancel()
                    print(
                        "\n" * 4 + "You try to hit him but miss, and the last thing you see is the bandit's club coming toward your head.\nGame Over.\n")
                    time.sleep(1)
                    sys.exit("Game Over. Thank you for playing 'The Dale-emma'.")
            print("\nYou successfully beat the bandit! +1 cudgel to inventory.")
            weapon += 1
            i = input(
                "You continue walking and eventually see a tavern in the distance.\nDo you ENTER or KEEP WALKING? ").upper()

        # FIGHT SPEED
        elif g == "FIGHT" and weapon < 1:
            print("\nYou brandish your fists, this will be a hard fight.")
            input("Be prepared to type quickly. Press ENTER KEY when ready to fight!")

            def kill():
                while True:
                    print(
                        "\n" * 4 + "You take too long to attack, the last thing you see is the bandit's club coming toward your head.\nGame Over.\n")
                    time.sleep(1)
                    sys.exit("Game Over. Thank you for playing 'The Dale-emma'.")

            t = threading.Timer(5, kill)
            t.start()
            k = input("\nType 5 'X''s. Then press ENTER KEY. ").upper()
            if len(k) == 5 and k.count("X") == 5:
                t.cancel()
                print("\nHIT")
                time.sleep(.8)
            else:
                t.cancel()
                print(
                    "\n" * 4 + "You try to hit him but miss, and the last thing you see is the bandit's club coming toward your head.\nGame Over.\n")
                sys.exit("Game Over. Thank you for playing 'The Dale-emma'.")
            u = threading.Timer(5, kill)
            u.start()
            l = input("\nType 6 'Y''s. Then press ENTER KEY. ").upper()
            if len(l) == 6 and l.count("Y") == 6:
                u.cancel()
                print("\nHIT")
                time.sleep(.8)
            else:
                u.cancel()
                print(
                    "\n" * 4 + "You try to hit him but miss, and the last thing you see is the bandit's club coming toward your head.\nGame Over.\n")
                time.sleep(1)
                sys.exit("Game Over. Thank you for playing 'The Dale-emma'.")
            v = threading.Timer(5, kill)
            v.start()
            m = input("\nType 4 'A''s. Then press ENTER KEY. ").upper()
            if len(m) == 4 and m.count("A") == 4:
                v.cancel()
                print("\nHIT")
                time.sleep(.8)
            else:
                v.cancel()
                print(
                    "\n" * 4 + "You try to hit him but miss, and the last thing you see is the bandit's club coming toward your head.\nGame Over.\n")
                sys.exit("Game Over. Thank you for playing 'The Dale-emma'.")
            print("\nYou successfully beat the bandit! +1 cudgel to inventory.")
            weapon += 1
            i = input(
                "\nYou continue walking and eventually see a tavern in the distance.\nDo you ENTER or KEEP WALKING? ").upper()

            # RUN PATH
        elif g == "RUN" and f == "PATH":
            input(
                "\nTo escape the bandit on the rough terrain you need to tread carefully! Press ENTER KEY when ready to run!")

            def kill():
                while True:
                    print(
                        "\n" * 4 + "You take too long to get away, the last thing you feel is the bandit's club on the back of your head.\nGame Over.\n")
                    time.sleep(1)
                    sys.exit("Game Over. Thank you for playing 'The Dale-emma'.")

            t = threading.Timer(5, kill)
            t.start()
            k = input("\nType 5 'X''s. Then press ENTER KEY. ").upper()
            if len(k) == 5 and k.count("X") == 5:
                print("\nSPRINT")
                t.cancel()
                time.sleep(1)
            else:
                while True:
                    t.cancel()
                    print(
                        "\n" * 4 + "You stumble and fall to the ground, the last thing you see is the bandit's club coming toward your head.\nGame Over.\n")
                    time.sleep(1)
                    sys.exit("Game Over. Thank you for playing 'The Dale-emma'.")
            i = input(
                "\nYou escape.\nYou continue walking and eventually see a tavern in the distance.\nDo you ENTER or KEEP WALKING? ").upper()

        # RUN CLIMB
        elif g == "RUN" and f == "CLIMB":
            input(
                "\nTo escape the bandit on the rough terrain you need to tread carefully! Press ENTER KEY when ready to run!").upper()

            def kill():
                while True:
                    print(
                        "\n" * 4 + "You take too long to get away, the last thing you feel is the bandit's club on the back of your head.\nGame Over.\n")
                    time.sleep(1)
                    sys.exit("Game Over. Thank you for playing 'The Dale-emma'.")

            t = threading.Timer(5, kill)
            t.start()
            k = input("\nType 5 'X''s. Then press ENTER KEY. ").upper()
            if len(k) == 5 and k.count("X") == 5:
                t.cancel()
                print("\nDODGE")
                time.sleep(.8)
            else:
                t.cancel()
                print(
                    "\n" * 4 + "You stumble and fall to the ground, the last thing you see is the bandit's club coming toward your head.\nGame Over.\n")
                sys.exit("Game Over. Thank you for playing 'The Dale-emma'.")
            u = threading.Timer(5, kill)
            u.start()
            l = input("\nType 6 'Y''s. Then press ENTER KEY. ").upper()
            if len(l) == 6 and l.count("Y") == 6:
                u.cancel()
                print("\nSIDE-STEP")
                time.sleep(.8)
            else:
                u.cancel()
                print(
                    "\n" * 4 + "You stumble and fall to the ground, the last thing you see is the bandit's club coming toward your head.\nGame Over.\n")
                sys.exit("Game Over. Thank you for playing 'The Dale-emma'.")
            v = threading.Timer(5, kill)
            v.start()
            m = input("\nType 4 'A''s. Then press ENTER KEY. ").upper()
            if len(m) == 4 and m.count("A") == 4:
                v.cancel()
                print("\nSPRINT")
                time.sleep(.8)
            else:
                v.cancel()
                print(
                    "\n" * 4 + "You stumble and fall to the ground, the last thing you see is the bandit's club coming toward your head.\nGame Over.\n")
                sys.exit("Game Over. Thank you for playing 'The Dale-emma'.")
            i = input(
                "\nYou escape the bandit and he loses your trail.\nYou continue walking and eventually see a tavern in the distance.\nDo you ENTER or KEEP WALKING? ").upper()
            # End of Fight Scenarios

    if i == "ENTER" and g == "FIGHT":
        print("\nYou enter the tavern. The four customers and bartender turn to look at you.")
        j = input(
            "They see the blood and dirt on your clothes from your fight earlier then turn back to their conversations.\nDo you STAY or LEAVE? ").upper()

    elif i == "ENTER" and g == "RUN":
        print("\nYou enter the tavern. The four customers and bartender turn to look at you.")
        j = input(
            "You see the biggest man nudge his nearly as large drinking buddy, but then everyone goes back to their conversations.\nDo you STAY or LEAVE? ").upper()

    elif i == "KEEP WALKING":
        print("\nYou keep walking past the tavern as the sun nears the hoizon.")

    if j == "LEAVE" or i == "KEEP WALKING":
        print(
            "\nAs you walk the sun starts to set. Night time noises envolope the forest...\nBut also the noise of footstep, not yours.")
        print("You look behind and see the two largest customers of the tavern walking purposefully toward you.")
        n = input("Do you turn and FIGHT or RUN? ").upper()
        if weapon > 0:
            helper.fight("\nThe two burly men approach you simultaneously, you draw your sword",
                              "You get punched.", "You knock them both unconscious!", 4)
        if weapon == 0:
            helper.fight("\nThe two burly men start to throw punches.", "You get punched.",
                              "You knock them both unconscious!", 7)
        input("\nThe two men lay on the ground groaning, do you want to SEARCH their bags, or KEEP WALKING?")

    elif j == "STAY" and g == "FIGHT":
        input("\nThe evening passes without distress.\nDo you try to TALK or remain QUIET? ").upper()

    elif j == "STAY" and g == "RUN":
        input(
            "\nAfter you sit down, the two biggest men get up and demand you give them all you own.\nDo you GIVE them your supplies, or FIGHT? ").upper()
        if weapon > 0:
            helper.fight("\nThe two burly men start to throw punches before you can draw your sword.",
                              "You get punched.", "You knock them both unconscious!", 6)
        if weapon == 0:
            helper.fight("\nThe two burly men start to throw punches.", "You get punched.",
                              "You knock them both unconscious!", 6)

else:
    print("\n" * 4 + "Restart. Make sure to only type the capitalized word, in ALL CAPS.")