import random
import time

"""
This game, 'Donutland' is an interactive text-based game where the player must make choices to escape a magical land of donuts. The game 
also allows for the user to answer basic math questions to proceed in the game. The game is designed to be
to be fun and educational for kids. Development of this game took a unique function based approach, where functions without inputs
were called for the purpose of displaying text, recieving user input, and redirecting to the next function. The game also uses a dictionary 
to store questions and answers for the math part of the game.
"""

# Questions and answers for math part of game (generated by AI)
questions = {
    1: {"question": "Solve for x: 2x + 3 = 11", "answer": 4},
    2: {"question": "What is the sum of 15 and 9?", "answer": 24},
    3: {"question": "What is 45 divided by 5?", "answer": 9},
    4: {"question": "Find x: 7x - 4 = 24", "answer": 4},
    5: {"question": "What is the product of 6 and 7?", "answer": 42},
    6: {"question": "Subtract 13 from 29.", "answer": 16},
    7: {"question": "Solve for x: 5x + 2 = 17", "answer": 3},
    8: {"question": "What is the square of 8?", "answer": 64},
    9: {"question": "Find x: x/4 = 7", "answer": 28},
    10: {"question": "What is 12 times 11?", "answer": 132},
    11: {"question": "What is 100 minus 37?", "answer": 63},
    12: {"question": "Solve for x: 9x = 81", "answer": 9},
    13: {"question": "What is the cube of 3?", "answer": 27},
    14: {"question": "What is 5 squared?", "answer": 25},
    15: {"question": "Find x: 2x + 5 = 15", "answer": 5},
    16: {"question": "What is 10 times 12?", "answer": 120},
    17: {"question": "Add 14 and 32.", "answer": 46},
    18: {"question": "What is the remainder when 29 is divided by 4?", "answer": 1},
    19: {"question": "Solve for x: 3x - 7 = 20", "answer": 9},
    20: {"question": "What is 81 divided by 9?", "answer": 9},
}

# Used to track math questions and provide summary at end.
questions_used = {}
questions_attempted = 0
questions_correct = 0

# Special print effect
def aprint(text=""):
    if text == "":
        print()
    else:
        for char in text:
            print(char, end="", flush=True)
            time.sleep(0.03)
        print()

# Asks the user a math question to answer in order to proceed in the game.
def question():
    aprint()
    aprint("!! You must answer the following question to proceed !!")

    # Choose random question
    random.seed()
    q = random.choice(range(1, 20))

    # Get global variables
    global questions_attempted
    global questions_correct
    global questions_used

    # Modify global variables
    questions_attempted += 1

    # Track if user got question correct on first try
    correct_first_try = True

    # Ask question until user gets it correct
    while True:
        # Display question
        aprint()
        aprint(questions[q]["question"])

        # Add question to questions_used dictionary for summary at end
        questions_used[questions_attempted] = questions[q]

        # Get answer
        str_answer = input("Answer: ")

        # Check if answer is a number. If not, ask user to enter a number. 
        # Design allows for answer not to count as wrong if user accidentally enters a string.
        try:
            answer = int(str_answer)
        except ValueError:
            aprint("Please enter a number.")
            continue

        # Add user answer to questions_used dictionary
        questions_used[questions_attempted]["user_answer"] = answer

        # Check if answer is correct
        if answer == questions[q]["answer"]:
            # Display message
            aprint("Correct!")
            aprint()
            aprint("Continue on your journey.")

            # Add if user got question correct on first try to questions_used dictionary
            questions_used[questions_attempted]["correct"] = correct_first_try

            # Add to questions_correct if user got question correct on first try
            if correct_first_try:
                questions_correct += 1
            
            aprint()

            # Break out of loop
            break
        else:
            # Change correct_first_try to False because user got question wrong
            correct_first_try = False

            # Display message
            aprint("Incorrect. Try again!")
        

# Asks user for a choice given a prompt and possible choices and ensures that the choice is valid. Returns the choice.
def ask_choice(prompt, options):

    # Keep asking until user enters a valid choice
    while True:
        
        prompt_and_options = prompt+" "+str(options).replace('\'', '')+"\n"

        # Ask prompt and get choice. Replace quotes for better UI.
        choice = input(prompt_and_options).replace(" ", "").lower()

        # Check if choice is valid
        if choice.lower() in options:
            break
        else:
            # Display message if choice is invalid
            aprint("Invalid choice.")
            aprint()
            choice = input(prompt_and_options)

    # Return choice of user
    return choice 


# Ends the game, either with a win or loss. Asks user if they would like to play again.
def end(won):
    
    # Display message based on if user won or lost
    if not won:
        aprint()
        aprint("You have died.")
    else:
        aprint()
        aprint("You have won!")

    aprint()

    # Ask user if they would like to see their math scores. Lowercase and remove spaces from input.
    showscores = ask_choice("Would you like to see your math scores?", ["yes", "no"])

    # If answer is yes, display scores
    if showscores == "yes":
        display_scores()

    aprint()

    # Ask user if they would like to play again.
    play_again = ask_choice("Would you like to play again?", ["yes", "no"])

    # Restart game if user wants to play again
    if play_again == "yes":
        aprint()
        intro()
    else:
        aprint()
        aprint("Goodbye!")

        exit()


# Displays the math scores using the variables defined at the top of the file.
def display_scores():
    aprint()
    
    # Display math scores
    aprint("Math scores\n--------------------------")

    # Display grade
    aprint("Grade: "+str(questions_correct)+"/"+str(questions_attempted))

    # Display percentage
    aprint("Percentage: "+str(questions_correct/questions_attempted*100)+"%")

    # Display all questions and answers
    aprint("Questions:")

    # Iterate over all questions used and display them
    for question, i in enumerate(questions_used):
        aprint()

        # Display question, correct answer, user answer, and if user got question correct
        aprint(str(i)+") "+str(questions_used[i]["question"]))
        aprint("Correct answer: "+str(questions_used[i]["answer"]))
        aprint("Actual answer: "+ str(questions_used[i]["user_answer"]))

        # Display if user got question correct
        if questions_used[i]["correct"]:
            aprint("CORRECT")
        else:
            aprint("INCORRECT")
        aprint()

# Starting point of the game, introduces the game to user and recieves information from the user (their name). Redirects to: house, tree, river, mountain, or eat donut. Redirects from: end(both lose and win).
def intro():
    # Get global variables
    global questions_used
    global questions_attempted
    global questions_correct

    # Reset math scores
    questions_used = {}
    questions_attempted = 0
    questions_correct = 0

    # Get name of user
    name = input("Hello traveler? What is your name?\n")

    # Display a stickman with the user's name
    aprint()
    aprint(" "+name)
    aprint("  O ")
    aprint(" /|\ ")
    aprint(" / \ ")

    aprint()

    # Introduce user to game
    aprint(f"Well, {name}, you just so happen to be in a magical land of donuts.")

    aprint("However, you are stuck in this donut land and do not know how to get out.")
    aprint("You must make the right choices to escape this land.")
    aprint()
    aprint("In front of you, you see a donut house.")
    aprint("To your right, you see a donut tree.")
    aprint("To your left, you see a donut river.")
    aprint("Behind you, you see a donut mountain.")
    aprint("You are holding a donut in your hand.")
    
    # Ask math question to user
    question()

    # Get user choice, redirect to next function based on choice
    choice = ask_choice("Were do you go?/What do you do?", ["house", "tree", "river", "mountain", "eat donut"])
    if choice == "eat donut":
        # Redirect to eat donut
        eat_donut()
    elif choice == "tree":
        # Redirect to donut tree
        donut_tree()
    elif choice == "river":
        # Redirect to donut river
        donut_river()
    elif choice == "house":
        # Redirect to donut house
        donut_house()
    elif choice == "mountain":
        # Redirect to donut mountain
        donut_mountain()

# Donut house path. Redirects to: donut river. Redirects from: intro.
def donut_house():
    aprint()

    # Display storyline
    aprint("You find a huge troll in the donut house.")
    aprint("He kicks you out and throws you in the river!")

    # Ask a question before proceeding
    question()

    # Redirect to donut river
    donut_river()

# Donut tree path. Redirects to: donut river. Redirects from: intro.
def donut_tree():
    aprint()

    # Display storyline
    aprint("You climb the donut tree.")
    aprint("You slip and fall into the donut river!")

    # Ask a question before proceeding
    question()

    # Redirect to donut river
    donut_river()

# Eat donut path; user dies. Redirects to: end(lose). Redirects from: intro.
def eat_donut():
    aprint()

    # Display storyline
    aprint("You eat the donut.")
    aprint("The donut was poisonous! You have died of a sugar overdose.")

    # End game
    end(False)

# Donut mountain path. Redirects to: troll mountain, donut river. Redirects from: intro.
def donut_mountain():
    aprint()

    # Display storyline
    aprint("You walk to the donut mountain.")
    aprint("You see a giant donut at the top of the mountain.")
    aprint("You decide to climb the mountain.")
    aprint("It wasn't a donut, it was a boulder!")
    aprint("On your left is a deadly donut river, on your right is another steep donut mountain...")

    # Ask a question before proceeding
    question()

    # Get user choice, redirect to next function based on choice
    choice = ask_choice("Climb the other mountain or jump in the river?", ["climb", "jump"])
    if choice == "climb":
        # Redirect to troll mountain
        troll_mountain()
    elif choice == "jump":
        # Redirect to donut river
        donut_river()

# Troll mountain path. Redirects to: fight troll, run away. Redirects from: donut mountain.
def troll_mountain():
    aprint()
    
    # Display storyline
    aprint("You walk to the donut mountain.")
    aprint("You see a huge donut troll at the top of the mountain.")

    # Ask a question before proceeding
    question()

    # Get user choice, redirect to next function based on choice
    choice = ask_choice("Do you fight the troll or run away?", ["fight", "run"])
    if choice == "fight":
        # Redirect to fight troll
        fight_troll()
    elif choice == "run":
        # Redirect to run away
        run_away()

# Fight troll path. Redirects to: end(lose). Redirects from: troll mountain.
def fight_troll():
    aprint()

    # Display storyline
    aprint("You fight the troll.")
    aprint("He grabs your shield, slings you to the ground, jumps on it!")
    aprint("You are smashed into a donut pancake.")
    aprint("You lose!")

    # End game with loss
    end(False)

# Run away path. Redirects to: donut river. Redirects from: troll mountain.
def run_away():
    aprint()
    
    # Display storyline
    aprint("You run away.")
    aprint("You trip and fall down")
    aprint("You fall into the donut river.")

    # Redirect to donut river
    donut_river()

# Donut river path Redirects to: donut cave, donut tree. Redirects from: donut house, donut tree, donut mountain.
def donut_river():
    aprint()

    # Display storyline
    aprint("You get knocked unconcious by a log.")
    aprint("You wake up on a donut beach.")

    # Ask a question before proceedings
    question()

    # Get user choice, redirect to next function based on choice
    choice = ask_choice("You see a cave shaped like a donut and another huge donut tree.", ["cave", "tree"])
    if choice == "cave":
        # Redirect to donut cave
        donut_cave()
    elif choice == "tree":
        donut_tree()
    
# Donut cave path. Redirects to: donut sword, donut shield. Redirects from: donut river.
def donut_cave():
    aprint()

    # Display storyline
    aprint("You enter the donut cave.")
    aprint("You see a portal to the real world!")
    aprint("But there is a troll guarding the portal.")
    aprint("You have to fight the troll.")
    aprint("You have enough donuts to craft either a donut sword or a donut shield.")

    # Ask a question before proceeding
    question()

    # Get user choice, redirect to next function based on choice
    choice = ask_choice("Do you craft a donut sword or a donut shield?", ["sword", "shield"])
    if choice == "sword":
        # Redirect to donut sword
        donut_sword()
    elif choice == "shield":
        # Redirect to donut shield
        donut_shield()

# Donut sword path. Redirects to: end(win). Redirects from: donut cave.
def donut_sword():
    aprint()

    # Display storyline
    aprint("You craft a donut sword.")
    aprint("You fight the troll.")

    # End game with win
    end(True)

# Donut shield path. Redirects to: end(lose). Redirects from: donut cave.
def donut_shield():
    aprint()

    # Display storyline
    aprint("You craft a donut shield.")
    aprint("You fight the troll.")
    aprint("He grabs your shield, slings you to the ground, jumps on it!")
    aprint("You are smashed into a donut pancake.")

    # End game with loss
    end(False)

# Initiate game by calling intro function
intro()