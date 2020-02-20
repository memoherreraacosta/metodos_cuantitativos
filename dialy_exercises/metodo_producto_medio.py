print("Enter first number")
n = int(input())
print("Enter seconds number")
m = int(input())

def producto_medio(n, m):
    if m == 0:
       return
    else:
       mul = n*m
       str_mul = str(mul)
       try:
           med_mul = str(int(str_mul[1:len(str_mul) - 1]))
       except ValueError:
           return
       n = m
       m = int(med_mul) if len(med_mul) <= 3 else int(med_mul[:3])
       print(n)
       producto_medio(n, m)


producto_medio(n, m)
