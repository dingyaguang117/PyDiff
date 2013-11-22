PyDiff
======

A library to diff two files, output is unified format

example:

<pre>
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
    print pydiff.diff(a,b)

if __name__ == '__main__':
    main()

</pre>

output
------
- a
- a
+ b
+ b
  b
  c
+ d
  d
  e

