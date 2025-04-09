# Import needed libraries
import time
import sys
from character import Character
import random

def  finish():
    fast_print("Victory is ours. Thank you for your help.")
    fast_print("H.A.C.K has been exposed for what they truely are.")
    fast_print("Goodbye")
    sys.exit()

# Lists and dictionaries initialized here
definitions = {
    'Authentication': 'Authentication is the process of verifying the identity of a user, device, or system, often through methods like passwords, biometrics, or multi-factor authentication.',
    'Base64 Encoding': 'Base64 encoding is a method of converting binary data into an ASCII string format using a set of 64 different fast_printable characters, often used for data transmission and storage.',
    'CIA Triad': 'The CIA Triad refers to the three core principles of cybersecurity: Confidentiality (ensuring data privacy), Integrity (ensuring data accuracy and trustworthiness), and Availability (ensuring data is accessible when needed).',
    'Cybersecurity': 'Cybersecurity is the practice of protecting systems, networks, and data from cyberattacks, data breaches, and unauthorized access to ensure confidentiality, integrity, and availability of information.',
    'Data Breach': 'A Data Breach occurs when sensitive, protected, or confidential data is accessed, disclosed, or stolen by unauthorized individuals.',
    'DDoS': 'A DDoS attack is a malicious attempt to disrupt normal traffic of a targeted server, service, or network by overwhelming the target or its infrastructure with a flood of Internet traffic.',
    'Encryption': 'Encryption is the process of converting data into a code to prevent unauthorized access, often using algorithms and cryptographic keys.',
    'Exploit': 'An Exploit is a piece of software or code designed to take advantage of a vulnerability in a system, application, or network.',
    'Lockpicking': 'Lockpicking is the act of using tools to manipulate the components of a lock to open it without the original key, often used in security research or by criminals.',
    'Machine Learning': 'Machine Learning is a subset of artificial intelligence (AI) that allows systems to learn from data and improve performance without explicit programming, often used in predictive analytics and pattern recognition.',
    'Malware': 'Malware is malicious software designed to disrupt, damage, or gain unauthorized access to computer systems, including viruses, worms, trojans, and ransomware.',
    'OSINT': 'OSINT (Open Source Intelligence) is the practice of collecting and analyzing publicly available information from sources like websites, social media, and public records to gather intelligence.',
    'Phishing': 'Phishing is a type of social engineering attack where attackers impersonate legitimate organizations or individuals to deceive victims into revealing personal or financial information.',
    'Reconnaissance': 'Reconnaissance (Recon) refers to the process of gathering information about a target system, network, or individual to identify vulnerabilities or weaknesses, often done before an attack.',
    'Ransomware': "Ransomware is a type of malicious software that encrypts the victim's data and demands payment, often in cryptocurrency, to restore access.",
    'SQL Injection': 'SQL Injection is a web attack technique where malicious SQL queries are inserted into input fields to manipulate a database.',
    'Social Engineering': 'Social Engineering is a manipulation technique used to deceive individuals into divulging confidential or personal information, often through phishing, pretexting, or baiting.',
    'Spyware': 'Spyware is a type of malicious software that secretly gathers information about a user or organization without their knowledge, often monitoring activity and stealing sensitive data.',
    'Tailgating': 'Tailgating is a physical security breach where an unauthorized person gains access to a restricted area by following closely behind an authorized person, typically without their knowledge.',
    'Trojan Horse': 'A Trojan Horse is a type of malware that disguises itself as a legitimate program or file to trick users into installing it, often allowing unauthorized access to a system.',
    'USB': 'USB (Universal Serial Bus) is a standard for connecting peripheral devices like keyboards, mice, and storage devices to a computer, often used for data transfer and charging.',
    'Virus': 'A Virus is a type of malware that attaches itself to a legitimate program or file and spreads to other programs or files when executed, often causing harm to the system.',
    'Worm': 'A Worm is a type of malware that replicates itself and spreads across networks without needing to attach to a host program, often exploiting vulnerabilities in software to propagate.'
}

prepList = [
    'Buy a fake ID.',
    'Find the company HQ map and the layout of the building(entry points, security cameras, etc).',
    'Research about the employees that we will likely encounter when we get there (security, etc).',
    'Create a spyware and upload it to a USB to take it to the HQ of H.A.C.K. and gather data on their network.',
    'Buy a disguise.',
    'Learn to pick a lock and buy a lock pick set.',
    'Go to the gym and get physically fit.',
    'Finalize plans and begin attack(Only choose this option when you are ready to exit).'
]

def getUserInfo():
    print()
    fast_print('Before we begin, I will need to get some of your information.')
    name = input(f'Please enter your first name: ')
    name = name.capitalize()
    userAge = True
    while userAge == True:
        try:
            age = int(input('Please enter your age: '))
            if age < 16:
                print("Don't you think you're a little young to be taking down a company?")
                userAge = True
            elif age > 85:
                print("Don't you think you're a little old to be taking down a company?")
                userAge = True
            else:
                userAge = False
            
        except:
            print('Please enter a valid age')
            userAge = True
    userGender = True

    while userGender == True:
        gender = input('Please enter your gender(M/F): ').capitalize()
        if gender == 'F' or gender == 'M':
            userGender = False
        else:
            print('Please enter a M or an F')
            userGender = True
    user = Character(name, age, gender)
    if name == 'Imiar':
        user.name = 'NATHAN'
        user.age = 1000000000
        user.gender = 'MALE'
        user.prep_level = 100000
        user.disguise = True
        user.employee_knowledge = True
        user.usb = True
        user.map = True
        user.fake_id = True
        user.money = 10000000000000000000000000000000000
        user.fitness = 10000000000000000
        user.key = True
        user.found_id = True
        user.lock_pic = True
    fast_print(f'Thanks, {user.name}! Now we can start the attack process.')
    return user

def fast_print(text, delay=0.01):
    """fast_Prints text one character at a time very fast."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def getInput():
    """Prompt the user for input."""
    return input("Enter the number of your choice(1, 2, etc.) or 'def' to see the list of definitions: ").strip()

def checkDefinitions():
    """Allows the user to look up definitions until they choose to exit."""
    fast_print('\nHere is the list of definitions:')
    for definition in definitions:
        fast_print(definition)

    while True:
        fast_print('\nEnter "e" or "EXIT" if you are done looking at definitions.')
        choice = input('Please enter the definition you would like to see: ').strip()

        if choice in definitions:
            fast_print('\nDefinition:')
            fast_print(definitions[choice] + '\n')
        elif choice.lower() in ['exit', 'e']:
            break  # Exit the definition lookup
        else:
            fast_print('Invalid definition. Please try again.\n')

def generatePrice():
    price = random.randint(100, 500)
    return price

def checkPay(user, chosen_option, item):
    price = generatePrice()
    fast_print(f'\nA(n) {item} will cost you ${price}.')
    choice = input(f'Would you like to pay that amount? ').upper()
    if choice == 'YES' or choice == 'Y' or choice == 'YEAH':
        fast_print(f"\nYou now have a(n) {item}.")
        user.money -= price
        return True
    else:
        fast_print(f'If you want to change your mind you can try to buy one later!')
        prepList.insert(0, chosen_option)
        return False

def prep(user):
    """Handles the preparation phase, allowing users to choose actions while also looking up definitions."""
    while prepList:  # Continue until all options are used
        fast_print("\nPreparation Options:")
        for i, option in enumerate(prepList, 1):
            fast_print(f"{i}. {option}")
        fast_print(f'Your account balance is ${user.money}.')

        user_choice = getInput()

        if user_choice.lower() == "def":
            checkDefinitions()
            continue  # Go back to showing options

        if user_choice.isdigit():
            user_choice = int(user_choice) - 1  # Convert to 0-based index

            if 0 <= user_choice < len(prepList):
                
                chosen_option = prepList.pop(user_choice)  # Remove chosen item
                if 'map' in chosen_option:
                    fast_print('\nTo find the building information you conduct a search online.')
                    fast_print('After searching for a while you find the layout of the building and now have a map of H.A.C.K HQ! Good job!')
                    user.map = True
                if 'fake' in chosen_option:
                    if user.employee_knowledge == True:
                        tf = checkPay(user, chosen_option, 'fake ID')
                        user.fake_id = tf
                    else:
                        fast_print('You have not yet done OSINT yet so you don\'t know what to put on the fake ID!')
                        prepList.insert(0, chosen_option)
                if 'employees' in chosen_option:
                    fast_print(f"\nYou now know the people that you are likely to run into while there.\n")
                    user.employee_knowledge = True
                if 'lock' in chosen_option:
                    tf = checkPay(user, chosen_option, 'Lock Pick')
                    user.lock_pick = True
                if 'USB' in chosen_option:
                    fast_print(f"\nYou now have a USB with spyware uploaded to it so that you can upload it to their network.\n")
                    user.usb = True
                if "disguise" in chosen_option:
                    tf = checkPay(user, chosen_option, 'disguise')
                    user.disguise = tf
                if 'fit' in chosen_option:
                    if user.fitness < 1:
                        fast_print('You will need to buy a membership first.')
                        tf = checkPay(user, chosen_option, 'gym membership')
                        fast_print('You went to the gym and got a little bit stronger!')
                        prepList.insert(0, chosen_option)
                        user.fitness += 1
                    else:
                        fast_print('You went to the gym and got a little bit stronger!')
                        prepList.insert(0, chosen_option)
                        user.fitness += 1
                if "Finalize plans" in chosen_option:
                    confirm = input("Are you sure you are ready to start the attack? (yes/no): ").strip().lower()
                    if confirm == 'yes':
                        prepList.append(chosen_option)
                        break  # Exit prep loop if user confirms
                    else:
                        prepList.append(chosen_option)  # Add it back if not ready
            else:
                fast_print("Invalid choice. Please select a valid option.")
        else:
            fast_print("Invalid input. Please enter a number or 'def'.")

    fast_print("\nPreparation complete. Moving to the attack phase...\n")
    return user

def noPrepFail(user):
    fast_print('You enter the building. A security guard sees you and approches')
    fast_print(f"""
Security Guard: How can I help you?
{user.name}: Hi! I'm here to help with maintenence!
Security Guard: Let's see some ID.
{user.name}: Oh you know what I must've forgot it!
You know this will not work. You have two options:
1. Leave and prepare better.
2. Fight him.
""")
    tf = True
    while tf:
        try:
            choice = int(input('What would you like to do(1 or 2)? '))
            if choice == 1:
                fast_print('Good choice.')
                tf = False
                return True

            elif choice == 2:
                fast_print('Ok, violence it is.')
                fast_print('You punch him in the face and make a run for the CEO Room.')
                fast_print('You make it about 20 feet before taken down and arrested. Better luck next time.')
                fast_print('GAME OVER')
                tf = False
                return False
            else:
                fast_print('Please enter a 1 or a 2.')
                tf = True
        except:
            fast_print('Please enter a valid option(1 or 2).')
            tf = True

def left(user):
    fast_print("""You turn left at the hallway and head to the CEO Room.
You get to the door and luckily it looks like no one is around, but the door is locked.
""")
    if user.lock_pic == False:
        fast_print("It looks like you don't have a lock pick, so we'll have to break the door down.")
        if user.fitness >= 3:
            fast_print("You were strong enough to knock it down in one go! That increases your chances of no one hearing and catching you.")
            user.risk_level +=1
        else:
            fast_print("Because you didn't go to the gym that often, it took you a couple of tries to knock down the door increasing your chances of someone hearing you.")
            user.risk_level +=3
    elif user.lock_pic == True:
        fast_print("""You try to pick the lock, and after about 5 minutes you are able to break into the room!
Looks like buying a lock pick payed off!
""")
    fast_print("""Now that you are in the room we need to check his computer.
It looks like his computer is locked and needs a password.
You did some OSINT so you can try to guess his password, or you can look around his desk for hints.
Would you like to 
1. Guess the password 
2. look for clues?
""")

    option = True
    while option == True:
        choice = input("Enter a 1 or a 2: ")
        if choice == "1":
            num = random.randint(1, 20)
            if num == 5 or num == 15:
                fast_print("You guessed it!")
                option = False
            else:
                fast_print("Hmm. Looks like we might need to try something else.")
                user.risk_level += 1
                option = True
        elif choice == '2':
            fast_print("Let's take a look around the desk to see if we can find his password.")
            fast_print("\nAfter looking for a while you found a sticky note that says:")
            fast_print("ZWFzeXBhc3N3b3JkMTIz")
            fast_print("This looks like it could be the password, it just looks like its been encoded.")
            fast_print("Visit this website to decode it: https://www.base64decode.org/")
            fast_print("Enter the password when you have it.")
            option2 = True
            while option2:
                passwrd = input("PASSWORD: ")
                if passwrd == 'easypassword123':
                    fast_print("The password is correct!")
                    option2 = False
                else:
                    fast_print("Hmm. That didn't seem to work. Try again.")
                    user.risk_level += 1 
                    option2 = True
            option = False
        else:
            fast_print("Please enter a valid option")
            option = True
    fast_print("Now that you are in the computer you have access to everything!! You plug in the USB and upload the spyware.")
    fast_print("You get out of there as fast as possible. Your work is done!")

def right(user):
    fast_print("""You turn right at the hallway and head to the main server room.
You find the door is slightly propped open!
""")
    tf = True
    while tf:
        fast_print("You enter the server room... and suddenly stop. Two IT staff are inside, talking.")
        fast_print("What do you do?")
        fast_print("1. Hide and observe")
        fast_print("2. Bluff your way in")
        fast_print("3. Cause a distraction")
        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            fast_print("You hide behind a server rack. You overhear them talking about a system update.")
            fast_print("\nYou hide behind a server rack, holding your breath.")
            fast_print("You overhear the IT guys discussing a vulnerability in the backup server.")
            fast_print("Eventually, they leave. The room is yours. You find a desk with an open computer.")
            fast_print("Let's take a look around the desk to see if we can find his password.")
            fast_print("\nAfter looking for a while you found a sticky note that says:")
            fast_print("aGFja2lzZXZpbA==")
            fast_print("This looks like it could be the password, it just looks like its been encoded.")
            fast_print("Visit this website to decode it: https://www.base64decode.org/")
            fast_print("Enter the password when you have it.")
            option2 = True
            while option2:
                passwrd = input("PASSWORD: ")
                if passwrd == 'hackisevil':
                    fast_print("The password is correct!")
                    option2 = False
                else:
                    fast_print("Hmm. That didn't seem to work. Try again.")
                    user.risk_level += 1 
                    option2 = True
            fast_print("✅ Upload complete. You've also gained intel on a backup server!\n")
            user.risk_level += 2
            tf = False

        elif choice == "2":
            fast_print("You confidently walk in, saying you're from HQ. They look at you skeptically...")
            fast_print("\nYou walk in confidently. 'HQ sent me for diagnostics,' you say.")
            fast_print("They look confused but let you approach a terminal.")
            fast_print("You plug in the USB while making small talk.")
            fast_print("✅ Upload complete, but one of them seems suspicious...")
            fast_print("🚨 You hear a faint voice calling security. You need to leave—fast!\n")
            user.risk_level += 5
            tf = False

        elif choice == "3":
            fast_print("You trigger a fake fire alarm. Panic. Everyone clears out. You have 3 minutes.")
            fast_print("You plug in the USB to a computer that got left open due to the chaos. The spyware uploads!")
            fast_print("You now leave as fast as possile.")
            user.risk_level += 10
            tf = False
    
        else:
            print("Invalid choice. Try again.\n")
            tf = True

def full_prep(user):
    fast_print("""\nYou enter the building.
As you enter the building you are stopped by a security guard who asks for your ID.
Because you prepared sufficeintly, you were able to show him your fake ID and he fell for it!
You are now in the building past securirity!
Now lets find a place to plant our USB.
You come to a halway that goes left or right.
\nBecause we have a map we know where the main server room is and where the CEO room is.
To the left is the CEO room, and to the right is the main server room.
Would you like to go left, or right?
""")
    LR = True
    while LR == True:
        choice = input("\nEnter left or right: ").upper()
        if choice == 'L' or choice == 'LEFT':
            left(user)
            LR = False
        elif choice == 'R' or choice == 'RIGHT':
            right(user)
            LR = False
        else:
            fast_print('Please enter a valid option.')
            LR = True
    fast_print("\n....")
    fast_print("....")
    fast_print("....\n")
    fast_print("As you're leaving the building, a security guard stops you.")
    fast_print("The guard asks to see your ID.")
    if user.risk_level >= 7:
        fast_print('He is very suspicious of you because there were reports of suspicious activity.')
        fast_print("You show your ID but he doesn't buy it.")
        fast_print('You can either 1. Run out of there or 2. Try to convince him you work there.')
        oneortwo = True
        while oneortwo == True:
            newchoice = input('Enter a 1 or a 2: ')
            if newchoice == '1':
                fast_print('You ran out of the building without being caught. That was a close one!')
                oneortwo = False
            elif newchoice == '2':
                fast_print('You were able to convince him you work there! Good thing you did your research.')
                oneortwo = False
            else:
                fast_print('Please enter a valid number.')
                oneortwo = True
    fast_print("""\nYou made it out of there alive and well.
Now you just have to wait for the spyware you uploaded to get all the info you need to report them to the police.
.....
.....
.....

""")

def halfPrep(user):
    fast_print('You find your way into an office space and see a lot of computers. You decide to look aroundand find a computer to try to open up.')
    fast_print("You choose a computer and it says it needs a password to unlock.")
    fast_print("""
Would you like to 
1. Guess the password 
2. look for clues?
""")
    option = True
    while option == True:
        choice = input("Enter a 1 or a 2: ")
        if choice == "1":
            num = random.randint(1, 20)
            if num == 5 or num == 15:
                fast_print("You guessed it!")
                option = False
            else:
                fast_print("Hmm. Looks like we might need to try something else.")
                user.risk_level += 1
                option = True
        elif choice == '2':
            fast_print("Let's take a look around the desk to see if we can find his password.")
            fast_print("\nAfter looking for a while you found a sticky note that says:")
            fast_print("YmFzaWNwYXNzd29yZA==")
            fast_print("This looks like it could be the password, it just looks like its been encoded.")
            fast_print("Visit this website to decode it: https://www.base64decode.org/")
            fast_print("Enter the password when you have it.")
            option2 = True
            while option2:
                passwrd = input("PASSWORD: ")
                if passwrd == 'basicpassword':
                    fast_print("The password is correct!")
                    option2 = False
                else:
                    fast_print("Hmm. That didn't seem to work. Try again.")
                    user.risk_level += 1 
                    option2 = True
            option = False
        else:
            fast_print("Please enter a valid option")
            option = True
    fast_print("Now that you are in the computer you have access to everything!! You plug in the USB and upload the spyware.")
    fast_print("You get out of there as fast as possible. Your work is done!")

def stealData(user):
    fast_print('Since you have some sort of disguise or ID we can just walk in through the front doors.\n')
    fast_print("""You walk right past the security and they welcome us without any questions.
You need to find a place to steal the data.
You find a room labeled Server Room. This is where you want to be.
You find the door is locked.
""")
    if user.lock_pic == False:
            fast_print("It looks like you don't have a lock pick, so we'll have to break the door down.")
            if user.fitness >= 3:
                fast_print("You were strong enough to knock it down in one go! That increases your chances of no one hearing and catching you.")
                user.risk_level +=1
            else:
                fast_print("Because you didn't go to the gym that often, it took you a couple of tries to knock down the door increasing your chances of someone hearing you.")
                user.risk_level +=3
    elif user.lock_pic == True:
            fast_print("""You try to pick the lock, and after about 5 minutes you are able to break into the room!
Looks like buying a lock pick payed off!
""")
    fast_print("Now that you are in the room you are able to find and steal information.")
    fast_print("""You find a computer that you think you might be able to find information on.
It looks like the computer is locked and needs a password.
You did some OSINT so you can try to guess the password, or you can look around his desk for hints.
Would you like to 
1. Guess the password 
2. look for clues?
""")
    option = True
    while option == True:
        choice = input("Enter a 1 or a 2: ")
        if choice == "1":
            num = random.randint(1, 20)
            if num == 5 or num == 15:
                fast_print("You guessed it!")
                option = False
            else:
                fast_print("Hmm. Looks like we might need to try something else.")
                user.risk_level += 1
                option = True
        elif choice == '2':
            fast_print("Let's take a look around the desk to see if we can find his password.")
            fast_print("\nAfter looking for a while you found a sticky note that says:")
            fast_print("c3VwZXJzZWN1cmVwYXNzd29yZA==")
            fast_print("This looks like it could be the password, it just looks like its been encoded.")
            fast_print("Visit this website to decode it: https://www.base64decode.org/")
            fast_print("Enter the password when you have it.")
            option2 = True
            while option2:
                passwrd = input("PASSWORD: ")
                if passwrd == 'supersecurepassword':
                    fast_print("The password is correct!")
                    option2 = False
                else:
                    fast_print("Hmm. That didn't seem to work. Try again.")
                    user.risk_level += 1 
                    option2 = True
            option = False
        else:
            fast_print("Please enter a valid option")
            option = True
    fast_print("""Now that we have the password we will need to steal the information.
You find a USB drive next to the computer and start to download as much information as possible to take home and give to the police.
You leave the building as fast as possible. Good job!
""")

def enterBuilding(user):
    fast_print('Now that we are here at H.A.C.K HQ, we need to enter the building.')
    fast_print('As you make choices, your risk level will go up. If you make enough bad choices, you will get caught.')
    if user.usb == True and user.disguise == True and user.fake_id == True: # DONE
        fast_print('Since you have a disguise, fake ID and the USB, we should be safe to enter throught the main entrance undetected.')
        fast_print('We are now entering the building! Good luck!')
        full_prep(user)
        return False
    elif user.usb == True and user.disguise == False or (user.usb == True and user.fake_id == False): # DONE
        fast_print('Since we do not have a disguise or a fake ID, they might detect that we do not work there... Let\'s try to find a backdoor.')
        fast_print("It looks like there's a backdoor that is propped open! Lets go ahead and enter it!\n")
        halfPrep(user)
        return False
    elif (user.usb == False and user.disguise == True) or (user.usb == False and user.fake_id == True): # IF NO USB BUT THEY HAVE DISGUISE OR NO USB BUT YES ID
        fast_print("Since we have no USB, let's see if we can find another way to steal data from them.")
        fast_print('We are now entering the building! Good luck!')
        stealData(user)
        return False
    elif user.usb == False and user.disguise == False and user.fake_id == False: # Done
        fast_print('Since we did almost no preparation, we might just have to fight our way in and hopefully get through.')
        fast_print('We are now entering the building! Good luck!')
        tf = noPrepFail(user)
        return tf

def phase1(user):
    fast_print(f'''.....
.....\n
Now we are going to enter the building.
Our objective, {user.name}, is to find a place to plug in our USB and upload our spyware.
''')
    usbCheck = input("You did prepare a USB with the spyware, right? ")
    if user.usb == True:
        fast_print("Looks like we're good to go then! Let's head over to the building and start our attack.")
        enterBuilding(user)
    else:
        fast_print("Oh no! It looks like we actually don't have one prepared.")
        fast_print('Well, it looks like we will have to either go back and prepare the USB and spyware.')
        fast_print("Or we could get into the building and find another way to take them down.")
        fast_print('What would you like to do?')
        fast_print('1. Go back and prepare it.')
        fast_print('2. Stay and carry out the attack.')
        usbChoice = input('Enter 1 or 2').strip()
        if usbChoice == '1':
            fast_print("OK! Let's go back and prepare again so that we are ready for anything!")
            return True
        elif usbChoice == '2':
            fast_print('We will carry out the attack then! We will just have to find another way')
            tf = enterBuilding(user)
            return tf
        else:
            fast_print("I didn't quite understand that. We'll just go back and prepare again anyways so that we are 100% sure")
            return True

def main():
    """Main game function."""
    user = getUserInfo()
    phaseChoice = True
    while phaseChoice == True:
        fast_print('\nTo carry out this attack, we will need some preparation.')
        fast_print('We are planning on infiltrating the building and getting into their network manually.\n')
        fast_print('The process of finding out information about people, companies, building layouts, etc. is calld OSINT.')
        fast_print('We have a couple of things that we can do to make sure we are ready to carry out the attack.')
        user = prep(user)
        phaseChoice = phase1(user)
    fast_print('Six weeks have passed. You have now collected all of the data you need to report them to the police.')
    fast_print('You anonymously report them to the police and a full on investigation is started.')
    fast_print('H.A.C.K. is taken down and justice is served!')
    fast_print(f'Good work {user.name}! You have helped stop an evil organization from doing even more damage.')
    fast_print("I hope that you've learned a thing or two about how cybersecurity works!\n")
    finish()

if __name__ == '__main__':
    main()

"""
First we are going to get the user info
Next we will do some prep to get ready for the attack. The more prep they do, the better prepared they will be for any challenge that they face.
Next the attack will start and there will be 3 phases.
Phase 1 is enter the building.
Phase 2 is locate a computer to upload the malware.
Phase 3 is escape.
Lastly is watch the company burn down to the ground and report them to the police.

"""
