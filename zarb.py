import random

def gen(n):
    a, b = random.randint(1, n), random.randint(1, 10)
    if random.randint(1, 2) == 1:
        a, b = b, a
    return a, b

def correct():
    options = ["Afarin!"]
    print(options[random.randint(0, len(options)-1)])
    return 1

def wrong():
    options = ["Ey Baba!"]
    print(options[random.randint(0, len(options)-1)])
    return 0

def ask(n):
    a, b = gen(n)
    r = random.randint(1, 3)
    if r == 1:
        print(f"{a} x {b} = ?")
        ans = int(input())
        if ans == a * b:
            return correct()
        else:
            return wrong()
    elif r == 2:
        print(f"{a} x ? = {a*b}")
        ans = int(input())
        if ans == b:
            return correct()
        else:
            return wrong()
    else:
        print(f"? x {b} = {a*b}")
        ans = int(input())
        if ans == a:
            return correct()
        else:
            return wrong()


points = 0
for i in range(20):
    points += ask(3)
print("Emtiaz:", points)
