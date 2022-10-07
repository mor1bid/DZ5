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

# num = []
# with open('l.txt', 'r') as dig:
#     for i in dig:
#         num.append(i)
# num = str(num).split()
# print(num)
# stripe = [(i, f(i)) for i in num if num.isdigit()]
# print(stripe)

dig = open('l.txt', 'r')
data = dig.read() + ' '
dig.close()

num = []

while data != '':
    space_pos = data.index(' ')
    num.append(int(data[:space_pos]))
    data = data[space_pos+1:]

out = []
for e in num:
    if not e % 2:
        out.append((e,e **2))
print(out)

# map (использвать только 1 раз)

li = [x for x in range(1,20)]

li = list(map(lambda x:x+10, li))

print(li)

mydata = map(int,input().split())

for e in mydata:
    print(e)

print('--')

for e in mydata:
    print(e)

data = [x for x in range(10)]

res = list(filter(lambda x: x%2==0, data))
print(res)

boys = ['biba69', 'boba13', 'beb12a']
ip = [1, 2, 3]
money = ['none']

users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4, 5, 9, 14, 7]

data = list(zip(boys, ip))
# data = list(enumerate(zip(users, ids)))
print(data)