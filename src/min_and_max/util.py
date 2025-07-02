import numpy

def min_then_max(array_2d):

    array = numpy.array(array_2d)
    return int(numpy.max(numpy.min(array, axis=1)))

