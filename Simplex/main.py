import graphics
import Simplex
import task1
import task2

while True:
    print('Лабораторная работа 2')
    print('1) Задание 1')
    print('2) Задание 2')
    choose = input()
    print('')
    if (choose == '1'):
        task1.main()
    elif (choose == '2'):
        task2.main()
    print('\n')