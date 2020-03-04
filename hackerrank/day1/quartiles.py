#n = int(input())
#x = [int(element) for element in input().split(" ")]

x = sorted([8,6,2,2,5,8])
n = len(x)
pair = lambda n: n % 2 == 0
decimal = lambda n: n % 1 == 0

def median(n, x):
    is_pair = pair(n)
    index = n//2
    pair_median = (x[index - 1] + x[index])/2
    median_to_return = int(pair_median) if decimal(pair_median) else pair_median
    return median_to_return if is_pair else x[index]


def quartiles(n, x):
    q2 = median(n, x)
    is_pair = pair(n)
    mid = int(n/2) if is_pair else int(n//2)
    if is_pair:
        q1 = median(mid, x[:mid])
        q3 = median(mid, x[mid:])
    else:
        q1 = median(mid, x[:mid])
        q3 = median(mid, x[mid + 1:])
    print(q1)
    print(q2)
    print(q3)


quartiles(n, x)
