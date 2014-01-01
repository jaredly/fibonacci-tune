cimport cython
cimport numpy
import numpy

@cython.cdivision(True)
cdef double lperiod(unsigned mod) nogil:
    cdef double first, second, a, b, count
    cdef char gotfirst = 0
    first = second = a = b = 1
    count = 0
    while count < 100 * 1000 * 1000:
        a, b = b, (a + b) % mod
        if gotfirst == 1:
            if a == second:
                break
            gotfirst = 0
        else:
            gotfirst = a == first
        count += 1
    return count

def lenperiod(unsigned mod):
    return lperiod(mod)

'''
couldn't quite get this working

@cython.wraparound(False)
@cython.boundscheck(False)
cdef numpy.ndarray[double, ndim=2] mperiods(unsigned maxmod):
    result = numpy.zeros([2, maxmod-4])
    cdef unsigned i = 0
    for i in range(4, maxmod):
        result[i, 0] = i-4
        result[i, 1] = lperiod(i)
    return result

def manyperiods(unsigned maxmod):
    return mperiods(maxmod)
'''

