from functions import interaction_comands as ic

def main():

    contact_dict = {}
    msg = '///   hello   ///   add name phone   ///   change name new_phone   ///   all OR phone name   ///   exit OR close   ///'

    while True:
        user_input = input('Enter command: ')

        # cmd = ic.parce_input(user_input) 

        input_tuple = ic.parce_input(user_input)
        cmd = input_tuple[0]
        argument_list = input_tuple[1]

        match cmd.casefold():

            case "hello":
                print(ic.greeting())

            case 'exit' | 'close':
                break

            case 'add':
                print(ic.add_contact(argument_list, contact_dict))

            case 'all':
                print(ic.show_all(contact_dict))

            case 'phone':
                print(ic.show_phone(argument_list, contact_dict))

            case 'change':
                print(ic.change_contact(argument_list, contact_dict))
            case 'help':
                print(msg)     
            case _:
                print('Something went wrong. You can view all available commands using the command: help')



if __name__ == "__main__":
    main()
