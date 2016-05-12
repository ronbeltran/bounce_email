import email


class BounceEmail:
    def __init__(self, email_str):
        self.email = self.from_string(email_str)

    @classmethod
    def from_string(cls, email_str):
        cls.email = email.message_from_string(email_str)

    @classmethod
    def from_file(cls, email_file):
        cls.email = email.message_from_file(email_file)

    def is_bounce(self):
        # TODO: Implement is_bounce logic
        return False
