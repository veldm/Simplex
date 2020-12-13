import graphics
import Simplex
from scipy import optimize

def main():
    print('Задание 1')
    print('1) Симплекс-метод')
    print('2) SciPy')
    choose = input()    
    if (choose == '1'):
        lines = []
        count = int(input('Количестов ограничений: '))
        for i in range(count + 1):
            lines.append(input())
        Simplex.calculate(lines)
    elif (choose == '2'):
        res = optimize.linprog([-3, -1], [[2, 1], [1, 0], [0, 1]], [5, 7, 3])
        print(res)