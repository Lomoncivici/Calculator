import math
print ('1)сложение')
print ('2)вычетание')
print ('3)умножение')
print ('4)деление')
print ('5)возведение в степень')
print ('6)возведение в квадрат')
print ('7)факториал')
print ('8)синус')
print ('9)косинус')
c = int (input('введите действие:'))
if c > 9 or c < 1:
    print('Ты Кирилл! ввёл (ввела) не то число!')
    exit()
a = float (input('введите первое число:'))
if c != 6 and c != 7 and c != 8 and c != 9:
    b = float (input('введите второе число:'))

if c == 1:
    print (f'итог::{a + b}')

if c == 2:
    print (f'итог:{a - b}')

if c == 3:
    print (f'итог:{a * b}')

if c == 4:
    print (f'итог:{a / b}')

if c == 5:
    print (f'итог:{a ** b}')

if c == 6:
    print (f'итог:{a ** 0.5}')

if c == 7:
    factorial = a
    for i in range(1,int (a)):
        factorial = factorial * i
    print(factorial)

if c == 8:
    print (f'итог:{math.sin (a)}')

if c == 9:
    print (f'итог:{math.cos (a)}')