import os
import unittest

from bounce_email import bounce_email
from . import constants


BASE_DIR = os.path.join(os.path.dirname(__file__))
BOUNCES_DIR = os.path.join(BASE_DIR, 'bounces')
NON_BOUNCES_DIR = os.path.join(BASE_DIR, 'non_bounces')
FIXTURES = os.path.join(BASE_DIR, 'fixtures')


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

    def test_all_bounces(self):
        files = os.listdir(BOUNCES_DIR)
        for f in files:
            path = os.path.join(BOUNCES_DIR, f)
            with open(path, 'r') as ff:
                email_str = ff.read()
                bounce = bounce_email.BounceEmail(email_str)
                self.assertNotEqual(bounce, None)
                self.assertEqual(bounce.is_bounced(), True)

    def test_all_non_bounces(self):
        files = os.listdir(NON_BOUNCES_DIR)
        for f in files:
            path = os.path.join(NON_BOUNCES_DIR, f)
            print path
            with open(path, 'r') as ff:
                email_str = ff.read()
                bounce = bounce_email.BounceEmail(email_str)
                self.assertNotEqual(bounce, None)
                self.assertEqual(bounce.is_bounced(), False)

    def test_does_not_fail_if_subject_is_none(self):
        no_subject = os.path.join(FIXTURES, 'no_subject.txt')
        with open(no_subject, 'r') as f:
            email_str = f.read()
            bounce = bounce_email.BounceEmail(email_str)
            self.assertNotEqual(bounce, None)
            self.assertEqual(bounce.is_bounced(), False)
