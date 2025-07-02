import numpy


def process_array(arr):
    numpy.set_printoptions(sign=' ')  # Ensures space after sign
    arr = numpy.array(arr, dtype=float)

    print(numpy.floor(arr))
    print(numpy.ceil(arr))
    print(numpy.rint(arr))