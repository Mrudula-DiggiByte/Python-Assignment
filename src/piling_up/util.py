from collections import deque
def is_piling_possible(cube_list):
    cubes = deque(cube_list)
    last = float('inf')

    while cubes:
        if cubes[0] >= cubes[-1] and cubes[0] <= last:
            last = cubes.popleft()
        elif cubes[-1] >= cubes[0] and cubes[-1] <= last:
            last = cubes.pop()
        else:
            return "No"

    return "Yes"
