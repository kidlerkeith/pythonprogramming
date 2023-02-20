
import math

x = float(input("Please enter a value in degrees: "))

sin_x = math.sin(math.radians(x))
cos_x = math.cos(math.radians(x))
tan_x = math.tan(math.radians(x))

print("The sin of", x, "is", sin_x)
print("The cos of", x, "is", cos_x)
print("The tan of", x, "is", tan_x)
