# Author: Michał Kotecki
# Date: 05.11.2020
# Description: Function find_local_minima() finds the smallest value for a given function and range.


def find_local_minima(function, step_precision, range_start, range_end):

    smallest_y_value = function(range_start)
    local_minima = range_start

    for x in range(range_start, range_end * step_precision, 1):
        x = x / step_precision
        if (function(x) < smallest_y_value):
            smallest_y_value = function(x)
            local_minima = x

    return local_minima, smallest_y_value

if __name__ == '__main__':

    function = lambda x : x + (1.0 / (x *x))
    searched_range = [1, 2]

    local_minima, smallest_y_value = find_local_minima(function, 100_000, *searched_range)

    print("Searched range:", searched_range)
    print("Found following local minima:", local_minima)
    print("Y axis value for this local minima:", smallest_y_value)