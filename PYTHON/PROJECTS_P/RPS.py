from random import randint

t=["rock","paper","scissors"]

player=True

score=0

while player:
    comp=t[randint(0,2)]
    player=str(input("Rock,Paper,Scissors??"))
    print("Computer:",comp)
    if comp==player:
        print("Tie")
    else:
        if comp=="rock" and player=="paper":
            print("You win.Paper covers rock")
            score=score+10
            player=True
        elif comp=="rock" and player=="scissors":
            print("You lose.Rock smashed scissors")
            player=False
        elif comp=="scissors" and player=="rock":
            print("you win.Rock smashed scissors")
            score=score+10
            player=True
        elif comp=="paper" and player=="rock":
            print("You lose.Paper covers rock")
            player=False
        elif comp=="paper" and player=="scissors":
            print("You win.Scissors cut paper")
            score=score+10
            player=True
        elif comp=="scissors" and player=="paper":
            print("You lose.Scissors cut paper")
            player=False
        else:
            print("Play a valid game.Check your spelling")
            player=True
    if(player==False):
        print("Better luck next time")
    print("SCORE:",score)    
    
