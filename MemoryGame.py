import random as rand


def startGame(d):
    print("Your chosen difficulty is:", d)

def highScores:
    print("Highest score:")

def menu():
    #Completely working title. Needs replacing with something better.
    print("PYTHON MEMORY GAME")
    print("")
    print("Input START to start game.")
    print("Input SCORES to view high scores.")
    print("Input EXIT to close the program.")

    # while True functioning as error trapping.
    while True:
        userInput = input("Please enter your selection:")
        if userInput.lower == "start":
            print("Game starting...")
            while True:
                dChoice = input("Please input your difficulty choice: (easy/med/hard)")
                if dChoice.lower() == "easy":
                    difficulty = 1
                    break
                elif dChoice.lower() == "med":
                    difficulty = 2
                    break
                elif dChoice.lower() == "hard":
                    difficulty = 3
                    break
                else:
                    print("Incorrect input. Please try again.")

            startGame(difficulty)
        elif userInput.lower() == "scores":
            print("Loading high scores...")
            highScores()
        elif userInput.lower() == "exit":
            print("Program exiting...")
            break

        else:
            print("No correct input detected.")
            continue

menu()
