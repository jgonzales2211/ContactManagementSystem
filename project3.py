# Contact Management Systems

contacts = [["Betty Johnson", "betty.johnson@gmail.com", "(408) 111-2222", "3333"],
            ["Mark Arlington", "mark.arlington@yahoo.com", "(669) 123-4567", "4444"]]

def display(contacts):
    """Shows all contacts on the list."""
    print("COMMAND MENU")
    for i in range(len(contacts)):
        print(f"{i+1}. {contacts[i][0]}, {contacts[i][3]}")
        print()
        
def add(contacts):
    """Adds new contact to the list."""
    name = input("Name: ")
    email = input("Email: ")
    phone = input("Phone: ")
    id = input("ID: ")
    contact = [name, email, phone, id]
    contacts.append(contact)
    print(f"{name}, {id} was added. \n")
    
    """Displays a specified contact from the list."""
def view(contacts):
    while True:
        try:
            number = int(input(f"Number (1 - {len(contacts)}): "))
            if 1 <= number <= len(contacts):
                contact = contacts[number - 1]
                print(f"{contact[0]}, {contact[3]}\n")
                break
            else:
                print("Invalid number. Try again!")
        except ValueError:
            print("Invalid number. Try again!")
            
    """Removes specified contact from the list."""
def delete(contacts):
    while True:
        try:
            number = int(input(f"Number (1 - {len(contacts)}): "))
            if 1 <= number <= len(contacts):
                contact = contacts.pop(number - 1)
                print(f"{contact[0]}, {contact[3]} was deleted.\n")
                break
            else:
                print("Invalid number. Try again!")
        except ValueError:
            print("Invalid number. Try again!")
    
    """Display the title of the program."""
def display_title():
    print("Contact Management System\n")
    
def display_menu():
    """Displays menu."""
    print("COMMAND MENU")
    print("list - Display all contacts")
    print("view - View a contact")
    print("add - Add a contact")
    print("del - Delete a contact")
    print("exit - Exit program\n")
    
    """Starts the Contact Management System program."""
def main():
    display_title()
    display_menu()
    while True:
        command = input("Command: ")
        if command == "list":
            display(contacts)
        elif command == "view":
            view(contacts)
        elif command == "add":
            add(contacts)
        elif command == "del":
            delete(contacts)
        elif command == "exit":
            print("\nThank you for using my app")
            break
        else:
            print("Invalid command. Try again!\n")
if __name__ == "__main__":   
    main()
            

    
    