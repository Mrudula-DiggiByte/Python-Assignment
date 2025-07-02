import numpy

def process_matrix_stats(array):
    # Mean across axis 1 (rows)
    mean_result = numpy.mean(array, axis=1)

    # Variance across axis 0 (columns)
    var_result = numpy.var(array, axis=0)

    # Standard deviation rounded to 11 decimal places
    std_result = round(numpy.std(array), 11)

    return mean_result, var_result, std_result
