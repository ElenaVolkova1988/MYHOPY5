# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит заданное количество конфет. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.

# a) Добавьте игру против бота

# b) Подумайте как наделить бота 'интеллектом'

def input_dat(name):
    x = int(
        input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, введите корректное количество конфет: "))
    return x


player1 = input("Игрок 1 : ")
player2 = input("Игрок 2 : ")
value = int(input("Введите количество конфет на столе: "))
