import os
import imaplib
from emailsocket import start_server
from flask import Flask, jsonify

class ImapSynchronization:

    def __init__(self):
        if os.getenv('EMAIL_LOGIN') is None: self.login = 'rsiliwoniukgolem@fastmail.com'
        if os.getenv('EMAIL_PASSWORD') is None: self.password = 'dy28fnda6k359q3n'
        if os.getenv('EMAIL_IMAP_URL') is None: self.imap_url = 'imap.fastmail.com'
        self.runserver()

    def open_connection(self):
        """Open Imap connection with given credentials"""
        connection = imaplib.IMAP4_SSL(self.imap_url)
        connection.login(self.login, self.password)
        return connection

    def get_message(self):
        """Message view containing headers:
        - subject
        - to
        - from
        and content"""
        try:
           c = self.open_connection()
           c.select('Inbox', readonly=True)
           typ, msg_data = c.fetch('1', '(RFC822)')
           for response_part in msg_data:
               if isinstance(response_part, tuple):
                   msg = email.message_from_string(response_part[0])
                   print(msg)
                   for header in [ 'subject', 'to', 'from' ]:
                       print('%-8s: %s' % (header.upper(), msg[header]))
        except:
           pass

    def get_senders(self):
        """Sender view"""
        try:
            pass
        except:
           pass

    def timeline_view(self):
       try:
           pass
       except:
           pass

    def topics_view(self):
       try:
           pass
       except:
           pass

if __name__ == '__main__':
    a = ImapSynchronization()
