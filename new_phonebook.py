import pymysql


class PhoneBook:
    """
    Class to work with phone numbers database.

    Contents methods:
    1. __init__(self)
    2. __del__(self)
    3. get_object()
    4. set_serializer(self, serializer)
    5. add_new_subscriber(self, subscriber, number)
    6. get_all_subscribers_with_phone_numbers(self)
    7. find_subscriber(self, key, value)
    8. update_subscriber(self, key, old_subscriber, new_value)
    9. remove_subscriber(self, key, value)
    10. save_database(self)
    11. load_database(self)
    """

    _connection = None
    _serialize = None
    _obj = None

    def __init__(self):
        self._connection = pymysql.connect(host="localhost",
                                           user="root",
                                           password="1234",
                                           db="phonebook",
                                           cursorclass=pymysql.cursors.
                                           DictCursor)

    def __del__(self):
        self._connection.close()

    @staticmethod
    def get_object():
        """
        A method that returns an object of PhoneBook class.
        """
        if PhoneBook._obj is None:
            PhoneBook._obj = PhoneBook()
        return PhoneBook._obj

    def set_serializer(self, serializer):
        """
        A method for compatibility with other modules.
        :param serializer: an object of Serializer class from serialize.py.
        :returns nothing.
        """
        pass

    def add_new_subscriber(self, subscriber, number):
        """
        Adds new record to database.
        :param subscriber: a string - subscriber's name.
        :param number: a string - subscriber's number.
        :returns a number of records in the database after adding a new one.
        """
        query = "insert into phonebook (subscriber, phone) values (%s, %s)"
        with self._connection.cursor() as cursor:
            cursor.execute(query, (subscriber, number))
            self._connection.commit()
            cursor.execute("select count(*) from phonebook")
            return cursor.fetchone()["count(*)"]

    def get_all_subscribers_with_phone_numbers(self):
        """
        Gets all subscribers from the database.
        :returns a list of dictionaries with 'subscriber' and 'phone' keys.
        """
        query = "select subscriber, phone from phonebook"
        with self._connection.cursor() as cursor:
            cursor.execute(query)
            return cursor.fetchall()

    def find_subscriber(self, key, value):
        """
        Searches for a subscriber in the database.
        :param key: "subscriber" or "phone".
        :param value: a string - subscriber's name or phone number.
        :returns a first found subscriber - a dictionary with 'subscriber'
        and 'phone' keys.
        """
        query = "select subscriber, phone from phonebook where "\
                + key + " = %s"
        with self._connection.cursor() as cursor:
            cursor.execute(query, value)
            return cursor.fetchone()

    def update_subscriber(self, key, old_subscriber, new_value):
        """
        Edits a subscriber in the database.
        :param key: "subscriber" or "phone".
        :param old_subscriber: dictionary with 'subscriber' and 'phone' keys.
        :param new_value: a string - new subscriber's name or phone number.
        :returns a number of records in the database in case of success, or
        -1 otherwise.
        """
        query = "update phonebook set " + key + " = %s where " + key + " = %s"
        with self._connection.cursor() as cursor:
            cursor.execute(query, (new_value, old_subscriber[key]))
            self._connection.commit()
            if self._connection.affected_rows() == 0:
                return -1
            cursor.execute("select count(*) from phonebook")
            return cursor.fetchone()["count(*)"]

    def remove_subscriber(self, key, value):
        """
        Removes a record from the database (a first found by the key).
        :param key: "subscriber" or "phone".
        :param value: a string - subscriber's name or phone number.
        :returns True in case of success, or False otherwise.
        """
        query = "delete from phonebook where " + key + " = %s"
        self._connection.cursor().execute(query, value)
        self._connection.commit()
        if self._connection.affected_rows() > 0:
            return True
        return False

    def save_database(self):
        """
        A method for compatibility with other modules.
        :returns nothing.
        """
        pass

    def load_database(self):
        """
        A method for compatibility with other modules.
        :returns nothing.
        """
        pass
