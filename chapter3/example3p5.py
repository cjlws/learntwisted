from twisted.internet.defer import Deferred
from twisted.python.failure import DefaultException

def callback1(result):
    print "Callback 1 said:", result
    return result

def callback2(result):
    print "Callback 2 said:", result

def callback3(result):
    raise Exception("Callback 3")

def errback1(failure):
    print "Errback 1 had an error on", failure
    return failure

def errback2(failure):
    raise Exception("Errback 2")

def errback3(failure):
    print "Errback 3 took care of", failure
    return "Everythhing is fine now"

# Exercise 1
# d = Deferred()
# d.addCallback(callback1)
# d.addCallback(callback2)
# d.callback("Test")

# Exercise 2
# d = Deferred()
# d.addCallback(callback1)
# d.addCallback(callback2)
# d.addCallback(callback3)
# d.callback("Test")

# Exercise 3
# d = Deferred()
# d.addCallback(callback1)
# d.addCallback(callback2)
# d.addCallback(callback3)
# d.addErrback(errback3)
# d.callback("Test")

# Exercise 4
# d = Deferred()
# d.addErrback(errback1)
# d.errback(DefaultException("Test"))

# Exercise 5
# d = Deferred()
# d.addErrback(errback1)
# d.addErrback(errback3)
# d.errback(DefaultException("Test"))

# Exercise 6
# d = Deferred()
# d.addErrback(errback2)
# d.errback(DefaultException("Test"))

# Exercise 7
# d = Deferred()
# d.addCallback(callback1)
# d.addCallback(callback2)
# d.addCallbacks(callback3, errback3)
# d.callback("Test")

# Exercise 8
d = Deferred()
d.addCallback(callback3)
d.addCallbacks(callback2, errback3)
d.addCallbacks(callback1, errback2)
d.callback("Test")


