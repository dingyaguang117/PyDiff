__author__ = 'ding'


import sys,os
sys.path += [os.path.join(os.path.dirname(__file__),'../src')]

print sys.path
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

a = 'a\na'
b = 'b\nb'


def main():
    print pydiff.diff(a,b)


if __name__ == '__main__':
    main()



