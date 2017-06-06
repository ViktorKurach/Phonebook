class Menu:
    _menu = [

        {
            'id': '1',
            'command': 'Get subscribers',
            'action': 'get_all_subscribers'
        },
        {
            'id': '2',
            'command': 'Add new subscriber',
            'action': 'add_new_subscriber'
        },
        {
            'id': '3',
            'command': 'Find subscriber by name',
            'action': 'find_subscriber',
            'key': 'subscriber'
        },
        {
            'id': '4',
            'command': 'Find subscriber by phone',
            'action': 'find_subscriber',
            'key': 'phone'
        },
        {
            'id': '5',
            'command': 'Update subscriber\'s name',
            'action': 'update_subscriber',
            'key': 'subscriber'
        },
        {
            'id': '6',
            'command': 'Update subscriber\'s phone',
            'action': 'update_subscriber',
            'key': 'phone'
        },
        {
            'id': '7',
            'command': 'Remove subscriber by name',
            'action': 'delete_subscriber'
        },
        {
            'id': '8',
            'command': 'Exit',
            'action': 'save_and_exit'
        }

    ]

    def read_number_of_menu_item(self):
        """
        wait for command from Console: command is the number of menu item
        to run it. After entering check entered data and, if command is valid,
        returns dict with command id, command title and action.
        Otherwise run itself again.
        """
        try:
            num = int(input('Enter command number:\n> '))
            if num <= 0 or num > len(self._menu):
                return self.read_number_of_menu_item()
            return self.get_item(num)
        except ValueError:
            return self.read_number_of_menu_item()

    def print_menu(self):
        """
        print Menu of program
        """
        for item in self._menu:
            print(item['id'] + ') ' + item['command'])

    def get_item(self, command):
        """
        returns dict from _menu with command id, command title,
        controller and action by id
        """
        return next(item for item in self._menu if item['id'] == str(command))


class Subscriber:
    def enter_subscriber(self):
        """
        read new subscriber's name from Console.
        Return name
        """
        name = input('Enter subscriber\'s name:\n> ')
        if len(name) <= 3:
            raise ValueError()
        return name

    def enter_phone_number(self):
        """
        read new subscriber's phone number from Console.
        Return phone number
        """
        phone = input('Enter phone number:\n> ')
        if len(phone) <= 5:
            raise ValueError()
        return phone

    def enter_new_subscriber_and_phone_number(self):
        """
        call enter_subscriber(), enter_phone_number() and return their results
        """
        return self.enter_subscriber(), self.enter_phone_number()

    def out_subscribers_and_their_phone_numbers(self, subscribers):
        """
        print subscribers as
        Name: subscriber's name
        Phone: subscriber's phone number
        ...
        """
        if len(subscribers) == 0 or subscribers == [None]:
            print('\nDatabase is empty or subscriber not found')
            return
        print('')
        for sub in subscribers:
            print('Name: %s\nPhone: %s\n' % (sub['subscriber'], sub['phone']))
        input('Press any key to continue\n')

    def enter_subscribers_data(self, key):
        """
        read and return subscriber's name or phone number from console.
        if key == 'subscriber' read subscriber's name, else phone number
        """
        if key == 'subscriber':
            value = self.enter_subscriber()
        else:
            value = self.enter_phone_number()
        return value


class MessagePrinter:
    def print_message_of_error_entering_data(self):
        print('Error with entering data of subscriber')

    def print_result_of_adding(self, index):
        """
        print message result of adding
        """
        self.print_message(
            index,
            'Subscriber successfully added',
            'Error with adding subscriber')

    def print_result_of_updating(self, index):
        """
        print message result of updating
        """
        self.print_message(
            index,
            'Subscriber successfully updated',
            'Error while updating subscriber')

    def print_result_of_deleting(self, index):
        """
        print message result of deleting
        """
        self.print_message(
            index,
            'Subscriber successfully deleted',
            'Error while deleting subscriber')

    def print_message(self, index, message1, message2):
        """
        print message of operation. If index > 0, print message1,
        else print message2.
        """
        if index > 0:
            print(message1)
        else:
            print(message2)
