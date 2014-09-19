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

</pre>

<pre>
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
</pre>
