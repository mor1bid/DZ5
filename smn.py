def f(x):
    x**2

g = f
print(f(1))
print(g(1))

def f(x):
    return x**2
print(g(2))
print(type(f))

def calc(x):
    return x+10
# print(calc(10))

def calc2(x):
    return x*10
# print(calc2(10))

# Сокращаем (op - operator):
def math(op, x):
    print(op(x))

math(calc2, 10)
math(calc, 10)

# def sum(x, y):
#     return x+y

sum = lambda q, w: q+w

def mult(x, y):
    return x*y
def calc(op, a, b):
    print(op(a, b))
calc(lambda q, w: q+w, 4, 5)
calc(sum, 6, 6)

#filter
lisst = []

# for i in range(1, 101):
#     if i%2 == 0:
#         lisst.append(i)
    
# print(lisst)

def f(x):
    return x**2

lisst = [(i, f(i)) for i in range(1, 21) if i % 2 == 0]
print(lisst)

num = []
with open('l.txt', 'r') as dig:
    for i in dig:
        n = dig.read()
        num.append(n)
print(num)
# stripe = [(i, f(i)) for i in num]
# print(stripe)