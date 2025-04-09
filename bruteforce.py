import sys
import time

def fast_print(text= '', delay=0.03):
    """Prints text one character at a time very fast."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def start():
    fast_print("\n🎮 Welcome to the Brute-Force Scenario!")
    fast_print("In this scenario, we will attempt a brute-force attack on the evil organization.")
    fast_print("Do you want to...")
    fast_print("1) Start brute-forcing the login with a password list")
    fast_print("2) Scan the site for other vulnerabilities first")
    fast_print("3) Walk away and avoid getting caught")
    choice1 = input("Enter 1, 2, or 3: ")

    if choice1 == "1":
        brute_force()
    elif choice1 == "2":
        scan_vulnerabilities()
    elif choice1 == "3":
        walk_away()
    else:
        fast_print("Invalid input.")
        start()

def brute_force():
    fast_print("\n🔓 You begin brute-forcing with a basic password list (password, admin, 123, etc)...")
    fast_print("After 1000 attempts, you succeed!")
    fast_print("Credentials found: admin / admin123")
    fast_print("What do you want to do next?")
    fast_print("1) Explore the dashboard for data")
    fast_print("2) Plant a backdoor")
    fast_print("3) Log out and disappear")
    choice = input("Enter 1, 2, or 3: ")

    if choice == "1":
        explore_dashboard()
    elif choice == "2":
        backdoor()
    elif choice == "3":
        log_out()
    else:
        fast_print("Invalid input.")
        brute_force()

def scan_vulnerabilities():
    fast_print("\n🧪 Scanning for vulnerabilities...")
    fast_print("You discover the site is running HTTP and sends passwords in plain text.")
    fast_print("What do you do?")
    fast_print("1) Capture credentials via a MITM (Man in the Middle) attack")
    fast_print("2) Go back and brute-force instead")
    choice = input("Enter 1 or 2: ")

    if choice == "1":
        fast_print("\n⚠️ You capture credentials but are detected on the network.")
        fast_print("You’ve been flagged. The company is investigating.")
        game_over("Bad Ending: You went too far and were caught.")
    elif choice == "2":
        brute_force()
    else:
        fast_print("Invalid input.")
        scan_vulnerabilities()

def walk_away():
    fast_print("\nYou chose not to look farther into the company.")
    fast_print("Although you won't be caught, the evil company takes over the world.")
    game_over("Bad Ending: The evil organization takes over the world. You might've been able to stop it!")

def explore_dashboard():
    fast_print("\n📂 You access company financial info, logins, and plans.")
    fast_print("What do you do?")
    fast_print("1) Leak the data")
    fast_print("2) Screenshot and leave")
    choice = input("Enter 1 or 2: ")

    if choice == "1":
        fast_print("\n🚨 The company traces the leak back to your IP.")
        game_over("Bad Ending: Your physical security has been compromised.")
    elif choice == "2":
        fast_print("\n😬 You leave with valuable screenshots that can be used to take the company down.")
        game_over("Good Ending: You are helping towards taking down the organization.")
    else:
        fast_print("Invalid input.")
        explore_dashboard()

def backdoor():
    fast_print("\n🕳️ You plant a backdoor for future access.")
    fast_print("You may potentially be able to use this at a later date.")
    game_over("Semi-good Ending: You didn't take down the company, but the backdoor is a valuable asset to have.")

def log_out():
    fast_print("\n🚪 You log out and erase your tracks.")
    fast_print("They don't know what you did... for now.")
    game_over("Gray Ending: You got in, but do they know?")

def game_over(ending):
    fast_print(f"\n🔚 GAME OVER: {ending}")
    fast_print("\nThanks for playing!")

if __name__ == "__main__":
    start()