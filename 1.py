'''
1. Сформувати функцію, що буде обчислювати факторіал заданого користувачем
натурального числа n.
'''
def factorial(x):
    if x < 0:
        raise ValueError('Error')
    if x == 0:
        return 1
    else:
        return x * factorial(x - 1)
n = int(input("your num is "))
print(factorial(n))