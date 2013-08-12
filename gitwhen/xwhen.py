#/usr/bin/env python

from abc import ABCMeta, abstractmethod

from gwutils import *

class XWhen:
    __metaclass__ = ABCMeta

    def __init__(self, args):
        self.args = args

    @abstractmethod
    def run(self): pass

class AddWhen(XWhen):
    def run(self):
        res = runCmd("git log --diff-filter=A -- %s" % self.args)
        print res[0]

class RemoveWhen(XWhen):
    def run(self):
        res = runCmd("git log --diff-filter=D -- %s" % self.args)
        print res[0]

