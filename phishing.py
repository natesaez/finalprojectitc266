import csv

def beginning():
    a = input('You chose to attempt to hack the company through phishing.\nDo you already know what phishing is? y/n: ')
    if a == "y":
        print()
        phishing_attack()
    elif a == "n":
        explain_phishing()

def explain_phishing():
    print()
    print("Phishing is the practice of sending fraudulent communications that appear to come from a legitimate and reputable source,\nusually through email and text messaging")
    print("If you want to learn more, go to this link: https://www.phishing.org/what-is-phishing")
    print()
    print("Today we will be working on a specific type of phishing called spear phishing.")
    print("Spear phishing uses specific and tailored messages to try and get information. Phishing is general, spear phishing is for specific people")
    a = input('Are you ready? y/n: ')
    if a == "y":
        print("\nGood\n")
        phishing_attack()
    elif a == "n":
        print("\nYou'll figure it out... probably\n")
        phishing_attack()

def phishing_attack():
    link = "www.thisisasafelink.com"
    print(f"I have the following link {link} which will inject crippling malware onto their computers if clicked on.")
    print("Your job is to get someone in the company to click on the link.")
    input("If you're ready to move on, click enter ")
    print()
    input("I found this csv file for you that contains several employees information. (Press enter to view it)\n")
    counter = 0
    while True:
        counter += 1
        if counter > 3:
            print("Uh oh. Because you've sent 3 different emails, they realized that someone is trying to phish them.\n"
            "They won't be falling for any more emails. Try a different attack now or wait a bit and try phishing again later.")
            return
        employees = read_csv('employees_extended.csv')
        email, subject, content = phishing_email()
        if pass_test(email, subject, content, employees, link):
            break
        else:
            input("Try again! (Press enter to proceed) ")


def phishing_email():
    email = ''
    content = ''
    print("\nNow you need to craft your phishing email. Remember, these employees have been trained well on phishing emails.\n")
    print("In order for your email to work, you'll need to make it urgent, using words like 'Now', 'Quick' or 'Urgent'\n")
    input("You'll also need to choose the right person and include the link in the email. Make sure it looks professional too. Press enter when you are done with a step.")

    email = input("Email address: ")
    subject = input("Subject: ")
    print("Enter your email content. Press Enter on an empty line to finish:")
    content_lines = []
    while True:
        line = input()
        if line == "":  
            break
        content_lines.append(line)

    content = "\n".join(content_lines)

    print("\nYour email looks like this:\n")
    print(f"""
--------------------------------------------
From: You <your-email@example.com>
To: {email}
Subject: {subject}
--------------------------------------------

{content}

Best regards,
Your Name
--------------------------------------------
    """)
    print()
    return email, subject, content

def pass_test(email, subject, content, employees, link):
    urgency_words = ["Now", "Quick", "Urgent", "now", "quick", "urgent", "Hurry", "hurry", "immediately", "Immediately"]
    input("Lets see if your email worked...\n")

    if email == "jack@example.com" and any(word in content for word in urgency_words) and link in content:
        print("You did it! Jack is older than the other employees by 10 years and works in human resources.\n"
        "His skillset is working with people, and he is unfamiliar with technology and phishing scams. He didn't hesitate to click the link.")
        print("Now their servers are infected with malware! Good job.")
        return True
    elif link not in content:
        print("You didn't even put the link in the email! Redo it and make sure to include the link.")
    elif not any(word in content for word in urgency_words):
        print("There wasn't a sense of urgency in your email, so the employee had time to realize this email was a scam.\nMake sure to include words like 'Now', 'Quick', or 'Urgent'.")

    elif email != "jack@example.com":
        print("Looks like a good email, but this person was too smart to fall for it. Try looking at the employee list and find someone who is more susceptable.")
    return False

def read_csv(path):
    employees = []
    with open(path, mode='r') as file:
        reader = csv.DictReader(file)
    
        for row in reader:
            employees.append(row)
            print(f"Employee Name: {row['name']}")
            print(f"Position: {row['position']}")
            print(f"Age: {row['age']}")
            print(f"Email: {row['email']}\n")
    return reader

def main():
    beginning()

if __name__ == "__main__":
    main()