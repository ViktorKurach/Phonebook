import json
import pickle
import yaml
import sys


class Serialize:
    """
    Class for selecting serialization type
    """
    _serializer = None

    def __init__(self, cls):
        """
        constructor, set serializer object
        """
        self._serializer = sys.modules['serialize'].__dict__[cls]

    def save(self, path_to_file, lst):
        """
        call selected save
        """
        return self._serializer.save(path_to_file, lst)

    def load(self, path_to_file):
        """
        call selected load
        """
        return self._serializer.load(path_to_file)


class AbstractSerializer:
    """
    Abstract class for serialize classes.
    Contains base logic of serialization.
    """
    @staticmethod
    def base_load(path_to_file, method, ext, mode):
        """
        base load method. Load data from :file with extension :ext by :method.
        Return a list with data
        """
        path_to_file = './dump/' + path_to_file + ext
        try:
            with open(path_to_file, mode) as f:
                res = method(f)
                return [] if not isinstance(res, list) else res
        except EOFError:
            return []

    @staticmethod
    def base_save(path_to_file, lst, method, ext, mode):
        """
        base save method. Serialize data in file by :path_to_file with
        extension :ext by method :method
        """
        path_to_file = './dump/' + path_to_file + ext
        with open(path_to_file, mode) as f:
            method(lst, f)


class PickleSerialize(AbstractSerializer):
    """
    Pickle serializer class
    """
    @staticmethod
    def load(path_to_file):
        """
        call base load method with parameters
        """
        return PickleSerialize\
            .base_load('p-' + path_to_file, pickle.load, '.pickle', 'rb')

    @staticmethod
    def save(path_to_file, lst):
        """
        call base save method with parameters
        """
        PickleSerialize\
            .base_save('p-' + path_to_file, lst, pickle.dump, '.pickle', 'wb')


class JsonSerialize(AbstractSerializer):
    """
    Json serializer class
    """
    @staticmethod
    def load(path_to_file):
        """
        call base load method with parameters
        """
        try:
            return JsonSerialize \
                .base_load('j-' + path_to_file, json.load, '.json', 'r')
        except:
            return []

    @staticmethod
    def save(path_to_file, lst):
        """
        call base save method with parameters
        """
        JsonSerialize\
            .base_save('j-' + path_to_file, lst, json.dump, '.json', 'w')


class YamlSerialize(AbstractSerializer):
    """
    Yaml serializer class
    """
    @staticmethod
    def load(path_to_file):
        """
        call base load method with parameters
        """
        return YamlSerialize\
            .base_load('y-' + path_to_file, yaml.load, '.yaml', 'r')

    @staticmethod
    def save(path_to_file, lst):
        """
        call base save method with parameters
        """
        YamlSerialize\
            .base_save('y-' + path_to_file, lst, yaml.dump, '.yaml', 'w')
