import numpy as np
from tabulate import tabulate
print("Генератор Геффе\n")

def gen_fib(i):
    print(f'РСЛОС {i + 1}')
    N = int(input("N = "))
    Fx = [0] * N
    print("Ф(x):")
    for i in range(N):
        Fx[i] = int(input(f"a{i + 1} = "))
    print("Ф(x) =", Fx)
    k = int(input("k = "))

    T = [Fx]
    for i in range(N - 1):
        T.append([0] * N)
        T[-1][i] = 1
    T = np.array(T)
    #print(f"T = \n{T}")

    if k == 1:
        V = T
    else:
        V = T @ T
        for i in range(k - 2):
            V = V @ T

    #print(f"V = \n{V}\n")

    Diag = []
    Diag.append(input('Начальное состояние: ').split())
    for i in range(len(Diag[0])):
        Diag[0][i] = int(Diag[0][i])

    s = []
    p = 0
    for i in range(len(V)):
        for j in range(len(V[i])):
            if V[i][j] % 2 == 1:
                p += Diag[-1][j]
        if p % 2 == 0:
            s.append(0)
        else:
            s.append(1)
        p = 0
    Diag.append(s)

    while Diag[0] != Diag[-1]:
        s = []
        p = 0
        for i in range(len(V)):
            for j in range(len(V[i])):
                if V[i][j] % 2 == 1:
                    p += Diag[-1][j]
            if p % 2 == 0:
                s.append(0)
            else:
                s.append(1)
            p = 0
        Diag.append(s)
    Diag = np.array(Diag)
    #print("Диаграмма состояний:")
    #for i in range(len(Diag)):
    #    print(Diag[i])
    #print(f"Период - {len(Diag) - 1}\n")
    Diag = list(Diag)
    del Diag[-1]
    Diag = np.array(Diag)
    period.append(len(Diag))

    q = []
    for i in range(N):
        q.append(Diag[:, i])
        #print(f"q{i} = {Diag[:, i]}")

    r = [0]
    R = ""
    for i in range(len(Diag)):
        st = ""
        for j in range(len(r)):
            st += str(Diag[i][r[j]])
        st = st.replace("[", "")
        st = st.replace("]", "")
        st = st.replace(" ", "")
        st = ''.join(reversed(st))
        R += str(int(st, 2))
        #print(st, "=", int(st, 2))

    #print("Результат:", R)
    return R

period = []
kolv = int(input('Количество РСЛОС: '))
fib = []
for i in range(kolv):
    R = gen_fib(i)
    print('Результат:', R, '\n')
    fib.append(R)
print('Результат многочленов:')
for i in range(len(fib)):
    print(fib[i])

print('\nБулевая функция генератора')
ch = int(input('Количество членов: '))
fx123 = []
print('Значения членов:')
for i in range(ch):
    fx123.append(input().split())

viv = 'f('
for i in range(kolv):
    if i != kolv - 1:
        viv += f'x{i + 1},'
    else:
        viv += f'x{i + 1}) = '
for i in range(len(fx123)):
    for j in range(len(fx123[i])):
        fx123[i][j] = int(fx123[i][j])
        if j != len(fx123[i]) - 1:
            viv += f'x{fx123[i][j]}∙'
        else:
            viv += f'x{fx123[i][j]}'
    if i != len(fx123) - 1:
        viv += " ⊕ "
print(viv)

dlp = 'L = '
for i in range(kolv):
    if i != kolv - 1:
        dlp += f'S{i + 1} ∙ '
    else:
        dlp += f'S{i + 1} = '
L = 1
for i in range(len(period)):
    L *= period[i]
    if i != kolv - 1:
        dlp += f'{period[i]} ∙ '
    else:
        dlp += f'{period[i]} = {L}'
print(dlp)

head = []
for i in range(kolv):
    head.append(f'x{i + 1}')
head.append('f')

for i in range(len(fib)):
    fib[i] = fib[i] * (int(L / period[i]))

table = []
fun = ''
while len(fib[-1]) != 0:
    table.append([])
    for i in range(len(fib)):
        table[-1].append(fib[i][0])
        fib[i] = fib[i][1:]
        if i == len(fib) - 1:
            F = []
            for j in range(len(fx123)):
                f = 1
                for k in range(len(fx123[j])):
                    f *= int(table[-1][fx123[j][k] - 1])
                F.append(f)
            F1 = 0
            for j in range(len(F)):
                F1 += F[j]
            if F1 % 2 == 0:
                F1 = '0'
            else:
                F1 = '1'
            table[-1].append(F1)
            fun += F1

print(tabulate(table, headers=head))
print(f'f - {fun}')
print(f'f - {int(fun, 2)}')
'''
P = str(int(fun, 2)) * 93
print(len(P))
file_name = "C:\\Users\\Дмитрий\\OneDrive\\Рабочий стол\\ТПГ\\test4.txt"
with open(file_name, 'w', encoding='utf8') as file:
    file.write(P)
'''