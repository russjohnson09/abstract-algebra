 # -- coding: utf-8 --
from __future__ import print_function
import sys
from sys import argv
from numpy import array
from pyparsing import *

array_parser = OneOrMore(CharsNotIn('&') + '&' ) + CharsNotIn('&\\')  + restOfLine

element_parser = CharsNotIn('&\\').setResultsName('value')
ex = CharsNotIn('&\\').setResultsName('value') + oneOf("& \\")


element = CharsNotIn('&')

#row = ZeroOrMore(element + Suppress('&')) + element + Optional('\\\\')

#array = "\\begin{array}" + OneOrMore(~Literal("\\end{array}") + row) + "\\end{array}"


def transpose(fin):
    lst = []
    for line in fin:
        tmp = []
        for t,s,e in ex.scanString(line):
            if t.value:
                tmp.append(t.value)
        lst.append(tmp[:-1])
    print(len(lst))
    print(len(lst[0]))

    return zip(*lst)

def print_transpose(fout, lst):
    for i in lst:
        for j in i:
            fout.write(j)
            fout.write('&')
        fout.write('\\\\\n')

def parse(fin):
    for line in fin:
        a = row.parseString(line)
        print(a)
    return
    string = fin.read()
    string = string[:-1]
    print(string)
    a = array.parseString(string)
    print(a)
    




if __name__ == "__main__":
#    with file(argv[1],'r') as fin:
#        lst = parse(fin)



#    sys.exit(0)
    with file(argv[1],'r') as fin:
        lst = transpose(fin)
    if len(argv) == 3:
        with file(argv[2], 'w') as fout:
            print_transpose(fout, lst)
    else:
        print_transpose(sys.stdout, lst)

