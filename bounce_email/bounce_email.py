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
INLINE_MESSAGE_BEGIN_DELIMITERS_PATTERNS = [
    '[-\s]*{}[\s-]*'.format(d) for d in INLINE_MESSAGE_BEGIN_DELIMITERS]
INLINE_MESSAGE_END_DELIMITER_PATTERN = '[-\s]*End of message[\s-]*'


class BounceEmail:

    def __init__(self, email_str):
        self.email = email.message_from_string(email_str)
        self.error_status = self.get_code()
        self.diagnostic_code = self.get_reason_from_status_code()
        self.bounced = self.check_if_bounce() or self.error_status != 'unknown' or self.diagnostic_code != 'unknown'
        self.bounce_type = self.get_type_from_status_code()
        self.original_mail = self.get_original_mail()

    @property
    def is_bounced(self):
        return self.bounced

    @property
    def reason(self):
        return self.diagnostic_code

    @property
    def code(self):
        return self.error_status

    @property
    def bounce_type(self):
        return self.bounce_type

    @property
    def original_email(self):
        return self.original_mail

    def check_if_bounce(self):
        subject_patterns = [
            re.compile('(returned|undelivered) mail|mail delivery( failed)?|(delivery )(status notification|failure)|failure notice|undeliver(able|ed)( mail)?|return(ing message|ed) to sender', re.IGNORECASE),
            re.compile('auto.*reply|vacation|vocation|(out|away).*office|on holiday|abwesenheits|autorespond|Automatische|eingangsbestätigung', re.IGNORECASE),
            re.compile('^(MAILER-DAEMON|POSTMASTER)\@', re.IGNORECASE),
        ]
        for pattern in subject_patterns:
            match = pattern.search(self.email.get('Subject', ''))
            if match:
                return True
        from_patterns = [
            re.compile('^(MAILER-DAEMON|POSTMASTER)', re.IGNORECASE),
        ]
        for pattern in from_patterns:
            match = pattern.search(self.email.get('From', ''))
            if match:
                return True
        return False

    def get_code(self):
        subject = self.email.get('Subject', '')

        pattern_mapping = {
            '97': 'delayed',
            '98': '(unzulässiger|unerlaubter) anhang',
            '99': 'auto.*reply|vacation|vocation|(out|away).*office|on holiday|abwesenheits|autorespond|Automatische|eingangsbestätigung',
        }

        for k, v in pattern_mapping.iteritems():
            pattern = re.compile(v, re.IGNORECASE)
            match = pattern.search(subject)
            if match:
                return k

        if self.email.is_multipart():
            pattern = re.compile('(Status:.|550 |#)([245]\.[0-9]{1,3}\.[0-9]{1,3})')
            for index, part in enumerate(self.email.get_payload()):
                # print '{}: {}'.format(index, part.get_content_type())
                if 'delivery-status' in part.get_content_type():   # message/delivery-status
                    match = pattern.search(part.as_string())
                    if match:
                        # check if starts with Status: XXX, or 550 XXX
                        code = match.group().strip()
                        if len(code.split()) > 1:
                            code = code.split()[1]
                        # check if starts with `#` e.g. #1234
                        if code.startswith('#'):
                            code = code[1:]
                        return code

        code = self.get_status_from_text(self.email.as_string())

        if code is None:
            code = 'unknown'
        return code

    def get_status_from_text(self, email_str):
        def search(p):
            pattern = re.compile(p, re.IGNORECASE)
            return pattern.search(email_str)

        # check for 5.2.2
        status_522 = ['mailbox is full|Mailbox quota (usage|disk) exceeded|quota exceeded|Over quota|User mailbox exceeds allowed size|Message rejected\. Not enough storage space|user has exhausted allowed storage space|too many messages on the server|mailbox is over quota|mailbox exceeds allowed size',
                      'This is a permanent error']
        matches = map(search, status_522)
        if None not in matches:
            return '5.2.2'

        # check for 4.2.2
        status_422 = status_522[0]
        match = search(status_422)
        if match:
            return '4.2.2'

        # check for 5.3.2 status
        status_532 = ['Technical details of permanent failure|Too many bad recipients',
                      'The recipient server did not accept our requests to connect']
        status_532_b = ['Connection was dropped by remote host',
                        'Could not initiate SMTP conversation']
        matches = map(search, status_532)
        if None not in matches:
            return '5.3.2'

        matches = map(search, status_532_b)
        matches = [m for m in matches if m is not None]
        if len(matches) >= 1:
            return '5.3.2'

        status_432 = ['Technical details of temporary failure',
                      'The recipient server did not accept our requests to connect']
        status_432_b = ['Connection was dropped by remote host',
                        'Could not initiate SMTP conversation']
        matches = map(search, status_432)
        if None not in matches:
            return '4.3.2'

        matches = map(search, status_432_b)
        matches = [m for m in matches if m is not None]
        if len(matches) >= 1:
            return '4.3.2'

        status_patterns = {
            '5.1.0': 'Address rejected',
            '4.1.2': "I couldn't find any host by that name",
            '4.2.0': 'not yet been delivered',
            '5.2.0': 'mailbox unavailable|No such mailbox',
            '5.4.4': 'Unrouteable address',
            '4.4.7': 'retry timeout exceeded',
            '5.2.0': 'The account or domain may not exist, they may be blacklisted, or missing the proper dns entries.',
            '5.5.4': '554 TRANSACTION FAILED',
            '4.4.1': "Status: 4.4.1|delivery temporarily suspended|wasn't able to establish an SMTP connection",
            '5.5.0': '550 OU\-002|Mail rejected by Windows Live Hotmail for policy reasons',
            '5.1.2': 'PERM_FAILURE: DNS Error: Domain name not found',
            '4.2.0': 'Delivery attempts will continue to be made for',
            '5.5.4': '554 delivery error:',
            '5.1.1': '550-5.1.1|This Gmail user does not exist',
            '5.7.1': '5.7.1 Your message.*?was blocked by ROTA DNSBL',
            '5.0.0': 'Delivery to the following recipient failed permanently',
            '5.2.3': 'account closed|account has been disabled or discontinued|mailbox not found|prohibited by administrator|access denied|account does not exist',
            '5.1.1': 'no such (address|user)|Recipient address rejected|User unknown|does not like recipient|The recipient was unavailable to take delivery of the message|Sorry, no mailbox here by that name|invalid address|unknown user|unknown local part|user not found|invalid recipient|failed after I sent the message|did not reach the following recipient|nicht zugestellt werden',
            '5.1.2': "unrouteable mail domain|Esta casilla ha expirado por falta de uso|I couldn't find any host named",
        }

        for k, v in status_patterns.iteritems():
            match = search(v)
            if match:
                return k


    def get_reason_from_status_code(self):
        if self.error_status is None:
            return 'unknown'
        reasons = {
            '00':  "Other undefined status is the only undefined error code. It should be used for all errors for which only the class of the error is known.",
            '10':  "Something about the address specified in the message caused this DSN.",
            '11':  "The mailbox specified in the address does not exist.  For Internet mail names, this means the address portion to the left of the '@' sign is invalid.  This code is only useful for permanent failures.",
            '12':  "The destination system specified in the address does not exist or is incapable of accepting mail.  For Internet mail names, this means the address portion to the right of the @ is invalid for mail.  This codes is only useful for permanent failures.",
            '13':  "The destination address was syntactically invalid.  This can apply to any field in the address.  This code is only useful for permanent failures.",
            '14':  "The mailbox address as specified matches one or more recipients on the destination system.  This may result if a heuristic address mapping algorithm is used to map the specified address to a local mailbox name.",
            '15':  "This mailbox address as specified was valid.  This status code should be used for positive delivery reports.",
            '16':  "The mailbox address provided was at one time valid, but mail is no longer being accepted for that address.  This code is only useful for permanent failures.",
            '17':  "The sender's address was syntactically invalid.  This can apply to any field in the address.",
            '18':  "The sender's system specified in the address does not exist or is incapable of accepting return mail.  For domain names, this means the address portion to the right of the @ is invalid for mail. ",
            '20':  "The mailbox exists, but something about the destination mailbox has caused the sending of this DSN.",
            '21':  "The mailbox exists, but is not accepting messages.  This may be a permanent error if the mailbox will never be re-enabled or a transient error if the mailbox is only temporarily disabled.",
            '22':  "The mailbox is full because the user has exceeded a per-mailbox administrative quota or physical capacity.  The general semantics implies that the recipient can delete messages to make more space available.  This code should be used as a persistent transient failure.",
            '23':  "A per-mailbox administrative message length limit has been exceeded.  This status code should be used when the per-mailbox message length limit is less than the general system limit.  This code should be used as a permanent failure.",
            '24':  "The mailbox is a mailing list address and the mailing list was unable to be expanded.  This code may represent a permanent failure or a persistent transient failure. ",
            '30':  "The destination system exists and normally accepts mail, but something about the system has caused the generation of this DSN.",
            '31':  "Mail system storage has been exceeded.  The general semantics imply that the individual recipient may not be able to delete material to make room for additional messages.  This is useful only as a persistent transient error.",
            '32':  "The host on which the mailbox is resident is not accepting messages.  Examples of such conditions include an immanent shutdown, excessive load, or system maintenance.  This is useful for both permanent and permanent transient errors. ",
            '33':  "Selected features specified for the message are not supported by the destination system.  This can occur in gateways when features from one domain cannot be mapped onto the supported feature in another.",
            '34':  "The message is larger than per-message size limit.  This limit may either be for physical or administrative reasons. This is useful only as a permanent error.",
            '35':  "The system is not configured in a manner which will permit it to accept this message.",
            '40':  "Something went wrong with the networking, but it is not clear what the problem is, or the problem cannot be well expressed with any of the other provided detail codes.",
            '41':  "The outbound connection attempt was not answered, either because the remote system was busy, or otherwise unable to take a call.  This is useful only as a persistent transient error.",
            '42':  "The outbound connection was established, but was otherwise unable to complete the message transaction, either because of time-out, or inadequate connection quality. This is useful only as a persistent transient error.",
            '43':  "The network system was unable to forward the message, because a directory server was unavailable.  This is useful only as a persistent transient error. The inability to connect to an Internet DNS server is one example of the directory server failure error. ",
            '44':  "The mail system was unable to determine the next hop for the message because the necessary routing information was unavailable from the directory server. This is useful for both permanent and persistent transient errors.  A DNS lookup returning only an SOA (Start of Administration) record for a domain name is one example of the unable to route error.",
            '45':  "The mail system was unable to deliver the message because the mail system was congested. This is useful only as a persistent transient error.",
            '46':  "A routing loop caused the message to be forwarded too many times, either because of incorrect routing tables or a user forwarding loop. This is useful only as a persistent transient error.",
            '47':  "The message was considered too old by the rejecting system, either because it remained on that host too long or because the time-to-live value specified by the sender of the message was exceeded. If possible, the code for the actual problem found when delivery was attempted should be returned rather than this code.  This is useful only as a persistent transient error.",
            '50':  "Something was wrong with the protocol necessary to deliver the message to the next hop and the problem cannot be well expressed with any of the other provided detail codes.",
            '51':  "A mail transaction protocol command was issued which was either out of sequence or unsupported.  This is useful only as a permanent error.",
            '52':  "A mail transaction protocol command was issued which could not be interpreted, either because the syntax was wrong or the command is unrecognized. This is useful only as a permanent error.",
            '53':  "More recipients were specified for the message than could have been delivered by the protocol.  This error should normally result in the segmentation of the message into two, the remainder of the recipients to be delivered on a subsequent delivery attempt.  It is included in this list in the event that such segmentation is not possible.",
            '54':  "A valid mail transaction protocol command was issued with invalid arguments, either because the arguments were out of range or represented unrecognized features. This is useful only as a permanent error. ",
            '55':  "A protocol version mis-match existed which could not be automatically resolved by the communicating parties.",
            '60':  "Something about the content of a message caused it to be considered undeliverable and the problem cannot be well expressed with any of the other provided detail codes. ",
            '61':  "The media of the message is not supported by either the delivery protocol or the next system in the forwarding path. This is useful only as a permanent error.",
            '62':  "The content of the message must be converted before it can be delivered and such conversion is not permitted.  Such prohibitions may be the expression of the sender in the message itself or the policy of the sending host.",
            '63':  "The message content must be converted to be forwarded but such conversion is not possible or is not practical by a host in the forwarding path.  This condition may result when an ESMTP gateway supports 8bit transport but is not able to downgrade the message to 7 bit as required for the next hop.",
            '64':  "This is a warning sent to the sender when message delivery was successfully but when the delivery required a conversion in which some data was lost.  This may also be a permanant error if the sender has indicated that conversion with loss is prohibited for the message.",
            '65':  "A conversion was required but was unsuccessful.  This may be useful as a permanent or persistent temporary notification.",
            '70':  "Something related to security caused the message to be returned, and the problem cannot be well expressed with any of the other provided detail codes.  This status code may also be used when the condition cannot be further described because of security policies in force.",
            '71':  "The sender is not authorized to send to the destination. This can be the result of per-host or per-recipient filtering.  This memo does not discuss the merits of any such filtering, but provides a mechanism to report such. This is useful only as a permanent error.",
            '72':  "The sender is not authorized to send a message to the intended mailing list. This is useful only as a permanent error.",
            '73':  "A conversion from one secure messaging protocol to another was required for delivery and such conversion was not possible. This is useful only as a permanent error. ",
            '74':  "A message contained security features such as secure authentication which could not be supported on the delivery protocol. This is useful only as a permanent error.",
            '75':  "A transport system otherwise authorized to validate or decrypt a message in transport was unable to do so because necessary information such as key was not available or such information was invalid.",
            '76':  "A transport system otherwise authorized to validate or decrypt a message was unable to do so because the necessary algorithm was not supported. ",
            '77':  "A transport system otherwise authorized to validate a message was unable to do so because the message was corrupted or altered.  This may be useful as a permanent, transient persistent, or successful delivery code.",
            #custom codes,
            '97':  "Delayed",
            '98':  "Not allowed Attachment",
            '99':  "Vacation auto-reply",
        }

        # code = code.gsub(/\./,'')[1..2]
        return reasons.get(self.error_status, 'unknown')

    def get_type_from_status_code(self):
        if self.error_status == 'unknown' or self.error_status is None:
            return TYPE_HARD_FAIL
        pre_code = int(self.error_status[0])
        types = {
            5: TYPE_HARD_FAIL,
            4: TYPE_SOFT_FAIL,
            2: TYPE_SUCCESS,
        }
        if pre_code not in types.keys():
            return TYPE_HARD_FAIL
        return types[pre_code]

    def index_of_original_message_delimiter(self):
        for index, d in enumerate(INLINE_MESSAGE_BEGIN_DELIMITERS_PATTERNS):
            pattern = re.compile(d)
            match = pattern.search(self.email.as_string())
            if match:
                return index

    def extract_original_message_after_delimiter(self, delimeter_index):
        pattern = re.compile(INLINE_MESSAGE_BEGIN_DELIMITERS_PATTERNS[delimeter_index])
        match = pattern.search(self.email.as_string())
        if match:
            msg = self.email.as_string().split(match.group())[1]
            end_pattern = re.compile(INLINE_MESSAGE_END_DELIMITER_PATTERN)
            match = end_pattern.search(msg)
            if match:
                msg = self.email.as_string().split(match.group())[0]
            return msg.strip()

    def original_mail_body_lines(self, mail):
        lines = []
        for k, v in mail.items():
            lines.append(': '.join([k, v]))
        return lines

    def extract_field_from(self, mail, field_name):
        pattern = re.compile(field_name, re.IGNORECASE)
        lines = self.original_mail_body_lines(mail)
        for line in lines:
            match = pattern.search(line)
            if match:
                field = match.group()
                return field.split(':')[1]

    def extract_original_to_field_from_header(self):
        return self.email.get('X-Failed-Recipients')

    def extract_and_assign_fields_from(self, original):
        message_id = original.get('Message-ID')
        if message_id is None:
            message_id = self.extract_field_from(original, '^Message-ID:')
            original.add_header('Message-ID', message_id)

        from_addr = original.get('From')
        if from_addr is None:
            from_addr = self.extract_field_from(original, '^From:')
            original.add_header('From', from_addr)

        subject = original.get('Subject')
        if subject is None:
            subject = self.extract_field_from(original, '^Subject:')
            original.add_header('Subject', subject)

        to_addr = original.get('To')
        if to_addr is None:
            to_addr = self.extract_field_from(original, '^To:') or self.extract_original_to_field_from_header()
            original.add_header('To', to_addr)

        return original

    def get_original_mail(self):
        original = None

        if self.email.is_multipart():
            for i, payload in enumerate(self.email.get_payload()):
                # print '{}: {}'.format(i, payload.get_content_type())
                if 'rfc822' in payload.get_content_type():  # message/rfc822
                    original = payload
        else:
            index = self.index_of_original_message_delimiter()
            if index is not None:
                message = self.extract_original_message_after_delimiter(index)
                original = email.message_from_string(message)

        if original:
            return self.extract_and_assign_fields_from(original)
