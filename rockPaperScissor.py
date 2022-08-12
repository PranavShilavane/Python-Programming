'''

This game is a simple single player game that I have made using the random module in Python. A simple game where we can play with computer which is basically made using the random module. This game is quit sensitive so if you try it dont make a thing which can bring an exception because when I have made this program I dont know about exception handling.

'''

import random

turn, userScore, computerScore = 0

print('''
      ***********************************************************************
      ************************                               ****************
      ************************    ROCK PAPER SCISSOR GAME    ****************
      ************************                               ****************
      ***********************************************************************
      ''')

userName = input("Enter the Player name : ")

print("\n\n\n")

while(turn != 5):
    print("\n\n\t\t "+userName+" : ")

    user = int(input('''
              1]  Rock
              2]  Paper
              3]  Scissor

              ---> '''))

    if(user != 1 and user != 2 and user != 3):
        print("\n\t\tPlease enter valid choice...")
        continue

    computer = random.randint(1, 3)

    print("\n\t\tComputer : "+str(computer))

    if(user == 1 and computer == 1):
        print("\n\t\tTye ... (*_*)____")

    elif(user == 2 and computer == 1):
        print("\n\t\tYou win ... (^_^)____")
        userScore += 1

    elif(user == 3 and computer == 1):
        print("\n\t\tComputer win ... (+_+)____")
        computerScore += 1

    elif(user == 1 and computer == 2):
        print("\n\t\tComputer win ... (+_+)____")
        computerScore += 1

    elif(user == 2 and computer == 2):
        print("\n\t\tTye ... (*_*)____")

    elif(user == 3 and computer == 2):
        print("\n\t\tYou win ... (^_^)____")
        userScore += 1

    elif(user == 1 and computer == 3):
        print("\n\t\tYou win ... (^_^)____")
        userScore += 1

    elif(user == 2 and computer == 3):
        print("\n\t\tComputer win ... (+_+)____")
        computerScore += 1

    elif(user == 3 and computer == 3):
        print("\n\t\tTye ... (*_*)____")

    turn += 1

print("\n\n\n")

if(userScore > computerScore):
    print("The winner is : "+userName)
elif(userScore < computerScore):
    print("The winner is : "+"Computer")
elif(userScore == computerScore):
    print("Match tye... (^_^)   ")


'''__________________________ SC [ Star ] __________________________'''
