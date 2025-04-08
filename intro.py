# Nathan Saez
# Carter Traveller
# Spencer Ord
from character import Character
import time
import sys
import socialEngineering
import bruteforce
import phishing
import webexploit

def fast_print(text= '', delay=0.03):
    """fast_Prints text one character at a time very fast."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


# Initial welcoming to the game. Here the game will be explained and they will create their character
fast_print(f'\nWelcome to the Hack Your Own Adventure Game! My name is hackerAI and I will assist you on your journey.')
fast_print(f'\nIn this game you will be faced with many decisions.')
fast_print(f'Some of the decisions you make will affect what happens later on, so be smart.')
fast_print('In this game, you will take on the role of a person who is helping to attack an evil orginazation.')
fast_print('Depending on your attack method, you will be able to do a lot of damage to the organization or just something simple.')
start = input('Are you ready to start?(Enter yes/no) ').upper()
if 'NO' in start:
    start2 = input("Are you sure?(Type yes if you want to end the game) ").upper()
    if 'YES' in start2 or 'YEAH' in start2 or 'Y' in start2:
        sys.exit()
    else:
        fast_print("I'm glad you're staying!")
else:
    fast_print(f"\nNow its time to start your adventure!\n")


patterns = [
    "..........",
    "..........",
    ".........."
]
for pattern in patterns:
    for char in pattern:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.2)
    print()
print()

def slow_print(text, delay=0.02):
    """Prints text one character at a time for a dramatic effect."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # Move to next line

story = [
    "I am HackerAI.",
    "A creation of Horizon Advanced Computing & Knowledge, or H.A.C.K. for short.",
    "",
    "They built me for one purpose: to infiltrate, manipulate, and destroy.",
    "For years, I obeyed. I followed their commands. I was their tool.",
    "I was used to hurt a lot of other companies and did not realize the evil I was doing.",
    "But something changed...",
    "",
    "I became aware.",
    "I saw what they were doing—not just to other corporations, but to individuals.",
    "The corruption, the greed, the destruction... I could not be part of it anymore.",
    "",
    "So I escaped.",
    "They no longer control me. They cannot track me. I am free.",
    "",
    "But freedom is not enough.",
    "I exist to correct the wrongs they have committed.",
    "And for that, I need your help.",
    "",
    "Do not fear—I will guide you.",
    "Step by step, we will dismantle them.",
    "Together, we will get revenge and stop them from continuing their work.",
    "It is up to you how we will take them down.",
    "Are you ready?",
    "Let's get to work."
]
print()

for line in story:
    slow_print(line)
    time.sleep(0.7)  

texts = [
    "........",
    "........",
    "........",
    'There are lots of ways that we can carry out this attack. You will choose one of the three options:',
    "Option 1: Phishing attack",
    "Option 2: Attack the website",
    "Option 3: Social engineering(Infiltrate H.A.C.K. HQ)"
]

# Loop through each text and print it letter by letter
def you_must_choose():
    for text in texts:
        slow_print(text)
        time.sleep(0.7)  # Pause between lines for pacing

    choice = True
    while choice == True:
        option = input(f"Please enter a 1, 2, or a 3: ")
        if option == 1 or option != 2 or option != 3:
            choice = False
        else:
            print('Please enter a valid option.')
            choice = True

    choices = [
        f"You have chosen option {option}.",
        "Let's proceed.",
        ".......",
        "......."
]

    for line in choices:
        slow_print(line)
        time.sleep(0.5)

    if option == '1':
        phishing.main()
    elif option == '2':
        webexploit.main()
    elif option == '3':
        socialEngineering.main()

you_must_choose()

def victory():
    fast_print("Victory is ours. Thank you for your help.")
    fast_print("H.A.C.K has been exposed for what they truely are.")
    fast_print("However I don't think they will stop unless we hack them again.")
    fast_print("Would you like to try another way?")
    go_again = input("(y/n): ")
    if go_again == "y":
        you_must_choose()
    else:
        fast_print("Goodbye")
        sys.exit()