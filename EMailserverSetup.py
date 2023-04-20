from EmailserverAIOSMTPD import *
from AIOSMTPD_Controller import *
from MessageSender import *

class EMailServerSetup(asyncio,AIOSMTPD_Controller,MessageSender):
    pass