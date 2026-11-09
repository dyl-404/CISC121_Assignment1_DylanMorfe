arr = [4, 4, 8, 5, 2, 1, 1]

def solution (N: int, A: list[int]):
    n = len(A)
    counters = [0] * N
    min = 0
    max = 0
    for i in range(n):
        if 1 <= A[i] <= N:
            # if an element appears after the min has changed
            if counters[A[i] - 1] < min:
                counters[A[i] - 1] = min + 1
            else:
            # increment the counter for that number
                counters[A[i] - 1] += 1
            # sets the new max
            if counters[A[i] - 1] > max:
                max = counters[A[i] - 1]
        # sets max counter
        elif A[i] == N + 1:
            min = max
    for i in range(N):
        # if the counter was untouched
        if counters[i] < min:
            counters[i] = min
    return counters

print(solution(7, arr))
