text = 'abc fgtga abc fkgoo abcfg'.split()
res = list(filter(lambda x: 'abc' not in x, text))
print('1.', res)

def xox(play = True):
    while play == True:
        print('2. Крестики-нолики! \nВводите соответсвующую позицию для игры. \nПервый ряд: 0-1-2 \nВторой ряд: 3-4-5 \nТретий ряд: 6-7-8')
        line1 = '. . .'.split()
        line2 = '. . .'.split()
        line3 = '. . .'.split()
        round = 0
        move = 0
        print('\n', line1, '\n', line2, '\n', line3, '\n')
        while round <= 4:
            if move <= 0:
                x = int(input('Игрок 1, введите желаемую позицию: '))
                if x >-1 and x <= 2:
                    for i in range(len(line1)):
                        if x == i and line1[i] == '.':
                            line1[i] = 'x'
                            move = 1
                        elif x == i and line1[i] != '.':
                            print('Данная позиция уже занята.')
                            move -= 1
                            round -= 1
                elif x > 2 and x <= 5:
                    for i in range(len(line2)):
                        if x - 3 == i and line2[i] == '.':
                            line2[i] = 'x'
                            move = 1
                        elif x - 3 == i and line2[i] != '.':
                            print('Данная позиция уже занята.')
                            move -= 1
                            round -= 1
                elif x > 5 and x < 9:
                    for i in range(len(line3)):
                        if x - 6 == i and line3[i] == '.':
                            line3[i] = 'x'
                            move = 1
                        elif x - 6 == i and line3[i] != '.':
                            print('Данная позиция уже занята.')
                            move -= 1
                            round -= 1
                else:
                    print('Задано некорректное значение.')
                    move -= 1
                    round -= 1
            if move == 1:    
                print('\n', line1, '\n', line2, '\n', line3, '\n')
            if line1[0] == 'x' and line1[2]==line1[1]==line1[0] or line1[0] == 'x' and line3[2]==line2[1]==line1[0] or line1[0] == 'x' and line3[0]==line2[0]==line1[0]:
                print('Игрок 1 побеждает!')
                break
            elif line1[0] == 'o' and line1[2]==line1[1]==line1[0] or line1[0] == 'o' and line3[2]==line2[1]==line1[0] or line1[0] == 'o' and line3[0]==line2[0]==line1[0]:
                print('Игрок 2 побеждает!')
                break
            elif line1[1] == 'x' and line3[1]==line2[1]==line1[1]:
                print('Игрок 1 побеждает!')
                break
            elif line1[1] == 'o' and line3[1]==line2[1]==line1[1]:
                print('Игрок 2 побеждает!')
                break
            elif line1[2] == 'x' and line3[2]==line2[2]==line1[2] or line1[2] == 'x' and line3[0]==line2[1]==line1[2]:
                print('Игрок 1 побеждает!')
                break
            elif line1[2] == 'o' and line3[2]==line2[2]==line1[2] or line1[2] == 'o' and line3[0]==line2[1]==line1[2]:
                print('Игрок 2 побеждает!')
                break
            elif line2[0] == 'x' and line2[2]==line2[1]==line2[0]:
                print('Игрок 1 побеждает!')
                break
            elif line2[0] == 'o' and line2[2]==line2[1]==line2[0]:
                print('Игрок 2 побеждает!')
                break
            elif line3[0] == 'x' and line3[2]==line3[1]==line3[0]:
                print('Игрок 1 побеждает!')
                break
            elif line3[0] == 'o' and line3[2]==line3[1]==line3[0]:
                print('Игрок 2 побеждает!')
                break
            if round == 4:
                move = 0
            if move >= 1:
                o = int(input('Игрок 2, введите желаемую позицию: '))
                if o >- 1 and o <= 2:
                    for i in range(len(line1)):
                        if o == i and line1[i] == '.':
                            line1[i] = 'o'
                            move = 0
                        elif o == i and line1[i] != '.':
                            print('Данная позиция уже занята.')
                            move += 1
                            round -= 1
                elif o > 2 and o <= 5:
                    for i in range(len(line2)):
                        if o - 3 == i and line2[i] == '.':
                            line2[i] = 'o'
                            move = 0
                        elif o - 3 == i and line2[i] != '.':
                            print('Данная позиция уже занята.')
                            move += 1
                            round -= 1
                elif o > 5 and o < 9:
                    for i in range(len(line3)):
                        if o - 6 == i and line3[i] == '.':
                            line3[o - 6] = 'o'
                            move = 0
                        elif o - 6 == i and line2[i] != '.':
                            print('Данная позиция уже занята.')
                            move += 1
                            round -= 1
                else:
                    print('Задано некорректное значение.')
                    move += 1
                    round -= 1
            round += 1
            if move == 0 and round != 5:
                print('\n', line1, '\n', line2, '\n', line3, '\n')
            if line1[0] == 'x' and line1[2]==line1[1]==line1[0] or line1[0] == 'x' and line3[2]==line2[1]==line1[0] or line1[0] == 'x' and line3[0]==line2[0]==line1[0]:
                print('Игрок 1 побеждает!')
                break
            elif line1[0] == 'o' and line1[2]==line1[1]==line1[0] or line1[0] == 'o' and line3[2]==line2[1]==line1[0] or line1[0] == 'o' and line3[0]==line2[0]==line1[0]:
                print('Игрок 2 побеждает!')
                break
            elif line1[1] == 'x' and line3[1]==line2[1]==line1[1]:
                print('Игрок 1 побеждает!')
                break
            elif line1[1] == 'o' and line3[1]==line2[1]==line1[1]:
                print('Игрок 2 побеждает!')
                break
            elif line1[2] == 'x' and line3[2]==line2[2]==line1[2] or line1[2] == 'x' and line3[0]==line2[1]==line1[2]:
                print('Игрок 1 побеждает!')
                break
            elif line1[2] == 'o' and line3[2]==line2[2]==line1[2] or line1[2] == 'o' and line3[0]==line2[1]==line1[2]:
                print('Игрок 2 побеждает!')
                break
            elif line2[0] == 'x' and line2[2]==line2[1]==line2[0]:
                print('Игрок 1 побеждает!')
                break
            elif line2[0] == 'o' and line2[2]==line2[1]==line2[0]:
                print('Игрок 2 побеждает!')
                break
            elif line3[0] == 'x' and line3[2]==line3[1]==line3[0]:
                print('Игрок 1 побеждает!')
                break
            elif line3[0] == 'o' and line3[2]==line3[1]==line3[0]:
                print('Игрок 2 побеждает!')
                break
            if round == 5:
                print('Ничья.')
        i = 0
        while i == 0:
            choice = input('Новая игра? y/n: ')
            if choice == 'n':
                return play == False
            elif choice == 'y':
                i+=1
            else:
                print('Ошибка!')
xox()

import random
def game(play = True):
    while play == True:
        i = 0
        while i == 0:
            mode = input('3. Здравствуйте! \nХотите играть с другим игроком, или с компьютером? h/b: ')
            if mode == 'h' or mode == 'b':
                i+=1
            else:
                print('Ошибка!')
        bank = int(input('Введите желаемое количество конфет в общем банке: '))
        p1mo = 27
        p1scor = 0
        p1bank = 0
        p2scor = 0
        p2bank = 0

        while bank>0:
            move = random.randint(0, 1)
            move = random.randint(0, 1)
            if move != 1:
                p1mo = int(input('Игрок 1 ходит первым! Введите желаемое кол-во конфет: '))
                if p1mo>28 or p1mo>bank:
                    print('Не жадничайте! Вы можете взять не больше чем есть в банке и не более 28 конфет за ход!')
                else:
                    p1scor += p1mo
                    p1bank += p1mo
                    bank -= p1mo
                print('Игрок 1 получил', p1bank, 'конфет(ы)! \n Конфет в банке:', bank, '\n')
                if mode == 'h':
                    p2mo = int(input('Игрок 2, введите желаемое кол-во конфет: '))
                elif bank>28:
                    p2mo = random.randint(1, p1mo+1)
                elif bank>p1mo:
                    p2mo = random.randint(p1mo, bank)
                else:
                    p2mo = random.randint(0, bank)
                if p2mo>28 or p2mo>bank:
                    print('Не жадничайте! Вы можете взять не больше чем есть в банке и не более 28 конфет за ход!')
                else:
                    p2scor += p2mo
                    p2bank = p2bank + p2mo + p1bank
                    p1bank = 0
                    bank -= p2mo
                print('Игрок 2 получил', p2bank, 'конфет(ы)! \n Игрок 1 остался без лакомств :с \n Конфет в банке:', bank, '\n')
            else:
                if mode == 'h':
                    p2mo = int(input('Игрок 2 ходит первым! Введите желаемое кол-во конфет: '))
                elif bank>28:
                    p2mo = random.randint(1, p1mo+1)
                elif bank>p1mo:
                    p2mo = random.randint(p1mo+1, bank)
                else:
                    p2mo = random.randint(0, bank)
                if p2mo>28 or p2mo>bank:
                    print('Не жадничайте! Вы можете взять не больше чем есть в банке и не более 28 конфет за ход!')
                else:
                    p2scor += p2mo
                    p2bank += p2mo
                    bank -= p2mo
                print('Игрок 2 получил', p2bank, 'конфет(ы)! \n Конфет в банке:', bank, '\n')
                p1mo = int(input('Игрок 1, введите желаемое кол-во конфет: '))
                if p1mo>28 or p1mo>bank:
                    print('Не жадничайте! Вы можете взять не больше чем есть в банке и не более 28 конфет за ход!')
                else:
                    p1scor += p1mo
                    p1bank = p1bank + p1mo + p2bank
                    p2bank = 0
                    bank -= p1mo
                print('Игрок 1 получил', p1bank, 'конфет(ы)! \nИгрок 2 остался без лакомств :с \n Конфет в банке:', bank, '\n')

        if p1bank>p2bank:
            print('Игрок 1 побеждает с личным счётом в', p1scor, 'конфет!')
        elif p1bank<p2bank:
            print('Игрок 2 побеждает с личным счётом в', p2scor, 'конфет!')
        else:
            print('Ничья!')
        i = 0
        while i == 0:
            choice = input('Новая игра? y/n: ')
            if choice == 'n':
                return play == False
            elif choice == 'y':
                i+=1
            else:
                print('Ошибка!')
game()

text = input('4. Введите текст, что желаете сжать: \n')
with open('dz4tin.txt', 'w') as tin:
    tin.writelines(text)
tin = open('dz4tin.txt', 'r')
tin = str(*tin)
enc = ''
co = 1

for i in range(len(tin)-1):
    if i <= len(tin):
        if tin[i] == tin[i + 1] and tin[i].isdigit()==False and co < 9:
            co += 1
        elif tin[i].isdigit():
            enc+=tin[i]
        elif co == 9:
            enc+=str(co)+tin[i]
            co = 1
        else:
            enc += str(co)+tin[i]
            co = 1
if tin[i+1].isdigit():
    enc+=tin[i+1]
else:
    enc += str(co)+tin[i+1]
print(enc)
with open('dz4tout.txt', 'w') as tout:
    tout.writelines(enc)
dec = ''
for i in range(len(enc)):
    if i<len(enc)-1:
        if enc[i].isdigit() and enc[i+1].isdigit() == False:
            co = enc[i]
        elif enc[i].isdigit() and enc[i+1].isdigit():
            dec += enc[i]
        else:
            dec += enc[i]*int(co)
    else:
        if enc[i].isdigit():
            dec += enc[i]
        else:
            dec += enc[i]*int(co)
print(dec)
