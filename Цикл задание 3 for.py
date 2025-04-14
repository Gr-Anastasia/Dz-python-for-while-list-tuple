i = int(input("Введите натуральное число n ≤ 9 : "))

n = 1

for x in range(1, i+1):
    x = ""
    for y in range(1, i+1):
        x += str(y)
        print(x)
    
