# num = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]x

def gauss(n):
    total = 0
    for item in range(1, n + 1):
        total += item
    print(total)

gauss(100)