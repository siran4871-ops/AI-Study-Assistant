
print("================================")
print("       AI STUDY ASSISTANT")
print("          VERSION 2.0")
print("================================")

name = input("Enter your name: ")

print("\nWelcome", name, "!")

while True:
    print("\n===== MAIN MENU =====")
    print("1. Study Tips")
    print("2. Python Basics")
    print("3. Python Quiz")
    print("4. Motivation")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        print("\nStudy Tip:")
        print("Study for 25 minutes.")
        print("Take a 5-minute break.")

    elif choice == "2":
        print("\nPython Basics")
        print("Python is a programming language.")
        print("Example: print('Hello World')")

    elif choice == "3":
        print("\nPython Quiz")
        print("Question: Which keyword is used to create a function?")
        print("A. loop")
        print("B. def")
        print("C. print")

        answer = input("Your answer: ").lower()

        if answer == "b":
            print("Correct! Excellent!")
        else:
            print("Incorrect. Correct answer is B (def).")

    elif choice == "4":
        print("\nKeep learning!")
        print("Small steps create big achievements.")

    elif choice == "5":
        print("Thank you for using AI Study Assistant!")
        break

    else:
        print("Invalid choice. Try again.")
        
