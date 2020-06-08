'''
2. Сформувати функцію для обчислення цифрового кореню натурального числа.
Цифровий корінь отримується наступним чином: необхідно скласти всі цифри заданого
числа, потім скласти всі цифри знайденої суми і повторювати процес до тих пір, поки
сума не буде дорівнювати однозначному числу, що і буде цифровим коренем заданого
числа.
'''

def root(n):
    sum = 0
    while n > 0:
        if n % 10 != 0:
            sum = sum + n % 10
            n = n // 10
    if sum > 9:
        return root(sum)
    else:
        return sum
x = int(input("n = "))
print(root(x))