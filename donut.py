import random

questions = {
    1: {"question": "Solve for x: 3x + 5 = 20", "answer": "x = 5"},
    2: {"question": "Simplify: (x^2 - 9)/(x + 3)", "answer": "x - 3 (for x ≠ -3)"},
    3: {"question": "If f(x) = 2x^2 + 3x - 5, find f(2)", "answer": "f(2) = 11"},
    4: {"question": "Solve for x: x^2 - 4x - 5 = 0", "answer": "x = 5 or x = -1"},
    5: {"question": "Factorize: x^3 - 3x^2 - 4x + 12", "answer": "(x - 2)(x^2 - x - 6)"},
    6: {"question": "Solve for x: 2/(x+1) + 3/(x-1) = 1", "answer": "x = 2 or x = -5"},
    7: {"question": "Expand: (2x + 3)^2", "answer": "4x^2 + 12x + 9"},
    8: {"question": "Simplify: (3x^2y)(4xy^2)", "answer": "12x^3y^3"},
    9: {"question": "Solve for x: log2(x) + log2(4) = 3", "answer": "x = 2"},
    10: {"question": "If f(x) = x^3 - x, find f'(x)", "answer": "f'(x) = 3x^2 - 1"},
    11: {"question": "Solve for x: e^(2x) = 7", "answer": "x = ln(7)/2"},
    12: {"question": "Find the vertex of the parabola: y = 2x^2 - 8x + 5", "answer": "Vertex: (2, -3)"},
    13: {"question": "Solve for x: |2x - 3| = 5", "answer": "x = 4 or x = -1"},
    14: {"question": "Simplify: (x^2 + 5x + 6)/(x^2 - 1)", "answer": "(x + 3)/(x - 1) (for x ≠ ±1)"},
    15: {"question": "Solve for x: x^4 - 16 = 0", "answer": "x = ±2 or x = ±i"},
    16: {"question": "Find the inverse of f(x) = 3x + 4", "answer": "f^(-1)(x) = (x - 4)/3"},
    17: {"question": "Evaluate: ∫(2x^3 - x^2 + 3)dx", "answer": "1/2x^4 - 1/3x^3 + 3x + C"},
    18: {"question": "Solve for x: 2^(x+1) = 16", "answer": "x = 3"},
    19: {"question": "Find the determinant of the matrix [[2, 3], [4, 5]]", "answer": "-2"},
    20: {"question": "If f(x) = (x - 1)/(x + 2), find f(f(1))", "answer": "f(f(1)) = 0"}
}

def question():
    print("!! You must answer the following question to proceed !!")
    q = random.choice(list(questions.keys()))
    print(questions[q]["question"])
    answer = input("Answer: \n")
    while True:
        if answer == questions[q]["answer"]:
            print("Correct!")
            print("Continue on your journey.")
            break
        else:
            print("Incorrect. Try again!")
        

def intro():
    name = input("Hello traveler? What is your name?\n")
    print()
    print(f"Well, {name}, you just so happen to be in a magical land of donuts.")
    print("However, you are stuck in this donut land and do not know how to get out.")
    print("You must make the right choices to escape this land.")
    print("In front of you, you see a donut house.")
    print("To your right, you see a donut tree.")
    print("To your left, you see a donut river.")
    print("Behind you, you see a donut mountain.")
    print("You are holding a donut in your hand.")
    
    question()

    choice = ask_choice("What do you do?", ["right", "left", "forward", "back", "eat donut"])
    if choice == "eat donut":
        eat_donut()
    elif choice == "right":
        donut_tree()
    elif choice == "left":
        donut_river()
    elif choice == "forward":
        donut_house()
    elif choice == "back":
        donut_mountain()


def donut_house():
    print()
    print("You find a huge troll in the donut house.")
    print("He kicks you out and throws you in the river!")
    donut_river()

def donut_tree():
    print()
    print("You climb the donut tree.")
    print("You slip and fall into the donut river!")
    donut_river()

def eat_donut():
    print()
    print("You eat the donut.")
    print("The donut was poisonous! You have died of a sugar overdose.")
    end(False)

def donut_mountain():
    print()
    print("You walk to the donut mountain.")
    print("You see a giant donut at the top of the mountain.")
    print("You decide to climb the mountain.")
    print("It wasn't a donut, it was a boulder!")
    print("On your left is a deadly donut river, on your right is a steep donut mountain...")

    question()

    choice = input("Climb the mountain or jump in the river?\n")
    return choice

def donut_mountain():
    print()
    print("You walk to the donut mountain.")
    print("You see a huge donut troll at the top of the mountain.")

    question()

    choice = ask_choice("Do you fight the troll or run away?", ["fight", "run"])
    if choice == "fight":
        fight_troll()
    elif choice == "run":
        run_away()

def fight_troll():
    print()
    print("You fight the troll.")
    print("He grabs your shield, slings you to the ground, jumps on it!")
    print("You are smashed into a donut pancake.")
    print("You lose!")
    end(True)

def run_away():
    print()
    print("You run away.")
    print("You trip and fall down")
    print("You fall into the donut river.")
    donut_river()


def donut_river():
    print()
    print("You get knocked unconcious by a log.")
    print("You wake up in a donut beach.")
    print("You see a portal to the real world.")
    print("But there is a troll guarding the portal.")
    print("You have to fight the troll.")
    print("You have enough donuts to craft either a donut sword or a donut shield.")

    question()

    choice = ask_choice("Do you craft a donut sword or a donut shield?", ["sword", "shield"])
    if choice == "sword":
        donut_sword()
    elif choice == "shield":
        donut_shield()

def donut_sword():
    print()
    print("You craft a donut sword.")
    print("You fight the troll.")
    print("You win!")
    end(True)

def donut_shield():
    print()
    print("You craft a donut shield.")
    print("You fight the troll.")
    print("He grabs your shield, slings you to the ground, jumps on it!")
    print("You are smashed into a donut pancake.")
    print("You lose!")
    end(False)

def ask_choice(prompt, options):
    choice = input(prompt+" "+str(options).replace('\'', '')+"\n")
    while choice not in options:
        print("Invalid choice.")
        choice = input(prompt+"\n")
    return choice 

def end(won):
    if not won:
        print("You have died. Restart the game?")
    else:
        print("You have won!")
    play_again = ask_choice("Would you like to play again?", ["yes", "no"])
    if play_again == "yes":
        print()
        intro()
    else:
        print("Goodbye.")
        exit()

intro()