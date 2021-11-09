

# using recursive
def climber(stairs:int, steps:list):
    grid = []

    if stairs < min(steps):
        return grid

    for step_size in steps:
        if stairs == step_size:
            grid.append([step_size])
        elif stairs > step_size:
            sub_grids = climber(stairs -step_size, steps)
            for sub_grid in sub_grids:
                grid.append([step_size]+ sub_grid)
    return grid

assert climber(4, [1, 2]) == \
    [[1, 1, 1, 1], [1, 1, 2], [1, 2, 1], [2, 1, 1], [2, 2]]
assert climber(4, [1, 2, 3]) == \
    [[1, 1, 1, 1], [1, 1, 2], [1, 2, 1], [1, 3], [2, 1, 1], [2, 2], [3, 1]]