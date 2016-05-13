import os
import unittest

from bounce_email import bounce_email

BASE_DIR = os.path.join(os.path.dirname(__file__))
BOUNCES_DIR = os.path.join(BASE_DIR, 'bounces')
NON_BOUNCES_DIR = os.path.join(BASE_DIR, 'non_bounces')
FIXTURES_DIR = os.path.join(BASE_DIR, 'fixtures')


class BounceEmailTest(unittest.TestCase):

    def _read_file(self, path):
        with open(path, 'r') as ff:
            return ff.read()

    def _test_bounce(self, filename):
        path = os.path.join(BOUNCES_DIR, filename)
        email_str = self._read_file(path)
        return bounce_email.BounceEmail(email_str)

    def _test_non_bounce(self, filename):
        path = os.path.join(NON_BOUNCES_DIR, filename)
        email_str = self._read_file(path)
        return bounce_email.BounceEmail(email_str)

    def _test_fixture_bounce(self, filename):
        path = os.path.join(FIXTURES_DIR, filename)
        email_str = self._read_file(path)
        return bounce_email.BounceEmail(email_str)

    def test_all_bounces(self):
        for f in os.listdir(BOUNCES_DIR):
            bounce = self._test_bounce(f)
            self.assertNotEqual(bounce, None)
            self.assertEqual(bounce.is_bounced(), True)

    def test_all_non_bounces(self):
        for f in os.listdir(NON_BOUNCES_DIR):
            bounce = self._test_non_bounce(f)
            self.assertNotEqual(bounce, None)
            self.assertEqual(bounce.is_bounced(), False)

    def test_does_not_fail_if_subject_is_none(self):
        path = os.path.join(FIXTURES_DIR, 'no_subject.txt')
        bounce = self._test_fixture_bounce(path)
        self.assertNotEqual(bounce, None)
        self.assertEqual(bounce.is_bounced(), False)
