def cell_exists(row, column, new_generation):
    return True if 0 <= row < len(new_generation) and 0 <= column < len(new_generation[row]) else False


def get_number_of_active_neighbors(row, column, new_generation):
    neighbors = [[-1, -1], [-1, 0], [-1, +1], [0, -1], [0, +1], [+1, -1], [+1, 0], [+1, +1]]
    return sum([new_generation[row + offset[0]][column + offset[1]] for offset in neighbors if
                cell_exists(row + offset[0], column + offset[1], new_generation)])


def set_cell_status(alive_neighbors, current_cell_status):
    return 1 if alive_neighbors == 3 else current_cell_status if alive_neighbors == 2 else 0


def remove_empty_first_row(new_generation):
    while not any(new_generation[0]):
        del new_generation[0]
    return new_generation


def remove_empty_last_row(new_generation):
    while not any(new_generation[-1]):
        del new_generation[-1]
    return new_generation


def remove_empty_boarders(new_generation):
    while sum([column[-1] for column in new_generation]) == 0:
        new_generation = [column[:-1] for column in new_generation]
    while sum([column[0] for column in new_generation]) == 0:
        new_generation = [column[1:] for column in new_generation]
    return new_generation


def add_empty_left_column(new_generation):
    return [[0] + column for column in new_generation]


def add_empty_right_column(new_generation):
    return [column + [0] for column in new_generation]


def add_empty_first_row(new_generation):
    expanded_array = [[0 for column in range(len(new_generation[0]))]] + new_generation
    return expanded_array


def add_empty_last_row(new_generation):
    expanded_array = new_generation + [[0 for column in range(len(new_generation[0]))]]
    return expanded_array


def create_next_generation(new_generation):
    next_generation = [[set_cell_status(get_number_of_active_neighbors(row, column, new_generation),
                                        new_generation[row][column])
                        for column in range(len(new_generation[row]))
                        if cell_exists(row, column, new_generation)]
                       for row in range(len(new_generation))]
    return next_generation


def get_generation(cells, generation):
    current_generation = remove_empty_first_row(remove_empty_last_row(remove_empty_boarders(create_next_generation(
        add_empty_last_row(add_empty_first_row(add_empty_right_column(add_empty_left_column(cells))))))))
    return current_generation if generation <= 1 else get_generation(current_generation, generation - 1)
