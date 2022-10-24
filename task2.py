#Создайте программу для игры с конфетами человек против человека.
from random import randint
import random
import time

#Игра для двух игроков


candy = 150
player = (randint(1, 2))

print(f'На столе {candy} конфет, кто последнюю заберет тот и выиграл')
print("За раз можно взять 28 конфет")

time.sleep(1)
print()
print(f' Начнет игру {player} игрок')
print()

while candy > 28:
    take = int(input(f'Игрок {player}, сколько конфет возьмешь?:  '))
    if take > 28:
        print("За раз можно взять 28 конфет")   
    else:
        candy-=take
        print(f'Конфет осталось {candy}')  
        if player == 1:
            player =  2
        elif player == 2:
            player = 1

print (f'Победил игрок {player}')   




#Игра с ботом


candy = 150


print(f'На столе {candy} конфет, кто последнюю заберет тот и проиграл')

time.sleep(1)

p=1


while candy > 28:
        while p == 1:
            take = int(input(f'Игрок 1, возьми конфет сколько хочешь, но не больше 28:  '))
            if take > 28:
                print("Это больше 28, читай условие)")
            else:
                candy-=take
                print(f'Конфет осталось {candy}')
                p=2
        while p == 2:
            if candy > 28:
                take = randint(1, 28)
                print ('Ход компьютера')
                time.sleep(1)
                print (f'Взял {take} конфет')
                candy-=take
                print(f'Конфет осталось {candy}')
                p=1
            else:
                take = candy
                print (f'Взял {take} конфет и победил')
                candy = 0
                print(f'Конфет осталось {candy}')
                break

if p == 1:
    print('Игрок 1 победил')
else:
    print('Компьютер победил')


       









