

# using recursive and  i still dont understand how this works :) 

def recursive_climber(stairs:int, steps:list):
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

assert recursive_climber(4, [1, 2]) == \
    [[1, 1, 1, 1], [1, 1, 2], [1, 2, 1], [2, 1, 1], [2, 2]]
assert recursive_climber(4, [1, 2, 3]) == \
    [[1, 1, 1, 1], [1, 1, 2], [1, 2, 1], [1, 3], [2, 1, 1], [2, 2], [3, 1]]


#without recursion its a bit trickier

"""
Climber function 

If the stairs N is divible by the X step number the funcion generates arrays [X] x div

example : N = 4 X = [1,2, 3 ] immediatelly generates the arrays:
    [1, 1, 1,  1] and [2, 2]

To generate the remaining arrays, the function loop through the steps X

    example: N = 4 X = [1, 2, 3]

    First loop step size 1
        check if sum(current element + element on the right) < N
        funtion inserts current element on the index 0 pushing the second element to the right

        [2]     < 4 True
        [1,2]   < 4 True
        [1,1,2] < 4 False

        once reach sum(array) = N 
        accessory function SHUFFLE helps us to retrieve the other combinations within the array

        shuffle(array) -> [[1,1,2], [1,2,1], [2,1,1]]

"""

def shuffle (l:list):
    grid = []
    grid.append(l)
    copy=l[:]
    for i in range(len(l), 0 ,-1):
        j=i-1
        if j > 0:
            copy[j], copy[j-1] = copy[j-1], copy[j]
            grid.append(copy[:])
    return grid

def logic_climber(n:int, X:list):
    grid, div, rem = [], [], []
    
    for x in X:
        div.append(n//x)
        rem.append(n%x)

    for i in range (0, len(X)):
        if rem[i]==0:
            sgrid = [X[i]]*div[i]
            grid.append(sgrid) if sgrid not in grid else grid
            sgrid = []
        for j in range (i+1, len(X)):
            sgrid = [X[j]]
            while sum(sgrid)< n:
                sgrid.insert(0,X[i])
                if sum(sgrid)> n:
                    sgrid.remove(X[i])
                    break
            if sum(sgrid) == n:
                if len(sgrid) > 1:
                    sub = shuffle(sgrid)
                    for s in sub:
                        grid.append(s)
                else:
                    grid.append(sgrid) if sgrid not in grid else grid
    return sorted(grid)

assert logic_climber(4, [1, 2]) == \
    [[1, 1, 1, 1], [1, 1, 2], [1, 2, 1], [2, 1, 1], [2, 2]]
assert logic_climber(4, [1, 2, 3]) == \
    [[1, 1, 1, 1], [1, 1, 2], [1, 2, 1], [1, 3], [2, 1, 1], [2, 2], [3, 1]]