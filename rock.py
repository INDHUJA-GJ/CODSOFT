import random

print("Rock beats scissors, scissors beat paper, and paper beats rock.")
print("Let's start")
count=0
com_count=0
while True:
    n=input("Enter your choice:")
    z=random.randint(1,3)
    if False:
        pass
    else:

        if z==1:
            n2="paper"
        elif z==2:
            n2="scissor"
        else:
            n2="rock"
        if n.lower()==n2:
            print("Tie!!!!!")
        elif n.lower()=="rock" and n2!="paper":
            print("User wins")
            count=count+1
        elif n.lower()=="paper" and n2!="scissor":
            print("User wins")
            count = count + 1
        elif n.lower()=="scissor" and n2!="rock":
            print("User wins")
            count = count + 1
        else:
            print("Computer Wins")
            com_count = com_count + 1
    print("User input:", n)
    print("Computer input:", n2)
    k=input("Do you want to continue(y/n):")
    if k=="y":
        continue
    else:
        break
if count>com_count:
    print("Final result: USER WINS!!!!")
else:
    print("Final result:Computer wins!!!!!!!!!!")