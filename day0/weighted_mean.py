#n = input()
#x = input()
#w = input()
n = "5"
x = "10 40 30 50 20"
w = "1 2 3 4 5"

n = int(n)
x = [int(element) for element in x.split(" ")]
w = [int(element) for element in w.split(" ")]

def weighted_mean():
    w_x = 0
    wi = 0
    for index in range(n):
        wi += w[index]
        w_x += x[index] * w[index]
    return round(w_x / wi), 1)

print(weighted_mean())
