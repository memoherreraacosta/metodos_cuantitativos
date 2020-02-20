print("Ingresa el valor de 'a'")
a = int(input())
print("Ingresa el valor de 'm'")
m = int(input())

def metodo_congruencial_lineal(a, m):
    s = a
    for i in range(m):
        print(s)
        s = (a*s)%m
        if s == a:
            return


metodo_congruencial_lineal(a, m)
