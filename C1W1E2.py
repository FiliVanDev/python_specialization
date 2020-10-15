# Задание по программированию: Рисуем лестницу
import sys

n_steps = sys.argv[1]  # получаем количество ступеней

for i in range(1, n_steps + 1):
    print(
        (n_steps - i) * " " + i * "#"
    )  # выводим построчно (n_steps - i) пробелов и i #
