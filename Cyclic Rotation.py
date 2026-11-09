arr = [2, 5, 1, 3, 6, 8]

def solution(A: list[int], K: int):
    n = len(A)
    b = [None] * n
    for i in range(n):
        # getting new position and ensuring that the last elements are brought to the first positions (% n)
        new_position = (i + K) % n
        b[new_position] = A[i]
    return b

print(solution(arr, 5))
