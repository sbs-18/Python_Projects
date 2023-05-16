import random
hand_list = ['Rock', 'Paper', 'Scissors']
while(True):
    while(True):
        CPU_hand=random.choice(hand_list)
        print("Choose Your Hand")
        print("1.Rock\n2.Paper\n3.Scissors\n4.Exit")
        user_value = input("Select the number of your hand : ")
        if(user_value != '1' and user_value !='2' and user_value !='3' and user_value !='4'):
            print("Wrong Input : Choose again only between number 1,2,3,4\n")
        else:
            user_hand_value = int(user_value)
            break

    print("---------------------------------------")
    if(user_hand_value==4):
        print("-----Thank You For Playing-----")
        break
    user_hand = hand_list[user_hand_value - 1]
    print("Your hand : ",user_hand)
    print("CPU hand : ",CPU_hand)
    print(user_hand,"VS",CPU_hand)
    print("---------------------------------------")

    if(user_hand == CPU_hand):
        print("Its a tie")
    elif(user_hand=="Rock" and CPU_hand == "Scissors"):
        print("You Win,Computer lose")
    elif(user_hand=="Paper" and CPU_hand == "Rock"):
        print("You Win,Computer lose")
    elif(user_hand=="Scissors" and CPU_hand == "Paper"):
        print("You Win,Computer lose")
    else:
        print("You Lose,Computer Win")
    print("--------------------------------------------------------------------------------------------------\n")
