import bot.helpers.logger as logger
import bot.helpers.storage as storage
import bot.cli.contactCommands as contact
import bot.helpers.parse_input as parse
# import questionary

# answer = questionary.select(
#     "Що ви хочете зробити?",
#     choices=["Додати запис", "Видалити запис", "Вихід"]
# ).ask()

# if answer == "Додати запис":
#     add_record_function()


def show_commands():
    text = {
        'Add New User': "add <username> <phone>",
        'Change user phone': "change <username> <new phone>",
        'Check user phone': "phone <username>",
        "See all contacts": "all",
        "Add Email": "add-email <username> <email@email.com>",
        "Add Birthday": "add-birthday <username> <DD.MM.YYYY>",
        "Check User's Birthday": "show-birthday <username>",
        "Upcoming birthdays (next 7 days)": "birthdays",
        "Remove phone": "remove-phone <username> <phone>"
    }
    print("    List of available commands:")
    for purpose, command in text.items():
        print(f"    > {purpose}: {command}")  


def main():
    contacts = storage.load_data()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse.parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            storage.save_data(contacts)
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(contact.add_contact(args, contacts))
        elif command == "remove":
            print(contact.remove_contact(args, contacts))
        elif command == "change":
            print(contact.change_contact(args, contacts))
        elif command == "remove-phone":
            print(contact.remove_phone(args, contacts))
        elif command == "phone":
            print(contact.show_phone(args, contacts))
        elif command == "all":
            print(contact.show_all(contacts))
        elif command == "add-birthday":
            print(contact.add_birthday(args, contacts))
        elif command == "add-email":
            print(contact.add_email(args, contacts))
        elif command == "remove-email":
            print(contact.remove_email(args, contacts))
        elif command == "change-email":
            print(contact.edit_email(args, contacts))
        elif command == "add-address":
            print(contact.add_address(args, contacts))
        elif command == "remove-address":
            print(contact.remove_address(args, contacts))
        elif command == "change-address":
            print(contact.change_address(args, contacts))
        elif command == "show-birthday":
            print(contact.show_birthday(args, contacts))
        elif command == "birthdays":
            print(contact.birthdays(contacts))
        elif command == "help":
            show_commands()
        else:
            print("Invalid command. Enter 'help' to see all commands.")

if __name__ == "__main__":
    main()
