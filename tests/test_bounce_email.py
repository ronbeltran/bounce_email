import unittest

from bounce_email import bounce_email
from . import constants


class BounceEmailTest(unittest.TestCase):

    def setUp(self):
        self.bounce1 = constants.BOUNCE_EMAIL1
        self.bounce2 = constants.BOUNCE_EMAIL2
        self.notbounce = constants.NORMAL_EMAIL1

    def test_is_bounced(self):
        bounce = bounce_email.BounceEmail(self.bounce1)
        self.assertNotEqual(bounce, None)
        self.assertEqual(bounce.is_bounced(), True)

    def test_is_bounced2(self):
        bounce = bounce_email.BounceEmail(self.bounce2)
        self.assertNotEqual(bounce, None)
        self.assertEqual(bounce.is_bounced(), True)

    def test_not_bounced(self):
        bounce = bounce_email.BounceEmail(self.notbounce)
        self.assertNotEqual(bounce, None)
        self.assertEqual(bounce.is_bounced(), False)
