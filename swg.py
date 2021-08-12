# snake-water-gun
#Snake water gun gaming

import random
print("welcome to our SNAKE-WATER-GUN gaming")
a = input("enter your name:")

your_score = 0
comp_score = 0
chances = 1

while chances<=5:


    p1 = input("enter ur choice s-Snake,w-Water,g-Gun:")
    lst = ["s","w","g"]
    p2 = random.choice(lst)


    if p1 == p2:
        print("TIE occurs")
        print("\nno points")

    elif p1 == "s" and p2 == "w":
        your_score = your_score + 1
        print("You-Snake and Computer-Water\n")
        print("snake drinks water!You win\n")
        print(f"\nyou got {your_score}")

    elif p1 == "w" and p2 == "g":
        your_score = your_score + 1
        print("You-Water and Computer-Gun\n")
        print("gun shrinks in water ! you win")
        print(f"you got {your_score}")


    elif p1 == "g" and p2 == "s":
        your_score = your_score + 1
        print("You-Gun and Computer-Snake\n")
        print("snake died by gun shot !you win")
        print(f"you got {your_score}")

    elif p1 == "w" and p1 == "s":
        comp_score = comp_score + 1
        print("You-Water and Computer-Snake\n")
        print("the snake drank water !you lose\n")
        print(f"computer gets {comp_score}")

    elif p1 == "g" and p2 == "w":
       comp_score = comp_score + 1
       print("you-Gun and Computer-Water\n")
       print("gun sank in water!you lose\n")
       print(f"computer gets {comp_score}")

    elif p1 == "s" and p2 == "g":
        comp_score = comp_score + 1
        print("you-Snake and Computer-Gun\n")
        print("snake died by gun shot !you lose\n")
        print(f"computer gets {comp_score}")

    else:
        print("it was tie")
        print("invalid")
        continue

    print("\nno. of guesses left: {}".format(5-chances))
    chances = chances + 1

    if chances > 5:
         print("\nGAME OVER")

print(f"your score: {your_score}\nComputer's score: {comp_score}")

if comp_score > your_score:
    print("\n computer won and you lost")

elif comp_score < your_score:
    print("\nyou won and computer lost")

else:
    print("it was tie!")

print(f"\nyour points are {your_score} and computer point are{comp_score}\n")







































