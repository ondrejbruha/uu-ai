import random


class Cell:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def set_x(self, x):
        self._x = x

    def set_y(self, y):
        self._y = y

    def move(self, x, y):
        self.set_x(x)
        self.set_y(y)

    def get_str(self):
        return f"Cell({self._x}, {self._y})"


class CellSet:
    def __init__(self):
        self.cells = []

    def add_cell(self, cell):
        self.cells.append(cell)

    def remove_cell(self, cell):
        self.cells.remove(cell)

    def get_cells(self):
        return self.cells

    def get_cell(self, index):
        return self.cells[index]

    def get_size(self):
        return len(self.cells)

    def init_set(self, num):
        for i in range(num):
            x = random.randint(0, 1000)
            y = random.randint(0, 1000)
            cell = Cell(x, y)
            self.add_cell(cell)


class RandomSimulation:
    def __init__(self, cell_num, step_num):
        self.steps = []
        for i in range(step_num):
            temp = CellSet()
            temp.init_set(cell_num)
            self.steps.append(temp)


class HistorySimulation:
    def __init__(self, cell_num, step_num):
        self.steps = []
        temp = CellSet()
        temp.init_set(cell_num)
        self.steps.append(temp)
        for i in range(step_num):
            temp = self.steps[i]
            cells = temp.get_cells()
            cell_set = CellSet()
            for cell in cells:
                x = cell.get_x() + random.randint(-2, 2)
                y = cell.get_y() + random.randint(-2, 2)
                cell.move(x, y)
                cell_set.add_cell(cell)
            self.steps.append(cell_set)


def population_script():
    simulation = HistorySimulation(10, 100)
    return simulation
