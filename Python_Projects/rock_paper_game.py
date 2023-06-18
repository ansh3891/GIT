import random
print("Hi there!, Welcome to Rock paper Scissors game")
user_wins=0
computer_wins=0
options=["Rock","paper","Scissors"]
while True:
    user_pick=input("Enter you choice: Rock, paper,Scissors or q to quit: ")
    if user_pick=="q":
        break
    elif user_pick not in options:
        continue
    random_number=random.randint(0,2)
    # rock=0, paper=1, scissor=2
    computer_pick=options[random_number]
    print("Computer picked: ",computer_pick)

    if user_pick=="rock" and computer_pick=="Scissors":
        print("You Won!")
        user_wins+=1
        continue

    elif user_pick=="paper" and computer_pick=="Rock":
        print("You Won!")
        user_wins+=1
        continue
    elif user_pick=="scissors" and computer_pick=="paper":
        print("You Won!")
        user_wins+=1
        continue
    else:
        print("Computer Won!")
        computer_wins+=1
        continue;
print("You won ",user_wins," times.")
print("Computer won",computer_wins," times.")
print("Goodbye")

