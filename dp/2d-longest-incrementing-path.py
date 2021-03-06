# time: O(num local min * n^2)

def find_paths(square, r, c):
    if local_max(square[r][c]):
        return 1
    steps = 0
    if r > 0:  # up
        steps = max(steps, 1 + find_paths(square, r-1, c))
    if c > 0:  # left
        steps = max(steps, 1 + find_paths(square, r, c-1))
    if c < len(square) - 1:  # right
        steps = max(steps, 1 + find_paths(square, r, c+1))
    if r < len(square) - 1:  # down
        steps = max(steps, 1 + find_paths(square, r+1, c))
    return steps

memo = {}  # local min: longest path from local min

def longest(square):
    steps = 0
    for r in range(len(square)):
        for c in range(len(square)):
            if local_min(square[r][c]):
                try: return memo[(r, c)]
                except KeyError:
                    steps = max(steps, find_paths(square, r, c))
                    memo[(r, c)] = steps
    return steps
