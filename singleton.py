#!/usr/bin/env python

def singleton(obj):
    cl = obj.__class__
    if hasattr(cl, '__instantiated'):
        raise ValueError("%s has already have an instance as per singleton requirements\n" % cl)
    else:
        cl.__instantiated = True
        print "\nAsh nazg durbatuluk, ash nazg gimbatul\nAsh nazg thrakatuluk agh burzum-ishi krimpatul\n"


class TheOneRing:
    """Singleton"""
    def __init__(self):
        singleton(self)


try:
    s = TheOneRing()
    a = TheOneRing()
except ValueError as e:
    print (str(e))
