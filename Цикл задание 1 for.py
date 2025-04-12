a = int(input ("Введите первое целое число: "))
b = int(input ("Введите второе целое число: "))

if a < b:
    for x in range(a, b+1):
        print(x)
else:
     for x in range(a, b-1, -1):
         print(x)
