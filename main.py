
print("================================")
print("     AI STUDY ASSISTANT")
print("================================")

name = input("Enter your name: ")

print("\nWelcome", name, "!")
print("Your AI Study Assistant is ready.")

while True:
    print("\nWhat do you want to do?")
    print("1. Study Tips")
    print("2. Python Basics")
    print("3. Motivation")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Study Tip: Study for 25 minutes and take a 5-minute break.")

    elif choice == "2":
        print("Python is a beginner-friendly programming language.")
        print("Example: print('Hello World')")

    elif choice == "3":
        print("Keep learning. Small steps create big achievements!")

    elif choice == "4":
        print("Thank you for using AI Study Assistant!")
        break

    else:
        print("Invalid choice. Please try again.")
        
