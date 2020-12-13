import graphics
import Simplex

def main():
    print('Задание 1')
    print('1) Графическое решение')
    print('2) Симплекс-метод')
    print('3) SciPy')
    choose = input()
    if (choose == '1'):
        print('Загрузка...')
        graphics.Show()
    elif (choose == '2'):
        lines = []
        count = int(input('Количестов ограничений: '))
        for i in range(count + 1):
            lines.append(input())
        Simplex.calculate(lines)
    elif (choose == '3'):
        pass