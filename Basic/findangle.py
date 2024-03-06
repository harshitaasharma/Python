# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
ab = float(input())
bc = float(input())
print(str(round(math.atan(ab/bc) / math.pi * 180)) + '\u00B0')
