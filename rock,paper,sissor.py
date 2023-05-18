import random

print("WELCOME TO THE GAME")
print("LETS PLAY ROCK , PAPER , SISSOR")

player=input("DO YOU WANT TO PLAY ? ")

if player.lower()!="yes":
    quit()
else:
    print("GLAD YOU SAID THAT LETS BEGIN")
user_wins=0
computer_wins=0

options=["rock" , "paper" , "sissor"]

while True:
    user_input=input("type rock/paper/sissor or quit: ").lower()
    if user_input=="quit":
        break

    if user_input not in options:
        continue

    random_numbers = random.randint(0,2)
    computer_pick=options[random_numbers]
    print("computer picked" , computer_pick + ".")

    if user_input=="rock" and computer_pick=="paper":
        print("YOU WON")
        user_wins+=1

    elif user_input=="paper" and computer_pick=="rock":
        print("YOU WON") 
        user_wins+=1

    elif user_input=="sissor" and computer_pick=="paper":
        print("YOU WON")
        user_wins+=1

    else:
        print("YOU LOOSE") 
        computer_wins+=1

print("YOU WON " , user_wins , "times")
print('COMPUTER WON' , computer_wins , "times")
print("GOODBYE")              




