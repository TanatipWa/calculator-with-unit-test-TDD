operators = ['+', '-', '*', '/']

def isNumber(number_str):
    return number_str.replace('.', '', 1).isdigit()
def isInt(number_str):
    if (number_str.isdigit()): return True
    else: return False
def isOperator(operator):
    for op in operators:
        if (operator == op): return True
    return False
def isYN(YN):
    if (YN == 'Y' or YN == 'y' or YN == 'N' or YN == 'n'): return True
    return False

def add(x, y):
    ans = ((x * 10) + (y * 10)) / 10
    if (isInt(str(ans))): return int(ans)
    else: return ans
def minus(x, y): return x - y
def multipy(x, y): return x * y
def divi(x, y):
    if (y == 0 or y == 0.0): return 'ZeroDivisionError'
    return x / y

'''while True:
    print('---------- CALCULATER ----------')
    while True:
        number1_str = input('Enter frist number: ')
        if (isNumber(number1_str)):
            if (isInt(number1_str)): number1 = int(number1_str)
            else: number1 = float(number1_str)
            break
        else: print('!!!TRY AGAIN!!!')

    while True:
        number2_str = input('Enter second number: ')
        if (isNumber(number2_str)):
            if (isInt(number2_str)): number2 = int(number2_str)
            else: number2 = float(number2_str)
            break
        else: print('!!!TRY AGAIN!!!')

    while True:
        operator = input('Enter operator(+, -, *, /): ')
        if (isOperator(operator)): break
        else: print('!!!TRY AGAIN!!!')

    print('================================')

    if (operator == '+'): result = add(number1, number2)
    elif (operator == '-'): result = minus(number1, number2)
    elif (operator == '*'): result = multipy(number1, number2)
    elif (operator == '/'): result = divi(number1, number2)
        
    print('Rusult =', result)
    print('================================')

    while True:
        again = input('Again? (Y/n): ')
        if (isYN(again)): break
        else: print('!!!TRY AGAIN!!!')
    if (again == 'N' or again == 'n'): break
    print()'''