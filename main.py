import bot.helpers.logger as logger
import bot.helpers.storage as storage
from bot.models.AddressBook import AddressBook
from bot.models.Record import Record
import bot.contactCommands as contact
# import questionary

# answer = questionary.select(
#     "Що ви хочете зробити?",
#     choices=["Додати запис", "Видалити запис", "Вихід"]
# ).ask()

# if answer == "Додати запис":
#     add_record_function()

@logger.input_error
def parse_input(user_input):
    if not user_input.strip():
        raise ValueError
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def show_commands():
    text = {
        'Add New User': "add <username> <phone>",
        'Change user phone': "change <username> <new phone>",
        'Check user phone': "phone <username>",
        "See all contacts": "all",
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
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            storage.save_data(contacts)
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(contact.add_contact(args, contacts))
        elif command == "change":
            print(contact.change_contact(args, contacts))
        elif command == "phone":
            print(contact.show_phone(args, contacts))
        elif command == "all":
            print(contact.show_all(contacts))
        elif command == "add-birthday":
            print(contact.add_birthday(args, contacts))
        elif command == "show-birthday":
            print(contact.show_birthday(args, contacts))
        elif command == "birthdays":
            print(contact.birthdays(contacts))
        elif command == "remove-phone":
            print(contact.remove_phone(args, contacts))
        elif command == "help":
            show_commands()
        else:
            print("Invalid command. Enter 'help' to see all commands.")

if __name__ == "__main__":
    main()
