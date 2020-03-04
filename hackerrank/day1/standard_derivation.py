from math import sqrt

n = 5 #int(input())
x = "10 40 30 50 20".split(" ")  #input().split(" ")

x = [int(number) for number in x]

mean = sum(x)/n
square = lambda x: x*x 

standard_dev = sqrt(
    sum([
        square(element - mean)
        for element in x
    ])/n
)

print(round(standard_dev,1))
