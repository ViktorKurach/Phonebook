from sys import exit
from configurations import Config
from phonebook import PhoneBook
from views import Printer, Subscriber
from serialize import Serialize


class Controller:
    subscriber = Subscriber()
    printer = Printer()

    def __init__(self):
        config = Config()
        serializer = Serialize(config.get_setting('Serialize', 'serialize'))
        PhoneBook.get_object().set_serializer(serializer)
        PhoneBook.get_object().load_database()

    def add_new_subscriber(self):
        sub, num = self.subscriber.enter_new_subscriber_and_phone_number()
        found = PhoneBook.get_object().find_subscriber('subscriber', sub)
        if found is not None:
            found = PhoneBook.get_object().find_subscriber('phone', num)
            if found is not None:
                self.printer.print_result_of_adding(-1)
                return
        self.printer.print_result_of_adding(
            PhoneBook.get_object().add_new_subscriber(sub, num))

    def get_all_subscribers(self):
        self.subscriber.out_subscribers_and_their_phone_numbers(
            PhoneBook.get_object().get_all_subscribers_with_phone_numbers())

    def find_subscriber(self, key):
        value = self.subscriber.enter_subscribers_data(key)
        self.subscriber.out_subscribers_and_their_phone_numbers([
            PhoneBook.get_object().find_subscriber(key, value)])

    def update_subscriber(self, key):
        sub = PhoneBook.get_object().find_subscriber(
            key, self.subscriber.enter_subscribers_data(key))
        res = -1
        if sub is not None:
            inv_key = 'subscriber' if key == 'phone' else 'phone'
            val = self.subscriber.enter_subscribers_data(key)
            res = PhoneBook.get_object().update_subscriber(inv_key, sub, val)
            self.subscriber.out_subscribers_and_their_phone_numbers([
                PhoneBook.get_object().find_subscriber(key, val)])
        self.printer.print_result_of_updating(res)

    def delete_subscriber(self):
        value = self.subscriber.enter_subscribers_data('subscriber')
        self.printer.print_result_of_deleting(
            PhoneBook.get_object().remove_subscriber('subscriber', value))
        self.subscriber.out_subscribers_and_their_phone_numbers(
            PhoneBook.get_object().get_all_subscribers_with_phone_numbers())

    def save_and_exit(self):
        PhoneBook.get_object().save_database()
        exit()
