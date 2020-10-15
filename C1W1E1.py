# Задание по программированию: Сумма цифр в строке
import sys

digit_string = sys.argv[1]  # sys.argv[0] - название самого скрипта 'C1W1E1.py'
print(sum([int(x) for x in digit_string]))  # вывод суммы цифр переданной строки
