import numpy

def calculate_determinant(matrix):
    A = numpy.array(matrix)
    return round(numpy.linalg.det(A), 2)