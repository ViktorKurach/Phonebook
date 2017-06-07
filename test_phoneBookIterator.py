from unittest import TestCase
from unittest.mock import Mock

from generator import generator, generate

from phonebook import PhoneBookIterator, PhoneBook


@generator
class TestPhoneBookIterator(TestCase):

    @generate(PhoneBook.get_object())
    def test__init__(self, obj):
        obj._phonebook = []
        obj.add_new_subscriber('subscriber1', 'phone1')
        obj.add_new_subscriber('subscriber2', 'phone2')
        obj.add_new_subscriber('subscriber3', 'phone3')
        it = PhoneBookIterator(obj)
        self.assertEqual(it.last_index, 3)
        self.assertListEqual(
            obj.get_all_subscribers_with_phone_numbers(),
            it.phonebook)

    @generate(PhoneBook.get_object())
    def test__next__(self, obj):
        obj._phonebook = []
        obj.add_new_subscriber('subscriber1', 'phone1')
        mock = Mock()
        mock.next.return_value = \
            {'subscriber': 'subscriber1',
             'phone': 'phone1'}
        it = PhoneBookIterator(obj)
        self.assertEqual(it.__next__(), mock.next())
        self.assertRaises(StopIteration, it.__next__)
