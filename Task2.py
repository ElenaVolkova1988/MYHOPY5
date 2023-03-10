# Создайте программу для игры в 'Крестики-нолики'
# НЕОБЯЗАТЕЛЬНО Добавить игру против бота с интеллектом

my_list= list(range (1,10)) #  создаем ячейки от 1 до 9
win_code = [(1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7)]# выигрышные комбинации, записаны в кортежи, потому что они неизменны
def draw_desk():
    for i in range(3):
        print( '|', my_list [0+i*3],'|', my_list [1+i*3],'|', my_list[2+i*3], '|' ) # в цикле рисуем поле, 3 раза по 3 строчки и заполняем цифрами от 1 до 9
    
def take_input(game):
    while True:
        temp= input('Куда поставить ' + game) # проверка на то,  указал ячейку от 1 до 9
        if not (temp in '123456789'):
            print ('Неверный ввод')
            continue                           # после того как программа выдала неверный ввод, она возвращает пользователя опять к вводу
        temp= int(temp)                        # проверка на то, что проверить не занята ли ячейка
        if str(my_list[temp-1]) in 'XO':
            print ('Эта ячейка уже занята')
            continue                            # если ячейка занята, то пользователя отправляем еще раз на ввод
        my_list[temp-1]=game                    # если ячейка указана правильно и свободная, то в нее записывает, что ввел пользователь или Х или О
        break                                   # выходим из цикла после записи в ячейку, что б не гонял по кругу
 
def check ():   
    for j in win_code:
        if ( my_list[j[0]-1])==(my_list[j[1]-1])==(my_list[j[2]-1]): # проверка вышгрышных комбинаций по кортежам
            return my_list [j[1]-1]
        else:
            return False
        
def main():
    count=0 # счетчик ходов
    while True:
        draw_desk() # заполняем поле
        if count %2 ==0: # если ход четный,то
            take_input('X') # поставить Х
        else:
            take_input('O')    
        if count > 3: # если уже сделано больше трех ходов, нужно проверить нет ли выигрышных комбинации
            winner=check()
            if winner:
                draw_desk() # перерисовываем поле
                print(winner, " Вы выиграли!")
                break
        count +=1 # если ходов меньше трех, переходим дальше
        if count > 8: # завершить игру
            draw_desk()
            print ("Игра окончена")
            break
                
main()            




