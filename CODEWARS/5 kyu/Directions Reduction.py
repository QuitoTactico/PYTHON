from collections import deque

def dir_reduc(arr):
    dir = deque()

    for i in arr:
        if dir and ((dir[-1] == 'NORTH' and i == 'SOUTH') or (dir[-1] == 'SOUTH' and i == 'NORTH') or (dir[-1] == 'EAST' and i == 'WEST') or (dir[-1] == 'WEST' and i == 'EAST')):
            dir.pop()

        else: 
            dir.append(i)

    return list(dir)


''' better than me:

opposite = {'NORTH': 'SOUTH', 'EAST': 'WEST', 'SOUTH': 'NORTH', 'WEST': 'EAST'}

def dirReduc(plan):
    new_plan = []
    for d in plan:
        if new_plan and new_plan[-1] == opposite[d]:
            new_plan.pop()
        else:
            new_plan.append(d)
    return new_plan
    
# ----------------------------------------------------------------


def dirReduc(arr):
    dir = " ".join(arr)
    dir2 = dir.replace("NORTH SOUTH",'').replace("SOUTH NORTH",'').replace("EAST WEST",'').replace("WEST EAST",'')
    dir3 = dir2.split()
    return dirReduc(dir3) if len(dir3) < len(arr) else dir3

'''