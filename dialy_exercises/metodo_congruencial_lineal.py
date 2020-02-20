print("Ingresa el valor de 'a'")
a = int(input())
print("Ingresa el valor de 'c'")
c = int(input())
print("Ingresa el valor de 'm'")
m = int(input())

def metodo_congruencial_lineal(a, c, m):
    s = c
    for i in range(m):
        print(c)
        c =(a*s + c)%m

metodo_congruencial_lineal(a, c, m)
