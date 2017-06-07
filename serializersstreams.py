import json
from io import StringIO
import yaml


class SerializeToStream:
    serializer = None

    class Stream(StringIO):
        def read(self):
            return super().getvalue()

    def __init__(self, serializer):
        self.serializer = serializer

    def serializeToStream(self, data):
        stream = self.Stream()
        self.serializer.dump(data, stream)
        return stream


def serializeToJsonStream(data):
    return SerializeToStream(json).serializeToStream(data)


def serializeToYamlStream(data):
    return SerializeToStream(yaml).serializeToStream(data)
