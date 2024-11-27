# math module
import math

print("Value of pi:", math.pi)  # Constant pi
print("Value of e:", math.e)  # Constant e
print("Square root of 64:", math.sqrt(64))  # sqrt() function
print("Ceiling of 4.3:", math.ceil(4.3))  # ceil() function
print("Floor of 4.7:", math.floor(4.7))  # floor() function
print("2 raised to the power 5:", math.pow(2, 5))  # pow() function
print("Absolute value of -5:", math.fabs(-5))  # fabs() function
print("Sine of 90 degrees:", math.sin(math.radians(90)))  # sin() function
print("Cosine of 0 degrees:", math.cos(math.radians(0)))  # cos() function
print("Tangent of 45 degrees:", math.tan(math.radians(45)))  # tan() function

# random module0
from random import random, randint, randrange

print("\nRandom number between 0 and 1:", random())  # random() function
print("Random integer between 1 and 10:", randint(1, 10))  # randint() function
print("Random number from range 0 to 20 with step 5:", randrange(0, 21, 5))  # randrange() function

# statistics module
import statistics

data = [10, 20, 20, 30, 40]
print("\nData:", data)
print("Mean of the data:", statistics.mean(data))  # mean() function
print("Median of the data:", statistics.median(data))  # median() function
print("Mode of the data:", statistics.mode(data))  # mode() function
