
def solution(X: int, Y: int, D: int):
    jumps = 0
    distance = Y-X
    while (distance > 0):
        distance -= D
        jumps += 1

    return jumps

print(solution(10, 85, 30))
