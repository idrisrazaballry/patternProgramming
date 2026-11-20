'''
          *
              *
                  *
                   *
                   *
                *
           *
      *
  *
*
*
  *
      *
            *
                *
'''
import math

height = 15
width = 10

for y in range(height):
    offset = int((math.sin(y * 0.5) + 1) * width)
    print(" " * offset + "*")

