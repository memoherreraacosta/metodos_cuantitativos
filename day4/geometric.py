n, d =input().split(" ")
l = int(input())

n = int(n)
d = int(d)

p = n / d
q = 1 - p

prob = pow(q, (k - 1)) * p
print(round(prob, 3))

