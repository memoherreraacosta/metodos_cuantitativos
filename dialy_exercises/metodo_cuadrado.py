print("Enter a number")
n = int(input())

def cuadrado_medio(n):
    if n == 0:
       return
    else:
       sqr = n*n
       str_sqr = str(sqr)
       n = int(str_sqr[1:4])
       print(n)
       cuadrado_medio(n)


cuadrado_medio(n)
