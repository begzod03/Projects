questions = {"What is Khabib Nurmagomedov UFC record?: ": "B",
             "Who is the president of UFC?: ": "C",
             "What does UFC stand for?: ": "B",
             "Which MMA organization is the biggest after UFC?: ": "D"}

options = [["A. 19/0/0", "B. 29/2/1", "C. 25/0/0", "D. 69/42/0"],
           ["A. Barack Obama", "B. Donald Trump", "C. Dana White", "D. Dana Izadphana"],
           ["A. United Fighting Community", "B. Ultimate Fighting Championship", "C. Uganda Fire Construction", "D. Ultimate Fight Club"],
           ["A. FIFA", "B. NFL", "C. NBA", "D. Bellator"]]

guesses = []
guess = None

def new_game():
    answers = []
    correct = 0
    question_num = 1

    for key in questions:
        print("~~~~~~~~~~~~~~")
        print(key)
        for i in options[question_num-1]:
            print(i)

        guess = input("Which one is it?: ").upper()
        guesses.append(guess)

        correct += check_answer(questions.get(key), guess)

        question_num +=1

    display_score(correct, guesses)

def check_answer(answer, guess):
    if answer == guess:
        print("Correct!")
        return 1
    else:
        print("Wrong")
        return 0

def display_score(correct, guesses):
    print("---------------")
    print("Results")
    print("---------------")
    print("Answers: ", end="")

    for i in questions:
        print(questions.get(i), end="")
    print("")

    print("Guesses: ", end="")

    for i in guesses:
        print(i, end="")
    print("")

    score = (correct/len(questions)*100)
    print("Your Score is: ", str(score), "%")

def play_again():
    response = input("Would you like to play again?: ").lower()

    if response == "yes":
        return True
    else:
        False

new_game()
while play_again():
    new_game()
print("Thanks for playing!")