# Author: Michał Kotecki
# Date: 19.11.2020
# Description: Function find_local_minima() finds the smallest value for a given function and range.
# Optimization: Smaller range can be searched to achieve the same result.

def find_local_minima(function, precision, range_start, range_end):

    while(range_end - range_start >= precision):
         range_start, range_end = minimize_range(function, range_start, range_end)

    return range_start, range_end


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
    range_start, range_end = find_local_minima(function, 0.001, *searched_range)

    print("Searched range:", searched_range)
    print("Local minima is in the following range:", range_start, range_end)