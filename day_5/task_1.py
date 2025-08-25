score = [15, 50, 45, 60, 75, 90]

def sum(score):
    total = 0

    for item in score:
        total += item

    print(total)

sum(score)


def max(score):
    max = 0

    for item in score:
        if item > max:
            max = item
    print(max)

max(score)