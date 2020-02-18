# Enter your code here. Read input from STDIN. Print output to STDOUT
#input = input().splitline()

input = """10
64630 11735 14216 99233 14470 4978 73429 38120 51135 67060"""
input = input.splitlines()
n = int(input[0])
x = input[1].split(" ")
x = sorted([int(element) for element in x])

def mean():
    return sum(x)/n


def median():
    pair = True if isinstance(n/2, int) else False
    index = n//2
    return x[index] if pair else (x[index] + x[index - 1])/2


def mode():
    my_dict = {
        i: x.count(i)
        for i in x
    }
    elements = list(my_dict.keys())
    mode = [
        k
        for k, v in my_dict.items()
        if v == max(list(my_dict.values()))
    ][0]
    return mode


print(mean())
print(median())
print(mode())
