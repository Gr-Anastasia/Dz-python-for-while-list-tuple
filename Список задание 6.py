listok = [1,2,4,8,9,100,15,13,17,28,56,74,62,35,45,78]

x = 0

for c in listok:
    c = int(c)

    if c > x:
        x = c

i = listok.index(x)


print("Максимальное число -", x, "Его индекс - ", i)

