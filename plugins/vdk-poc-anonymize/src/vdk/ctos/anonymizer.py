import hashlib
from typing import Any


class Anonymizer:

    @staticmethod
    def anonymize(value: Any):
        return hashlib.sha256(f"{value}".encode('utf-8')).hexdigest()
