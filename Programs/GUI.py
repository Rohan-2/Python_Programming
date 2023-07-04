picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

# iterate over picture
 # if 0 -> print ''
 # if 1 -> print *

fill = '*'
empty = ' '
for row in picture:
  for pixel in row:
    if (pixel):
      print(fill, end='')
    else:
      print(empty, end='')
  print('')       # need a new line after every row