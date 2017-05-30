if __name__ == '__main__':

    from views import Menu
    from controllers import Controller

    controller = Controller()
    menu = Menu()

    while True:
        menu.print_menu()
        command = menu.read_number_of_menu_item()
        if command.__contains__("key"):
            getattr(controller, command["action"])(command["key"])
        else:
            getattr(controller, command["action"])()
