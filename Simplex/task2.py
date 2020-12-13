import Simplex
from scipy import optimize

def main():
    print('Задание 2')
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
        res = optimize.linprog([4, 4, 15], [[-2, -1, -3], [0, 0, -3], [-3, 1, -6], [-1, -2, -3],
                                           [0, -3, -6]], [-8, -1, 3, 0, 0])
        print(res)
