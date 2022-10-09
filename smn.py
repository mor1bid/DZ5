text = 'abc fgtga abc fkgoo abcfg'.split()
res = list(filter(lambda x: 'abc' not in x, text))
print('1.', res)

line1 = '. . .'.split()
line2 = '. . .'.split()
line3 = '. . .'.split()
round = 0
move = 0
print('\n', line1, '\n', line2, '\n', line3, '\n')
while round < 3:
    if move == 0:
        x = int(input('Игрок 1, введите желаемую позицию: '))
        if x >-1 and x <= 2:
            for i in range(len(line1)):
                if x == i and line1[i] == '.':
                    line1[i] = 'x'
        elif x > 2 and x <= 5:
            for i in range(len(line2)):
                if x-3==i and line2[i] == '.':
                    line2[i] = 'x'
        elif x > 5 and x < 9:
            for i in range(len(line3)):
                if x - 6 == i and line3[i] == '.':
                    line3[i] = 'x'
        else:
            print('Задано некорректное значение.')
    print('\n', line1, '\n', line2, '\n', line3, '\n')
    move += 1
    if move == 1:
        o = int(input('Игрок 2, введите желаемую позицию: '))
        if o >- 1 and o <= 2:
            for i in range(len(line1)):
                if o==i and line1[i] == '.':
                    line1[i] = 'o'
        elif o > 2 and o <= 5:
            for i in range(len(line2)):
                if o - 3 == i and line2[i] == '.':
                    line2[i] = 'o'
        elif o > 5 and o < 9:
            for i in range(len(line3)):
                if o - 6==i and line3[i] == '.':
                    line3[i] = 'o'
        else:
            print('Задано некорректное значение.')
    print('\n', line1, '\n', line2, '\n', line3, '\n')
    move -= 1
    round += 1
if line1[0] == 'x' and line1[2]==line1[1]==line1[0] or line3[2]==line2[1]==line1[0] or line3[0]==line2[0]==line1[0]:
    print('Игрок 1 побеждает!')
elif line1[0] == 'o' and line1[2]==line1[1]==line1[0] or line3[2]==line2[1]==line1[0] or line3[0]==line2[0]==line1[0]:
    print('Игрок 2 побеждает!')
elif line1[0] == 'x' and line3[1]==line2[1]==line1[1]:
    print('Игрок 1 побеждает!')
elif line1[0] == 'o' and line3[1]==line2[1]==line1[1]:
    print('Игрок 2 побеждает!')
elif line1[0] == 'x' and line3[2]==line2[2]==line1[2] or line3[0]==line2[1]==line1[2]:
    print('Игрок 1 побеждает!')
else:
    round==0
