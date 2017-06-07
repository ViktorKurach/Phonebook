from unittest import TestCase

from generator import generator, generate

from phonebook import PhoneBook, PhoneBookIterator
from serialize import PickleSerialize
from serialize import YamlSerialize
from serialize import JsonSerialize


@generator
class TestPhoneBook(TestCase):
    @generate(
        JsonSerialize, YamlSerialize, PickleSerialize
    )
    def test_set_serializer(self, inp):
        PhoneBook.get_object().set_serializer(inp)

    @generate(
        [True, PhoneBookIterator], [False, list]
    )
    def test___iter__(self, inp):
        pb = PhoneBook.get_object()
        if (type(pb.__iter__()) == inp[1]) != inp[0]:
            self.fail()

    @generate(
        [1, 'subscriber1', 'number1']
    )
    def test_add_new_subscriber(self, inp):
        self.assertEqual(
            inp[0],
            PhoneBook.get_object().add_new_subscriber(inp[1], inp[2]))

    @generate(
        [{'subscriber': 'subscriber1', 'phone': 'number1'}]
    )
    def test_get_all_subscribers_with_phone_numbers(self, inp):
        self.assertListEqual(
            inp,
            PhoneBook.get_object().get_all_subscribers_with_phone_numbers())

    @generate(
        [{'subscriber': 'subscriber1', 'phone': 'number1'},
         'subscriber', 'subscriber1'],
        [None, 'phone', 'subscriber']
    )
    def test_find_subscriber(self, inp):
        self.assertEqual(
            inp[0],
            PhoneBook.get_object().find_subscriber(inp[1], inp[2]))

    @generate(
        [1, {'subscriber': 'subscriber1', 'phone': 'number1'},
         'subscriber', 'subscriber2'],
        [2, {'subscriber': 'subscriber1', 'phone': 'number1'},
         'phone', 'phone2'],
        [-1, {'subscriber': 'unsaved', 'phone': 'number1'},
         'subscriber', 'subscriber2']
    )
    def test_update_subscriber(self, inp):
        PhoneBook.get_object().add_new_subscriber("subscriber1", "number1")
        self.assertEqual(
            inp[0],
            PhoneBook.get_object().update_subscriber(inp[2], inp[1], inp[3]))

    @generate(
        [False, 'phone', 'unsaved'],
        [True, 'subscriber', 'subscriber1']
    )
    def test_remove_subscriber(self, inp):
        self.assertEqual(
            inp[0],
            PhoneBook.get_object().remove_subscriber(inp[1], inp[2]))

    @generate(
        [{'subscriber': 'subscriber1', 'phone': 'number1'}]
    )
    def test_load(self, inp):
        PhoneBook.get_object().set_serializer(YamlSerialize)
        PhoneBook.get_object()._phonebook = []
        PhoneBook.get_object().add_new_subscriber(
            inp[0]['subscriber'], inp[0]['phone'])
        PhoneBook.get_object().save_database()
        PhoneBook.get_object().load_database()
        self.assertListEqual(
            inp,
            PhoneBook.get_object().get_all_subscribers_with_phone_numbers())
