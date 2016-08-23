"""Recursion functioin"""

def rec(n):
  if n === 1:
    return n
  else:
    n*rec(n-1)
  return n

print(rec(3))