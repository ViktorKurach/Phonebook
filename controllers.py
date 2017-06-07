from sys import exit
from configurations import Config
# from phonebook import PhoneBook
from new_phonebook import PhoneBook
from views import MessagePrinter, Subscriber
from serialize import Serialize


class Controller:
    subscriber_view = Subscriber()
    message_printer = MessagePrinter()
    database = PhoneBook.get_object()

    def __init__(self):
        config = Config()
        serializer = Serialize(config.get_setting('Serialize', 'serialize'))
        self.database.set_serializer(serializer)
        self.database.load_database()

    def add_new_subscriber(self):
        sub, num = \
            self.subscriber_view.enter_new_subscriber_and_phone_number()
        if self.database.find_subscriber('subscriber', sub) or \
           self.database.find_subscriber('phone', num):
            self.message_printer.print_result_of_adding(-1)
            return
        self.message_printer.print_result_of_adding(
            self.database.add_new_subscriber(sub, num))

    def get_all_subscribers(self):
        self.subscriber_view.out_subscribers_and_their_phone_numbers(
            self.database.get_all_subscribers_with_phone_numbers())

    def find_subscriber(self, key):
        value = self.subscriber_view.enter_subscribers_data(key)
        self.subscriber_view.out_subscribers_and_their_phone_numbers([
            self.database.find_subscriber(key, value)])

    def update_subscriber(self, key):
        sub = self.database.find_subscriber(
            key, self.subscriber_view.enter_subscribers_data(key))
        res = -1
        if sub is not None:
            val = self.subscriber_view.enter_subscribers_data(key)
            res = self.database.update_subscriber(key, sub, val)
            self.subscriber_view.out_subscribers_and_their_phone_numbers([
                self.database.find_subscriber(key, val)])
        self.message_printer.print_result_of_updating(res)

    def delete_subscriber(self):
        value = self.subscriber_view.enter_subscribers_data('subscriber')
        self.message_printer.print_result_of_deleting(
            self.database.remove_subscriber('subscriber', value))
        self.subscriber_view.out_subscribers_and_their_phone_numbers(
            self.database.get_all_subscribers_with_phone_numbers())

    def error_operation(self):
        self.message_printer.print_message_of_error_entering_data()

    def save_and_exit(self):
        self.database.save_database()
        exit()
