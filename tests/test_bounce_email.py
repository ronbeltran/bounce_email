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

    def test_bounce_type_hard_fail(self):
        path = os.path.join(BOUNCES_DIR, 'tt_bounce_01.txt')
        bounce = self._test_bounce(path)
        self.assertEqual(bounce.code, '5.1.2', 'Bounce code should be 5.1.2')
        self.assertEqual(bounce_email.TYPE_HARD_FAIL, bounce.bounce_type)

    def test_unrouteable_mail_domain(self):
        path = os.path.join(BOUNCES_DIR, 'tt_bounce_01.txt')
        bounce = self._test_bounce(path)
        self.assertEqual(bounce.code, '5.1.2', 'Bounce code should be 5.1.2')

        path = os.path.join(BOUNCES_DIR, 'tt_bounce_02.txt')
        bounce = self._test_bounce(path)
        self.assertEqual(bounce.code, '5.1.2', 'Bounce code should be 5.1.2')

    def test_set_5_0_status(self):
        path = os.path.join(BOUNCES_DIR, 'tt_bounce_03.txt')
        bounce = self._test_bounce(path)
        self.assertEqual(bounce.code, '5.0.0', 'Bounce code should be 5.0.0')

        path = os.path.join(BOUNCES_DIR, 'tt_bounce_04.txt')
        bounce = self._test_bounce(path)
        self.assertEqual(bounce.code, '5.0.0', 'Bounce code should be 5.0.0')

        path = os.path.join(BOUNCES_DIR, 'tt_bounce_05.txt')
        bounce = self._test_bounce(path)
        self.assertEqual(bounce.code, '5.0.0', 'Bounce code should be 5.0.0')

    def test_rota_dnsbl(self):
        path = os.path.join(BOUNCES_DIR, 'tt_bounce_06.txt')
        bounce = self._test_bounce(path)
        self.assertEqual(bounce.code, '5.7.1', 'Bounce code should be 5.7.1')

    def test_user_unknown(self):
        path = os.path.join(BOUNCES_DIR, 'tt_bounce_07.txt')
        bounce = self._test_bounce(path)
        self.assertEqual(bounce.code, '5.0.0', 'Bounce code should be 5.0.0')

    def test_permanent_failure(self):
        path = os.path.join(BOUNCES_DIR, 'tt_bounce_08.txt')
        bounce = self._test_bounce(path)
        # self.assertEqual(bounce.code, '5.3.2', 'Bounce code should be 5.3.2')  # fixme: 5.0.0

        path = os.path.join(BOUNCES_DIR, 'tt_bounce_09.txt')
        bounce = self._test_bounce(path)
        # self.assertEqual(bounce.code, '5.3.2', 'Bounce code should be 5.3.2')

    def test_bounce_type_soft_fail(self):
        path = os.path.join(BOUNCES_DIR, 'tt_bounce_10.txt')
        bounce = self._test_bounce(path)
        self.assertEqual(bounce.code, '4.0.0', 'Bounce code should be 4.0.0')
        self.assertEqual(bounce_email.TYPE_SOFT_FAIL, bounce.bounce_type)

    def test_malformed_bounce(self):
        path = os.path.join(BOUNCES_DIR, 'malformed_bounce_01.txt')
        bounce = self._test_bounce(path)
        self.assertEqual(bounce.code, '5.1.1', 'Bounce code should be 5.1.1')

    def test_unknown_code(self):
        path = os.path.join(BOUNCES_DIR, 'unknown_code_bounce_01.txt')
        bounce = self._test_bounce(path)
        self.assertEqual(bounce.is_bounced, True)
        self.assertEqual(bounce.code, 'unknown', 'Bounce code should be unknown')
        self.assertEqual(bounce_email.TYPE_HARD_FAIL, bounce.bounce_type)  # fixme: TYPE_HARD_FAIL
        self.assertEqual(bounce.reason, 'unknown', 'Bounce reason should be unknown')

    # def test_all_bounces(self):
    #     for f in os.listdir(BOUNCES_DIR):
    #         bounce = self._test_bounce(f)
    #         self.assertIsNotNone(bounce)
    #         self.assertEqual(bounce.is_bounced, True)

    def test_all_non_bounces(self):
        for f in os.listdir(NON_BOUNCES_DIR):
            bounce = self._test_non_bounce(f)
            self.assertIsNotNone(bounce)
            self.assertEqual(bounce.is_bounced, False)

    def test_does_not_fail_if_subject_is_none(self):
        path = os.path.join(FIXTURES_DIR, 'no_subject.txt')
        bounce = self._test_fixture_bounce(path)
        self.assertIsNotNone(bounce)
        self.assertEqual(bounce.is_bounced, False)

    def test_mail_methods_fallback(self):
        path = os.path.join(BOUNCES_DIR, 'tt_bounce_10.txt')
        bounce = self._test_bounce(path)
        self.assertIsNotNone(bounce)
        # self.assertIsNotNone(bounce.email.body)
        # self.assertIsNotNone(bounce.email.date)

    def test_multipart(self):
        path = os.path.join(BOUNCES_DIR, 'tt_bounce_24.txt')
        bounce = self._test_bounce(path)
        self.assertIsNotNone(bounce)
        self.assertEqual(bounce_email.TYPE_HARD_FAIL, bounce.bounce_type)
        # self.assertEqual(bounce.is_bounced, True)
        # self.assertNotEqual(bounce.original_mail, None)

    # def test_original_message_with_multipart_mails(self):
    #     multipart_mails = ['05', '07', '10', '11', '13', '15', '16', '23', '24']
    #     for m in multipart_mails:
    #         path = os.path.join(BOUNCES_DIR, 'tt_bounce_{}.txt'.format(m))
    #         bounce = self._test_bounce(path)
    #         self.assertIsNotNone(bounce.original_mail)
    #         self.assertIsNotNone(bounce.original_mail.message_id)
    #         self.assertIsNotNone(bounce.original_mail.to)
    #         self.assertIsNotNone(bounce.original_mail._from)

    def test_original_message_with_multipart_mails_without_to_field(self):
        multipart_mails = ['03', '04']
        for m in multipart_mails:
            path = os.path.join(BOUNCES_DIR, 'tt_bounce_{}.txt'.format(m))
            bounce = self._test_bounce(path)
            # self.assertIsNotNone(bounce.original_mail)
            # self.assertIsNotNone(bounce.original_mail['Message-ID'])
            # self.assertEqual([], bounce.original_mail['To'])
            # self.assertIsNotNone(bounce.original_mail['From'])

    def test_original_message_without_inline_original_message(self):
        path = os.path.join(BOUNCES_DIR, 'tt_bounce_01.txt')
        bounce = self._test_bounce(path)
        self.assertIsNotNone(bounce)
        self.assertIsNone(bounce.original_mail)

    def test_original_message_with_inline_original_message(self):
        multipart_mails = ['06', '08', '09', '12_soft', '14', '17', '18', '19', '20', '21', '22', '25']
        for m in multipart_mails:
            path = os.path.join(BOUNCES_DIR, 'tt_bounce_{}.txt'.format(m))
            bounce = self._test_bounce(path)
            self.assertIsNotNone(bounce.original_mail)
            self.assertIsNotNone(bounce.original_mail['Message-ID'])
            self.assertIsNotNone(bounce.original_mail['To'])
            self.assertIsNotNone(bounce.original_mail['From'])

    def test_original_message_with_subject(self):
        path = os.path.join(BOUNCES_DIR, 'tt_bounce_04.txt')
        bounce = self._test_bounce(path)
        self.assertIsNotNone(bounce)
        # self.assertIsNotNone(bounce.original_mail)
        # self.assertIsNotNone(bounce.original_mail['Subject'])

    def test_original_message_with_bounced_gmail(self):
        path = os.path.join(BOUNCES_DIR, 'undeliverable_gmail.txt')
        bounce = self._test_bounce(path)
        self.assertIsNotNone(bounce)
        self.assertIsNotNone(bounce.original_mail)
        self.assertIsNotNone(bounce.original_mail['Message-ID'])
        self.assertIsNotNone(bounce.original_mail['To'])
        self.assertIsNotNone(bounce.original_mail['From'])
