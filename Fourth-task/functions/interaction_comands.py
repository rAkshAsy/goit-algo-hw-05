def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Enter the argument for the command"
        except KeyError:
            return "Sorry, this name is already taken. Please, enter another name."
        except IndexError:
            return "There`s no contact with this name. Please, enter another name."

    return inner


@input_error
def parce_input(user_input:str) -> tuple:
    cmd, *args = user_input.split(' ')
    cmd = cmd.strip().casefold()
    return cmd, args


@input_error
def add_contact(args: list, contacts: dict) -> str:
    name, phone = args
    if not name in contacts:
        contacts[name] = phone
        return f'Contact {name} added!'
    raise KeyError()


def show_all(contacts: dict) -> None:
    for name, phone in contacts.items():
        return f'{name}: {phone}'


@input_error
def show_phone(args_list: list, contacts: dict) -> str:
    name = args_list[0]
    if name in contacts:
        return contacts.get(name)
    raise IndexError


@input_error
def change_contact(args_list: list, contacts: dict) -> str:
    name, phone = args_list[0], args_list[1]
    if name in contacts:
        contacts[name] = phone
        return f'Contact updated: {name} {phone}'
    raise IndexError()
        

def greeting() -> str:
    return "Hi! How can I help you?"
