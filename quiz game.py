def new_game():
    guesses = []
    correct_guesses = 0
    question_number = 1
    for key in questions:
        print("------------------------")
        print(key)
        for i in options[question_number-1]:
            print(i)
        guess = input("Enter your guess: ")
        guess = guess.upper()
        guesses.append(guess)
        correct_guesses += check_answer(questions.get(key), guess)
        question_number += 1
    display_score(correct_guesses, guesses)


def check_answer(answer, guess):
    if answer == guess:
        print("Correct!")
        return 1
    else:
        print("Incorrect!")
        return 0


def display_score(correct_guesses, guesses):
    print("---------------------")
    print("Results")
    print("---------------------")
    print("Answer:", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("guesses:", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int(correct_guesses / len(questions) * 100)
    print("Your score is", str(score)+"%")


def play_again():
    response = input("Would you like to play again? ")
    response = response.upper()
    if response == "YES":
        return True
    else:
        return False


questions = {"what is your name": "A",
             "what is your favorite color": "B",
             "how old are you": "C",
             "your country ": "B"}
options = [["A.ASIM ALI", "B.KHAN", "C.david", "D.MUSTAFA"],
          ["A.white ", "B.pink", "C.black", "D.red"],
          ["A. 20", "B.18", "C.16", "D.35"],
          ["A.india", "B.pakistan", "C.afghanistan", "D.iran"]]

new_game()

while play_again():
    new_game()

print("Thanks for playing!")
