#https://stackoverflow.com/questions/2690965/a-simple-smtp-server-in-python
#https://docs.python.org/3/library/smtpd.html
#https://aiosmtpd.readthedocs.io/en/latest/
from __future__ import print_function
from datetime import datetime
import asyncore
#from smtpd import SMTPServer deprecated
from aiosmtpd import *

class EmlServer(SMTPServer):
    no = 0
    foo = 0
    def __init__(self):
        pass
    def process_message(self, peer, mailfrom, rcpttos, data):
        filename = '%s-%d.eml' % (datetime.now().strftime('%Y%m%d%H%M%S'),
                self.no)
        f = open(filename, 'w')
        f.write(data)
        f.close
        print('%s saved.' % filename)
        self.no += 1


    def run(self):
        # start the smtp server on localhost:1025
        self.foo = EmlServer(('localhost', 1025), None)
        try:
            asyncore.loop()
        except KeyboardInterrupt:
            pass

    def stop(self):
        self.foo.stop()
