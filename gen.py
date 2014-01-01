# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

import pyximport
pyximport.install()
from gen_c import lenperiod
import numpy

import time
def genlots(upto = 1000000, start = 4):
    if start < 4:
        start = 4
    s = time.time()
    result = numpy.zeros(upto - start)
    for i in xrange(start, upto):
        result[i - start] = lenperiod(i)
        if i % 10000 == 0:
            print i, (time.time()-s)/60.0
    print time.time()-s, start, upto
    return result

# <codecell>

# this took like 40 minutes. so just load the below file. 

def main():
    import sys
    if len(sys.argv) < 3:
        print 'Usage: gen.py num outname [start]'
        sys.exit(1)
    try:
        number = int(sys.argv[1])
    except:
        print 'First argument must be an integer'
        sys.exit(2)
    start = 4
    if len(sys.argv) == 4:
        try: start = int(sys.argv[3])
        except:
            print 'Start must be an integer'
            sys.exit(3)
    numpy.save('%s.npy' % sys.argv[2], genlots(number, start))

if __name__ == '__main__':
    main()
