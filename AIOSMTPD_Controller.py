from aiosmtpd.controller import Controller

class AIOSMTPD_Controller:

    _controller = Controller()
    def __init__(self, ExampleHandler):
        self._controller = Controller(ExampleHandler)
        self._controller.start()

    def stop(self):
        self._controller.stop()

    def get_hostname(self):
        return self._controller.hostname

    def get_port(self):
        return self._controller.port