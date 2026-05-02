"""
Task 4: Create a simple assistant bot that can store and manage contacts.
"""
from colorama import Fore


def parse_input(user_input: str) -> tuple[str, list[str]]:
    """Parse user input into command and arguments."""
    parts = user_input.strip().split()
    if not parts:
        return "", []
    cmd = parts[0].strip().lower()
    return cmd, parts[1:]

def add_contact(args: list[str], contacts: dict[str, str]) -> str:
    """Add a new contact with name and phone number to contacts."""
    if len(args) != 2:
        return f"{Fore.RED}Usage: add <name> <phone>{Fore.RESET}"

    name, phone = args

    if name in contacts:
        return f"{Fore.RED}Contact already exists. Use 'change'.{Fore.RESET}"

    contacts[name] = phone
    return f"{Fore.GREEN}Contact added.{Fore.RESET}"

def change_contact(args: list[str], contacts: dict[str, str]) -> str:
    """Change the phone number of an existing contact in contacts."""
    if len(args) != 2:
        return f"{Fore.RED}Usage: change <name> <phone>{Fore.RESET}"

    name, phone = args

    if name not in contacts:
        return f"{Fore.RED}Contact not found.{Fore.RESET}"

    contacts[name] = phone
    return f"{Fore.GREEN}Contact updated.{Fore.RESET}"

def show_phone(args: list[str], contacts: dict[str, str]) -> str:
    """Show the phone number of a contact by name."""
    if len(args) != 1:
        return f"{Fore.RED}Usage: phone <name>{Fore.RESET}"

    name = args[0]
    return contacts.get(name, f"{Fore.RED}Contact not found.{Fore.RESET}")

def show_all(contacts: dict[str, str]) -> str:
    """Show all contacts in the format: {name}: {phone}."""
    if not contacts:
        return f"{Fore.RED}No contacts found.{Fore.RESET}"

    result = "\n".join(
        f"{name}: {phone}"
        for name, phone in contacts.items()
    )
    return f"{Fore.GREEN}{result}{Fore.RESET}"

def main():
    contacts = {}
    print(f"{Fore.GREEN}Welcome to the assistant bot!{Fore.RESET}")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ("close", "exit"):
            print(f"{Fore.GREEN}Good bye!{Fore.RESET}")
            break

        if command == "hello":
            print(f"{Fore.GREEN}How can I help you?{Fore.RESET}")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print(f"{Fore.RED}Invalid command.{Fore.RESET}")

if __name__ == "__main__":
    main()
