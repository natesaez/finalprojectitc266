def start():
    print("\n🎮 Welcome to the Brute-Force Scenario!")
    print("You’re a beginner hacker attempting a brute-force attack on a small business website.")
    print("Do you want to...")
    print("1) Start brute-forcing the login with a password list")
    print("2) Scan the site for other vulnerabilities first")
    print("3) Walk away and avoid illegal activity")
    choice1 = input("Enter 1, 2, or 3: ")

    if choice1 == "1":
        brute_force()
    elif choice1 == "2":
        scan_vulnerabilities()
    elif choice1 == "3":
        walk_away()
    else:
        print("Invalid input.")
        start()

def brute_force():
    print("\n🔓 You begin brute-forcing with a basic password list (password, admin, 123, etc)...")
    print("After 1000 attempts, you succeed!")
    print("Credentials found: admin / admin123")
    print("What do you want to do next?")
    print("1) Explore the dashboard for data")
    print("2) Plant a backdoor")
    print("3) Log out and disappear")
    choice = input("Enter 1, 2, or 3: ")

    if choice == "1":
        explore_dashboard()
    elif choice == "2":
        backdoor()
    elif choice == "3":
        log_out()
    else:
        print("Invalid input.")
        brute_force()

def scan_vulnerabilities():
    print("\n🧪 Scanning for vulnerabilities...")
    print("You discover the site is running HTTP and sends passwords in plain text.")
    print("What do you do?")
    print("1) Capture credentials via a MITM (Man in the Middle) attack")
    print("2) Go back and brute-force instead")
    print("3) Report the issue anonymously")
    choice = input("Enter 1, 2, or 3: ")

    if choice == "1":
        print("\n⚠️ You capture credentials but are detected on the network.")
        print("You’ve been flagged. Authorities are investigating.")
        game_over("Bad Ending: You went too far.")
    elif choice == "2":
        brute_force()
    elif choice == "3":
        print("\n✅ You report the issue anonymously.")
        print("The business patches the vulnerability. You feel like a cyber Robin Hood.")
        game_over("Good Ending: Ethical hacker in the making!")
    else:
        print("Invalid input.")
        scan_vulnerabilities()

def walk_away():
    print("\n👏 You chose not to break the law.")
    print("You decide to pursue a legal and ethical career in cybersecurity.")
    game_over("Good Ending: Morally correct!")

def explore_dashboard():
    print("\n📂 You access employee records, salaries, and customer emails.")
    print("What do you do?")
    print("1) Leak the data")
    print("2) Screenshot and leave")
    print("3) Report the weak security anonymously")
    choice = input("Enter 1, 2, or 3: ")

    if choice == "1":
        print("\n🚨 Authorities trace the breach back to your IP.")
        game_over("Bad Ending: Arrested for data breach.")
    elif choice == "2":
        print("\n😬 You leave with screenshots, but guilt follows.")
        game_over("Semi-bad Ending: You knew it was wrong.")
    elif choice == "3":
        print("\n✅ You notify the business anonymously.")
        print("They patch it. You feel like a responsible hacker.")
        game_over("Good Ending: Nice work!")
    else:
        print("Invalid input.")
        explore_dashboard()

def backdoor():
    print("\n🕳️ You plant a backdoor for future access.")
    print("Weeks later, someone else finds it and exploits the system worse than you did.")
    game_over("Semi-bad Ending: You're partially responsible.")

def log_out():
    print("\n🚪 You log out and erase your tracks.")
    print("No one knows what you did... for now.")
    game_over("Gray Ending: You got away with it, but was it worth it?")

def game_over(ending):
    print(f"\n🔚 GAME OVER: {ending}")
    print("\nThanks for playing!")

if __name__ == "__main__":
    start()