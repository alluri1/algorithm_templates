# Use when finding next greater or previous smaller elements:
def monotonic_increasing(A):
    stack = []  # stores indices or values
    result = [None] * len(A)

    for i in range(len(A)):
        # Pop elements smaller than current (for next greater)
        while stack and A[stack[-1]] < A[i]:
            stack_top = stack.pop()
            # do something with stack top here

        # if stack has some elements left
        # do something with stack top here e.g.
        # previousGreater[i] = stack.at(-1)
        stack.append(i)

    return result
