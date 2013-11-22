__author__ = 'ding'
import sys,os
sys.path += [os.path.join(os.path.dirname(__file__),'../src')]

import pydiff

a = '''a
a
b
c
d
e'''

b = '''b
b
b
c
d
d
e'''

def main():
    result =  pydiff.diff(a,b)
    for one in result:
        if one.status == -1:
            print '-',one.val
        elif one.status == 1:
            print '+',one.val
        else:
            print ' ',one.val

if __name__ == '__main__':
    main()



