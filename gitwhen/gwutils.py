#/usr/bin/env python

import subprocess

class ParseError(Exception): pass
class FormatError(Exception): pass

def runCmd(cmd):
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    out = [output, err]
    return out

