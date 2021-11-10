
#python/006.py
#lowest positive value in time and space 


def missing_positive(arr:list):
    pos = [x for x in sorted(arr) if x >= 0]
    if pos:
        missing= [x for x in range(min(pos), max(pos)+2) if x not in pos]
        return min(missing)
    return None

assert missing_positive([3, 4, -1, 1]) == 2
assert missing_positive([1, 2, 0]) == 3
assert missing_positive([-1, -2, 0, 2]) == 1