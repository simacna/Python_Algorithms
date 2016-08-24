"""Recursion functioin"""

def rec(n):
  if n == 1:
    return n
  else:
    return  n*rec(n-1)
  

print(rec(3))


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
  draw_line(major_length, '0')
  for j in range(1, 1 + num_inches):
    draw_line()


