def solution(A, B):
  if A == B:
    return 0

  for i in range(1, len(A)):
    rotated_A = A[-1] + A[:-1]
    if rotated_A == B:
      return i
    A = rotated_A

  return -1