

# using recursive

def climber(stairs:int, steps:list):
    grid = []
    print('function called')
    if stairs < min(steps):
        return grid
    print('stairs has %s steps'%(stairs))
    for step_size in steps:
        print('step size: %s with index %s of %s' %(step_size,steps.index(step_size)+1,len(steps)))
        if stairs == step_size:
            grid.append([step_size])
            print('append', step_size)
        elif stairs > step_size:
            print(' stairs bigger than step, callback')
            sub_grids = climber(stairs -step_size, steps)
            print('sub_grids',sub_grids)
            for sub_grid in sub_grids:
                grid.append([step_size]+ sub_grid)
                print('add subgrid grid is now',grid)
    print('return', grid)
    return grid

assert climber(4, [1, 2]) == \
    [[1, 1, 1, 1], [1, 1, 2], [1, 2, 1], [2, 1, 1], [2, 2]]
assert climber(4, [1, 2, 3]) == \
    [[1, 1, 1, 1], [1, 1, 2], [1, 2, 1], [1, 3], [2, 1, 1], [2, 2], [3, 1]]


#without recursion

def rounds (n):
    """
     f2, f3 = f2, f1+f2
     f3, f4 = f3, f2+f3
     f4, f5 = f4, f3+f4
    """
    #f1, f2 = 1, 2 
    a, b = 1, 2
    for _ in range(n-1):
        a, b = b, a + b
    return a