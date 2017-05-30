class PhoneBook(object):
    """
    database for subscribers and phone numbers. Realize pattern singleton
    """
    _phonebook = []

    _obj = None
    _serialize = None

    def set_serializer(self, serializer):
        """
        set object of class Serialize
        """
        self._serialize = serializer

    @staticmethod
    def get_object():
        """
        create object of PhoneBook and place it in phonebook.
        Return phonebook. Realize Pattern Singleton for database
        """
        if PhoneBook._obj is None:
            PhoneBook._obj = PhoneBook()
        return PhoneBook._obj

    def add_new_subscriber(self, subscriber, number):
        """
        save new subscriber in storage
        """
        self._phonebook.append({'subscriber': subscriber, 'phone': number})
        return len(self._phonebook)

    def get_all_subscribers_with_phone_numbers(self):
        """
        return all subscribers ond their phone numbers from DB
        """
        return self._phonebook

    def find_subscriber(self, key, value):
        """
        find subscriber by name or phone number
        """
        sub = [sub for sub in self._phonebook if sub.get(key) == value]
        return None if not sub else sub[0]

    def update_subscriber(self, key, old_subscriber, new_value):
        """
        update subscriber in DB
        """
        if not self.remove_subscriber(key, old_subscriber[key]):
            return -1
        if key == 'subscriber':
            return self.add_new_subscriber(old_subscriber[key], new_value)
        return self.add_new_subscriber(new_value, old_subscriber[key])

    def remove_subscriber(self, key, value):
        """
        remove subscriber from DB by phone number or subscriber's name
        """
        sub = self.find_subscriber(key, value)
        if sub is None:
            return False
        self._phonebook = [i for i in self._phonebook if i != sub]
        return True

    def save_database(self):
        """
        serialize database with selected serializer
        """
        self._serialize.save('phonebook', self._phonebook)

    def load_database(self):
        """
        deserialize database with selected serializer, place it in _phonebook
        """
        self._phonebook = self._serialize.load('phonebook')
