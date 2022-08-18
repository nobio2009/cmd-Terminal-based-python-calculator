import os, time

def cmath():
    os.system('cls')
    print(eval(input('Maths: ')))
    time.sleep(2)
    os.system('cls')
    math()

def math():
    inputmethod=input('Please choose method\n1=+ 2=- 3=/ 4=* 5=Custom\n')
    if inputmethod=='1':
        num1=input('Pleas input num 1\n')
        num2=input('Pleas input num 2\n')
        print('\n\n')
        print(int(num1) + int(num2))
        time.sleep(2)
        os.system('cls')
        math()
    elif inputmethod=='2':
        num1=input('Pleas input num 1\n')
        num2=input('Pleas input num 2\n')
        print('\n\n')
        print(int(num1) - int(num2))
        time.sleep(2)
        os.system('cls')
        math()
    elif inputmethod=='3':
        num1=input('Pleas input num 1\n')
        num2=input('Pleas input num 2\n')
        print('\n\n')
        print(int(num1) / int(num2))
        time.sleep(2)
        os.system('cls')
        math()
    elif inputmethod=='4':
        num1=input('Pleas input num 1\n')
        num2=input('Pleas input num 2\n')
        print('\n\n')
        print(int(num1) * int(num2))
        time.sleep(2)
        os.system('cls')
        math()
    elif inputmethod=='5':
        cmath()
math()
