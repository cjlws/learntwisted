from twisted.internet.defer import Deferred
from twisted.python.failure import DefaultException

def myErrback(failure):
    print failure

d = Deferred()
d.addErrback(myErrback)
d.errback(DefaultException("Triggering errback"))

