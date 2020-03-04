from random import random
from math import sqrt

print("Write the number of points used")
num_points = int(input())

""" Define the proportion of the number of points inside
    of a quarter of a circle which is inside of a square
"""
def monte_carlo(points):
    points_in_circle = 0
    for cycle in range(points): 
        r1 = random()
        r2 = random()
        r1 = r1- .5
        r2 = r2- .5
        if sqrt((r1*r1 + r2*r2)) <= .5:
            points_in_circle += 1

    return 4*points_in_circle/points

print(monte_carlo(num_points))
