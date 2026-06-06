from datetime import date
def write_entry(entry):
    today = date.today()
    file = open("diary.txt", "a")
    file.write(str(today) + " | " + entry + "\n")
    file.close()
    print("Entry saved successfully!")

def read_entries():
    try:
        file = open("diary.txt", "r")
        content = file.read()
        file.close()
        if content == "":
            print("No entries yet")
        else:
            print("\n--- Your Diary ---")
            print(content)
            print("-------------------")
    except FileNotFoundError:
        print("No diary found. Write your first entry!")

def clear_diary():
    file = open("diary.txt", "w")
    file.write("")
    file.close()
    print("Diary cleared!")

# Main program
while True:
    print("\n1. Write entry")
    print("2. Read All Entries")
    print("3. Clear Diary")
    print("4. Exit")

    choice = input("Enter choice (1-4): ")

    if choice == "1":
        entry = input("Write your entry: ")
        write_entry(entry)
    elif choice == "2":
        read_entries()
    elif choice == "3":
        clear_diary()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
