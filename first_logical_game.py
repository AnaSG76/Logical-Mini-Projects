print("Welcome to my first logic game!")
name = input("What is your name? ")
age = int(input("What is your age? "))

lives = 10

if age >= 18:
    print("You are old enough to play!")

    wants_to_play = input("Do you want to play? ").lower()
    if wants_to_play == "yes":
        print("You are starting with", lives, "lives. Let's play!")
        red_or_green = input("First choice...Red or Green (red/green)? ")
        if red_or_green == "green":
            answer = input(
                "You are at a pedestrian crosswalk...Do you check for incoming traffic first or cross the street \
                (check/cross)? ")

            if answer == "check":
                print("You managed to get across safely and gained 2 lives!")
                lives += 2
                print("You now have " + str(lives) + " lives.")

            elif answer == "cross":
                print(
                    "You managed to get across, but were hit by a bicycle and lost 5 lives.")
                lives -= 5
                print("You now have " + str(lives) + " lives.")

            answer = input(
                "You get across and noticed a park and a bike path. Which do you go to (park/bike path)? ")
            if answer == "park":
                print("You go to the park and fell down the slide...you lose 5 lives.")
                lives -= 5
                if lives <= 0:
                    print("You now have 0 lives and you lost the game...")
                else:
                    print(
                        "You have made it with " +
                        str(lives) +
                        " lives...You win!")

            else:
                print("You got hit by 2 bicycles and lost...")

        else:
            print("You have a red light, cannot go anywhere and lost...")

    else:
        print("Sorry, we cannot play!")

elif age >= 16:
    print("You can play only with parental permission.")

    parental_permission = input("Do you have parental permission? ").lower()
    if parental_permission == "yes":
        print("You are starting with", lives, "lives. Let's paly!")

        red_or_green = input("First choice...Red or Green (red/green)? ")
        if red_or_green == "green":
            answer = input(
                "You are at a pedestrian crosswalk...Do you check for incoming traffic first or cross the street \
                (check/cross)? ")

            if answer == "check":
                print("You managed to get across safely and gained 2 lives!")
                lives += 2
                print("You now have " + str(lives) + " lives.")

            elif answer == "cross":
                print(
                    "You managed to get across, but were hit by a bicycle and lost 5 lives.")
                lives -= 5
                print("You now have " + str(lives) + " lives.")

            answer = input(
                "You get across and noticed a park and a bike path. Which do you go to (park/bike path)? ")
            if answer == "park":
                print("You go to the park and fell down the slide...you lose 5 lives.")
                lives -= 5
                if lives <= 0:
                    print("You now have 0 lives and you lost the game...")
                else:
                    print(
                        "You have made it with " +
                        str(lives) +
                        " lives...You win!")

            else:
                print("You got hit by 2 bicycles and lost...")

        else:
            print("You have a red light, cannot go anywhere and lost...")

    else:
        print("Sorry, we cannot play!")

else:
    print("You are not old enough to play...good bye!")
