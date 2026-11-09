arr = [-2, 0, 5, 8, 1]

#  https://chatgpt.com/c/6af142bb-c308-83e9-ae6c-b80adbb5d494
def solution(A: list[int]):
    n = len(A)
    for i in range(n):
        while 0 < A[i] <= n:
            # having a number be in its correct position ie first element = 1
            correct_idx = A[i] - 1
            if A[i] == A[correct_idx]:
                break
            # swap the number to be in its correct position
            A[i], A[correct_idx] = A[correct_idx], A[i]

    for i in range(n):
        # if the element is not in the correct index
        if A[i] != i + 1:
            return i + 1
    # array has all consecutive positive integers and returns length + 1
    return n + 1

print(solution(arr))
