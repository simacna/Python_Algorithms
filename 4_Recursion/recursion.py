"""Recursion functioin"""

def rec(n):
  if n == 1:
    return n
  else:
    return  n*rec(n-1)
  

# print(rec(3))


#below is where 3 functions related to drawing ruler are

def draw_line(tick_length, tick_label=""):
  """Draw one line with given tick length (followed by optional hash label)"""
  line = '-' * tick_length
  print(line)

def draw_interval(center_length):
  """Draw tick interval upon a central tick length"""
  if center_length > 0:
    draw_interval(center_length - 1)
    draw_line(center_length)
    draw_interval(center_length - 1)

def draw_ruler(num_inches, major_length):
  """Draw English ruler with given number of inches, major tick length"""
  draw_line(major_length)
  for j in range(1, 1 + num_inches):
    draw_interval(major_length - 1)    
    draw_line(major_length, str(j))
# draw_ruler(2,4)


def binary_search(data, target, low, high):
  times = 0
  if low > high:
    return False
  else:
    times +=1
    mid = (low + high) // 2
    print("mid", mid)
    if target == data[mid]:
      print("target", target)
      return True
    elif target < data[mid]:
      return binary_search(data, target, low, mid-1)
    else:
      return binary_search(data, target, mid+1, high)


# print(binary_search([2,4,5,7,8,9,12,14,17,19,22,25,27,28,33,37], 22, 0, 16))

def bi_search(data, target):
  first = 0
  last = len(data) - 1
  found = False
  
  while first <= last and not found:
    mid_point = (first + last)//2

# print(bi_search([1,2,4,5], 3))














