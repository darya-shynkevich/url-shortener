import string
import random


class ShortenerService:

    ALLOWED_CHARS = string.ascii_letters + string.digits

    def __init__(self, internal_domain: str = "http://localhost:8000/"):
        self.internal_domain = internal_domain

    def get_short_url(self, short_key: str) -> str:
        return f"{self.internal_domain}{short_key}"

    def shorten_random(self) -> str:
        key_len = random.randint(1, 100)
        return "".join(random.choices(self.ALLOWED_CHARS, k=key_len))
