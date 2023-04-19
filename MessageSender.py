#https://aiosmtpd.readthedocs.io/en/latest/controller.html
from smtplib import SMTP as Client
from AIOSMTPD_Controller import *
from EmailserverAIOSMTPD import *

class MessageSender:
    _handler = asyncio()
    _controller = AIOSMTPD_Controller()
    client = Client()
    def __init__(self):
        self._controller = AIOSMTPD_Controller(self._handler)
        self.client = Client(self._controller.get_hostname(),self._controller.get_port())

    def Send_Message(self, sender, receiver, message):
        self.client.sendmail(sender, receiver, message)

