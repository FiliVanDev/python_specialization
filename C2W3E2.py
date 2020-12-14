# Задание по программированию: Создание адаптера для класса
class MappingAdapter:  # Адаптер к обработчику
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def lighten(self, grid):
        self.adaptee.set_dim([len(grid[0]), len(grid)])
        self.adaptee.set_lights(
            (j, i)
            for i in range(0, len(grid))
            for j in range(len(grid[i]))
            if grid[i][j] == 1
        )
        self.adaptee.set_obstacles(
            (j, i)
            for i in range(0, len(grid))
            for j in range(len(grid[i]))
            if grid[i][j] == -1
        )
        return self.adaptee.generate_lights()
