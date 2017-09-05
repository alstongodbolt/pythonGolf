import random
def directions():
    print("This is mini-golf. \nThe goal is to shoot the golf ball in the hole in as "
          "few attempts as possible")
    print("You will be given your distance from the hole. Then you select low medium or"
          " high power. \nYou will continue until you make the hole")
    print("Good luck!")


def game():
    playAgain = True
    while playAgain == True:
        hole = random.uniform(150.1, 500.9)
        hole = round(hole, 2)
        par = 0
        if hole < 300:
            par = 4
        elif hole > 301 and hole < 400:
            par = 5
        else:
            par = 6
        print("This is a par {}.".format(par))
        print("The distance to the hole is: {} feet".format(hole))
        hitPower = 0
        holeDistance = 0
        strokes = 0
        while hole != 0:
            print()
            print("1: Within 5 feet")
            print("2: Within 20 feet")
            print("3: Within 50 feet")
            print("4: Within 165 feet")
            print("5: Medium range is 120 - 380")
            print("6: High range is 200 - 500")
        #print("\nEnter 1, 2, 3")
            power = int(input("\nEnter 1, 2, 3, 4, 5, 6: "))
            strokes += 1
            if power ==1:
                print("You selected within 5 feet")
                hitPower = random.uniform(1.0, 5.0)
                hitPower = round(hitPower, 2)
            elif power == 2:
                print("You selected within 20 feet")
                hitPower = random.uniform(10.1, 20.0)
                hitPower = round(hitPower, 2)
            elif power == 3:
                print("You selected within 50 feet")
                hitPower = random.uniform(15.1, 50.0)
                hitPower = round(hitPower, 2)
            elif power == 4:
                print("You selected within 165 feet")
                hitPower = random.uniform(45.1, 165.9)
                hitPower = round(hitPower, 2)
            elif power == 5:
                print("You selected within 380 feet")
                hitPower = random.uniform(120.1, 380.9)
                hitPower = round(hitPower, 2)
            elif power == 6:
                print("You selected within 500 feet")
                hitPower = random.uniform(200.1, 500.9)
                hitPower = round(hitPower, 2)
            else:
                print("You entered an invalid number")
            print("Hole distance: ", hole)
            print("Hitpower: ", hitPower)
            #hole = hole - hitPower
            if hitPower > hole:
                hole = hitPower - hole
            else:
                hole = hole - hitPower
            hole = round(hole, 2)

            if hole < 1.5:
                hole = 0
                strokes += 1
                print("You made it {} strokes!".format(strokes))
                if strokes - par == 0:
                    print("You made par")
                elif strokes - par == -1:
                    print("Bogey")
                elif strokes - par == -2:
                    print("Double Bogey")
                elif strokes - par > -3:
                    print("You don't want to know.")
            if hole > 0:
                print("New distance: ", hole)

        answer = input("Play again? (Y/N) ")
        if answer.upper() == "N":
            playAgain = False

directions()
game()

