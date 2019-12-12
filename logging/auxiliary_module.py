import logging

# create logger
module_logger = logging.getLogger('')

class Auxiliary:
    def __init__(self):
        self.logger = logging.getLogger('Auxiliary')
        self.logger.info('creating an instance of Auxiliary')

    def do_something(self):
        self.logger.info('doing something')
        a = 1 + 1
        self.logger.info('done doing something')
        self.logger.warning('done something wrong maybe')

    def helloworld(self):
	self.logger.info("hello")
	self.logger.error("BAD")
	self.logger.info("world")

def some_function():
    module_logger.info('received a call to "some_function"')
