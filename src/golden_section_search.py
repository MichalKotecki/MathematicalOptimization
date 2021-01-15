# Author: Michał Kotecki
# Date: 15.01.2020
# Description: Golden section search is used to find function's minimum.

import math

def golden_section_search(function, precision, range_start, range_end):

    p = ((math.sqrt(5) - 1) / 2)

    while abs(range_start - range_end) >= precision:
        t1 = range_start + (1 - p) * (range_end - range_start)
        t2 = range_start + (p * (range_end - range_start))

        if function(t1) > function(t2):
            range_start = t1
        elif function(t1) < function(t2):
            range_end = t2
        else:
            range_start = t1
            range_end = t2

    return range_start, range_end


if __name__ == '__main__':

    function = lambda x : x + (1.0 / (x *x))
    searched_range = [1, 2]

    minimized_range = golden_section_search(function, 0.001, *searched_range)
    print('Minimized range is: ', minimized_range)