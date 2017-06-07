from new_phonebook import PhoneBook
import unittest


class TestDatabaseConnection(unittest.TestCase):
    db = PhoneBook()
    sub = {"subscriber": "for_test", "phone": "000000"}

    def test_1_add_new_subscriber(self):
        self.assertEqual(2, self.db.add_new_subscriber("for_test", "000000"))

    def test_2_get_all_subscribers_with_phone_numbers(self):
        res = [{"subscriber": "test", "phone": "1234"},
               {"subscriber": "for_test", "phone": "000000"}]
        self.assertEqual(res,
                         self.db.get_all_subscribers_with_phone_numbers())

    def test_3_find_subscriber(self):
        self.assertEqual(self.sub, self.db.find_subscriber("phone", "000000"))

    def test_4_update_subscriber(self):
        self.assertEqual(2, self.db.update_subscriber("phone",
                                                      self.sub, "123456"))
        self.assertEqual(-1, self.db.update_subscriber("phone",
                                                       self.sub, "123456"))

    def test_5_remove_subscriber(self):
        self.assertEqual(True, self.db.remove_subscriber("subscriber",
                                                         "for_test"))
        self.assertEqual(False, self.db.remove_subscriber("subscriber",
                                                          "for_test"))

    def test__get_object(self):
        self.assertEqual(self.db.get_object(), self.db.get_object())

    def test__set_serializer(self):
        self.assertEqual(None, self.db.set_serializer(None))

    def test_save_database(self):
        self.assertEqual(None, self.db.save_database())

    def test_load_database(self):
        self.assertEqual(None, self.db.load_database())

    def test_destructor(self):
        db = PhoneBook()
        del db
