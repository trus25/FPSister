import Pyro4


def client_init():
    input_ip = input(">> Input server's IP address(or just enter if testing on local): ")
    if input_ip == "":
        _address = "localhost"
    else:
        _address = input_ip

    _name = input(">> Input your name: ")

    return _name, _address


def connect(_name, _address):
    _uri = "PYRONAME:game_server@" + _address + ":7777"
    _server = Pyro4.Proxy(_uri)
    print("test")
    print(_server.register_client(_name).get("message"))
    return _uri, _server


def get_data(response: dict):
    return response.get("data")


def print_menu():
    print("List of available services(with keyword for using it):")
    print("1. Print game board (board)")
    print("2. Start the game (start)")
    print("3. Fill game board (fill <index>)")
    # print("4. Edit content of selected file(file_edit <filename>")
    # print("5. Delete a text file on your current lucky number folder(file_delete <filename>)")
    # print("6. Change your lucky number(ln_change <number>)")
    # print("7. Print your current lucky number(ln_print)")
    # print("8. Print services list(help)")
    print("9. Exit program (exit)")


if __name__ == "__main__":
    symbol = ""
    connected = True

    name, address = client_init()

    uri, server = connect(name, address)
    print("Welcome {}! Type 'menu' without quotes to see all possible commands!".format(name))

    try:
        while connected:
            user_request = input(">> ")
            split = user_request.split(" ")

            if split[0] == "board":
                print(server.get_board())
            elif split[0] == "start":
                print(server.start_game(name))
            elif split[0] == "fill" and len(split) == 3:
                print(server.fill_board(name, int(split[1]), int(split[2])))
            elif split[0] == "menu":
                print_menu()
            elif split[0] == "exit":
                connected = False
            else:
                print("Command not found or incomplete!")
    finally:
        print(server.remove_client(name, role))
        print("Good bye {}!".format(name))



