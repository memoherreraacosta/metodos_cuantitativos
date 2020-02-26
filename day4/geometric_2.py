n, d =input().split(" ")
k = int(input())

n = int(n)
d = int(d)

p = n / d
q = 1 - p

prob = 1- pow(q, k)
print(round(prob,3))
