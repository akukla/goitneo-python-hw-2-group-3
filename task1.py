def input_error(msg):
    def actual_decorator(func):
        def inner(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except (KeyError, ValueError, IndexError):
                return msg
        return inner
    return actual_decorator

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error("Give me name and phone please")
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error("Give me name and phone please")
def change_contact(args, contacts):
    name, phone = args
    if name not in contacts:
        return "Contact not found"
    contacts[name] = phone
    return "Contact updated."

@input_error("Enter user name")
def get_contact(args, contacts):
    name, = args
    if name not in contacts:
        return "Contact not found"
    return contacts[name]


def get_all_contact(args, contacts):
    if len(contacts) == 0:
        return 'Address book is empty'
    ret = []
    for key in contacts:
        ret.append(f'{key}: {contacts[key]}')
    return '\n'.join(ret)


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(get_contact(args, contacts))
        elif command == "all":
            print(get_all_contact(args, contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()