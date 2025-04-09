import sys
import time

def  finish():
    fast_print("Victory is ours. Thank you for your help.")
    fast_print("H.A.C.K has been exposed for what they truely are.")
    fast_print("Goodbye")
    sys.exit()

def fast_print(text= '', delay=0.03):
    """Prints text one character at a time very fast."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def start():
    fast_print("\n🎮 Welcome to the Brute-Force Scenario!")
    fast_print("You’re a beginner hacker attempting a brute-force attack on a small business website.")
    fast_print("Do you want to...")
    fast_print("1) Start brute-forcing the login with a password list")
    fast_print("2) Scan the site for other vulnerabilities first")
    fast_print("3) Walk away and avoid illegal activity")
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
    fast_print("3) Report the issue anonymously")
    choice = input("Enter 1, 2, or 3: ")

    if choice == "1":
        fast_print("\n⚠️ You capture credentials but are detected on the network.")
        fast_print("You’ve been flagged. Authorities are investigating.")
        game_over("Bad Ending: You went too far.")
    elif choice == "2":
        brute_force()
    elif choice == "3":
        fast_print("\n✅ You report the issue anonymously.")
        fast_print("The business patches the vulnerability. You feel like a cyber Robin Hood.")
        game_over("Good Ending: Ethical hacker in the making!")
    else:
        fast_print("Invalid input.")
        scan_vulnerabilities()

def walk_away():
    fast_print("\n👏 You chose not to break the law.")
    fast_print("You decide to pursue a legal and ethical career in cybersecurity.")
    game_over("Good Ending: Morally correct!")

def explore_dashboard():
    fast_print("\n📂 You access employee records, salaries, and customer emails.")
    fast_print("What do you do?")
    fast_print("1) Leak the data")
    fast_print("2) Screenshot and leave")
    fast_print("3) Report the weak security anonymously")
    choice = input("Enter 1, 2, or 3: ")

    if choice == "1":
        fast_print("\n🚨 Authorities trace the breach back to your IP.")
        game_over("Bad Ending: Arrested for data breach.")
    elif choice == "2":
        fast_print("\n😬 You leave with screenshots, but guilt follows.")
        game_over("Semi-bad Ending: You knew it was wrong.")
    elif choice == "3":
        fast_print("\n✅ You notify the business anonymously.")
        fast_print("They patch it. You feel like a responsible hacker.")
        game_over("Good Ending: Nice work!")
    else:
        fast_print("Invalid input.")
        explore_dashboard()

def backdoor():
    fast_print("\n🕳️ You plant a backdoor for future access.")
    fast_print("Weeks later, someone else finds it and exploits the system worse than you did.")
    game_over("Semi-bad Ending: You're partially responsible.")

def log_out():
    fast_print("\n🚪 You log out and erase your tracks.")
    fast_print("No one knows what you did... for now.")
    game_over("Gray Ending: You got away with it, but was it worth it?")

def game_over(ending):
    fast_print(f"\n🔚 GAME OVER: {ending}")
    finish()

if __name__ == "__main__":
    start()