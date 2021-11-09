
def check_sum (arr, K):
    for item in arr:
        for i in arr:
            if sum([item, i]) == K:
                return True
    return False

assert not check_sum([], 17)
assert check_sum([10, 15, 3, 7], 17)
assert not check_sum([10, 15, 3, 4], 17)