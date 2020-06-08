'''
3. Сформувати функцію для обчислення індексу максимального елемента масиву
 n*n, де 1<=n<=5.
'''

import random

def search(array, n, i=0, j=0, max_element=0, max_index=[0, 0]):
    if array[i][j] > max_element:
        max_element = array[i][j]
        max_index = [i, j]

    if ((i != n) and (j == n)):
        return search(array, n, i + 1, 0, max_element, max_index)
    if ((i == n) and (j == n)):
        return max_index
    return search(array, n, i, j + 1, max_element, max_index)

n = int(input("Enter size - "))
array = []
for i in range(n):
    tmp_array = [random.randint(0, 50) for k in range(n)]
    array.append(tmp_array)

print(search(array, n - 1))
print(array)
