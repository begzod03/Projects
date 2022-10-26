import random

print("Welcome to Rock, Paper, and Scissor. A totally fair game against a computer :)")
count = 0
tie = 0
loses =0
while True:
    pieces = ['rock', 'paper', 'scissor']
    player = None

    player = input("Please input which piece you picking: ").lower()
    computer = random.choice(pieces)

    if player not in pieces:
        while player not in pieces:
            player = input("that's illegal >:( Please pick an option: ")



    if(computer == player):
        print("computer: ", computer, " player: ", player, "\n a tie!")
        tie +=1
    elif(player == "rock" and computer == "scissor"):
        print("computer: ", computer, " player: ", player, "\n You win!")
        count +=1
    elif(player == "scissor" and computer == "paper"):
        print("computer: ", computer, " player: ", player, "\n You win!")
        count +=1
    elif(player == "paper" and computer == 'rock'):
        print("computer: ", computer, " player: ", player, "\n You win!")
        count +=1
    else:
        print("computer: ", computer, " player: ", player, "\n You Lose!")
        loses +=1

    option = input("Would you like to play again? (yes,no): ")

    if option != "yes":
        break


stats = input("thanks for playing! Would you like to see your stats? ").lower()

if stats == "yes":
    print("Wins: ", count, "\nLoses: ", loses, "\nties: ", tie)
else:
    print("")