# -*- coding: utf-8 -*-
import re
import email

TYPE_HARD_FAIL = 'Permanent Failure'
TYPE_SOFT_FAIL = 'Persistent Transient Failure'
TYPE_SUCCESS = 'Success'
INLINE_MESSAGE_BEGIN_DELIMITERS = [
    'Original message',
    'Below this line is a copy of the message.',
    'Message header follows',
]
INLINE_MESSAGE_BEGIN_DELIMITERS_PATTERNS = [re.compile('^[-\s]*{}[\s-]*$'.format(d)) for d in INLINE_MESSAGE_BEGIN_DELIMITERS]
INLINE_MESSAGE_END_DELIMITER_PATTERN = re.compile('^[-\s]*End of message[\s-]*$')


class BounceEmail:
    def __init__(self, email_str):
        self.email = email.message_from_string(email_str)
        self.bounced = False
        self.diagnostic_code = None
        self.error_status = None

    def is_bounced(self):
        self.bounced = self.check_if_bounce()
        return self.bounced

    def diagnostic_code(self):
        # TODO
        return self.diagnostic_code

    def error_status(self):
        # TODO
        return self.error_status

    def check_if_bounce(self):
        patterns = [
            re.compile('(returned|undelivered) mail|mail delivery( failed)?|(delivery )(status notification|failure)|failure notice|undeliver(able|ed)( mail)?|return(ing message|ed) to sender', re.IGNORECASE),
            re.compile('auto.*reply|vacation|vocation|(out|away).*office|on holiday|abwesenheits|autorespond|Automatische|eingangsbestätigung', re.IGNORECASE),
            re.compile('^(MAILER-DAEMON|POSTMASTER)\@', re.IGNORECASE),
        ]
        for pattern in patterns:
            match = pattern.match(self.email.get('Subject', ''))
            if match:
                return True
        from_patterns = [
            re.compile('^(MAILER-DAEMON|POSTMASTER)\@', re.IGNORECASE),
        ]
        for pattern in from_patterns:
            match = pattern.match(self.email.get('From', ''))
            if match:
                return True
        return False
