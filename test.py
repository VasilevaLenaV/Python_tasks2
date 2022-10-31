# 1) Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# *Пример:*
# - 6782 -> 23
# - 0,56 -> 11

def is_int(c):
    try:
        int(c)
        return True
    except ValueError:
        return False


def func(y):
    x = [str(a) for a in str(y)]
    return x


def sum(arr):
    sum_num = 0
    for i in arr:
        if is_int(i):
            sum_num = sum_num + int(i)
    return sum_num


num = func(input("Задача 1. Введите вещественное число: "))
print(sum(num))


# 2) Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# *Пример:*
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def func(n):
    return range(1, n+1)   # создает массив


def mult(r):  # массив с набором произведений чисел
    arr = [''] * len(r)
    x = 1
    for i in r:
        x *= i
        arr[i-1] = str(x)
    return arr


m = int(input("Задача 2. Введите число: "))
y = func(m)
s = ","
print(f"[{s.join(mult(y))}]")


# 3) Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.
# *Пример:*
#     Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}
#     Сумма 9.06

def get_list(N):
    return list(formula(d) for d in range(1, N+1))


def formula(a):
    return (1 + 1/a) ** a


def summa(s):
    sum = 0
    for i in get_list(s):
        sum += i
    return sum


n = int(input("Задача 3. Введите число: "))
print(f"Сумма {summa(n):.2f}")


# 4) Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции вводятся с клавиатуры .

from random import randint


def get_list(N):
    return [randint(-N, N) for c in range(1, N+1)]


def mult(n_element, positions):
    list_n = get_list(n_element)
    print(list_n)
    mult_element = 1
    for i in positions:
        if len(list_n) < int(i):
            continue
        mult_element *= list_n[int(i)-1]
    return mult_element


n = int(input("Задача 4. Введите число: "))
index = (input("Введите индекс: ")).split(",")
print(mult(n, index))


# 5) Реализуйте алгоритм перемешивания списка.

import random


def get_list(n):
    return list(range(1, n + 1))


def get_mixlist(arr):
    llist = arr[:]
    for i in range(len(llist)):
        index_number = random.randint(0, len(llist) - 1)
        temp = llist[i]
        llist[i] = llist[index_number]
        llist[index_number] = temp
    return llist


N = int(input("Задача 5. Введите длину списка: "))

listN = get_list(N)
result = get_mixlist(listN)

print(f"Исходный список: {listN}")
print(f"Перемешанный список: {result}")