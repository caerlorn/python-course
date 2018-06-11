#!/usr/bin/env python

# Yildirim Can Sehirlioglu - 156336IVCM - Hmw2

# So, what I understood from the homework description was that we were asked to use singleton (anti)pattern.
# Although after some research I saw that it is wildly different in Python than in Java or C++.
# As a personal note, I liked the Borg (anti)pattern more as a monostate for Python class instances instead of a
# singleton.


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
