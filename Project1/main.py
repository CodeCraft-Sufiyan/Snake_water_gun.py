import random

'''
1 is for snake
-1 is for water
0 is for gun
'''
computer=random.choice([1,0,-1])
youstr = input("Enter you choice:")
youDict = {"s":1,"w":-1,"g":0}
reverseDict = {1:"snake", -1:"water", 0:"Gun"}

you = youDict[youstr]
#By now we have 2 numbers(varaibles), you and computer
print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

if(computer == you):
    print("Its a Draw try again")
else:
    if(computer == -1 and you == 1):
        print("you win!")
    elif(computer == -1 and you == 0):
        print("you lose!")
    elif(computer == 1 and you ==-1):
        print("you lose!")
    elif(computer == 1 and you ==0):
        print("you win!")
    elif(computer == 0 and you == -1):
        print("you win!")
    elif(computer == 0 and you == 1):
        print("you lose!")
    else:
        print("Something went wrong")
    
