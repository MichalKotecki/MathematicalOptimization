# Author: Michał Kotecki
# Date: 19.11.2020
# Description: Function find_local_minima() finds the smallest value for a given function and range.
# Optimization: Smaller range can be searched to achieve the same result.

def find_local_minima(function, step_precision, range_start, range_end):

    smallest_y_value = function(range_start)
    local_minima = range_start

    for x in range(range_start, int(range_end * float(step_precision)), 1):
        x = x / step_precision
        if (function(x) < smallest_y_value):
            smallest_y_value = function(x)
            local_minima = x

    return local_minima, smallest_y_value


def minimize_range(function, range_start, range_end):
        range_middle = (range_start + range_end) / 2
        middle_of_first_half = (range_start + range_middle) / 2
        middle_of_second_half = (range_end + range_middle) / 2

        if(function(middle_of_first_half) < function(range_middle)):
            range_end = range_middle
        elif(function(middle_of_second_half) < function(range_middle)):
            range_start = range_middle
        else:
            range_start = middle_of_first_half
            range_end = middle_of_second_half

        return [range_start, range_end]

if __name__ == '__main__':

    function = lambda x : x + (1.0 / (x *x))
    searched_range = [1, 2]
    searched_range = minimize_range(function, *searched_range)

    local_minima, smallest_y_value = find_local_minima(function, 100_000, *searched_range)

    print("Searched range:", searched_range)
    print("Found following local minima:", local_minima)
    print("Y axis value for this local minima:", smallest_y_value)