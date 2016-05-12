import unittest

from bounce_email import bounce_email
from . import constants


class BounceEmailTest(unittest.TestCase):

    def setUp(self):
        self.bounce1 = constants.BOUNCE_EMAIL1
        self.bounce2 = constants.BOUNCE_EMAIL2
        self.normal_email = constants.NORMAL_EMAIL1

    def test_init(self):
        bounce = bounce_email.BounceEmail(self.bounce1)
        self.assertEqual(bounce.is_bounce(), False)
