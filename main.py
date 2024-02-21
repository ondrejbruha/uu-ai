from cells import population_script

if __name__ == '__main__':
    history = population_script().steps
    for step in history:
        for cell in step.get_cells():
            print(cell.get_str())

