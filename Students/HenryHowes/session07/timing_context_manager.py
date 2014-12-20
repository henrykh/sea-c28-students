import time
import sys


class Timer(object):

    def __init__(self, handled_errors, file_out=sys.stdout):
        if self.file_out is not sys.stdout:
            self.file_out = open(file_out, 'w')
        else:
            self.file_out = file_out
        self.handled_errors = handled_errors

    def __enter__(self):
        self.timer = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.timer = time.time() - self.timer
        self.file_out.write(u"this code took {} seconds".format(self.timer))
        if self.file_out is not sys.stdout:
            self.file_out.close()
        return self.handled_errors
