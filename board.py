"""
Rubik Flip Board Class
attributes:
cells: list that holds each cell and its attributes
size: the size of the board
"""
import math

import pygame

from cell import Cell


class Board:
    def __init__(self, rows: int, cols: int, surface_size: int, surface_color: tuple, grid_color: tuple):
        self.rows = rows
        self.cols = cols
        self.surface_size = surface_size
        self.surface_color = surface_color
        self.grid_color = grid_color
        self.cells = []
        self.surface = None
        self.square_size = None
        self.neighbors = {}
        self.first_turn = True

    def __repr__(self):
        return f'{self.__class__.__name__}(rows={self.rows}, columns={self.cols})'

    def add_cell(self, cell: Cell):
        self.cells.append(cell)

    def __len__(self):
        return len(self.cells)

    def populate_board(self):
        for row in range(self.rows):
            for col in range(self.cols):
                self.add_cell(Cell(row, col))

    def initialze(self):
        self.populate_board()
        self.draw_board()

    def print_cells(self):
        for cell in self.cells:
            print(f'Cell coords: {cell.get_pos()}\tCell color: {cell.get_color()}')

    def draw_grid(self, surface_size: int, square_size: int, surface: pygame.surface.Surface):
        for row in range(0, surface_size, square_size):
            for col in range(0, surface_size, square_size):
                rect = pygame.Rect(row, col, square_size, square_size)
                pygame.draw.rect(surface, self.grid_color, rect, 1)

    def draw_board(self):
        n = int(math.sqrt(len(self.cells)))
        self.square_size = self.surface_size // n
        surface_size = n * self.square_size
        self.surface = pygame.display.set_mode((surface_size, surface_size))
        self.surface.fill(self.surface_color)
        self.draw_grid(surface_size, self.square_size, self.surface)

    def update_board(self, x: int, y: int, color: tuple):
        rect = pygame.Rect(y * self.square_size + 10, x * self.square_size + 10, 100, 100)
        pygame.draw.rect(self.surface, color, rect, 0)

    def place(self, x: int, y: int):
        if self.color(x, y) == (0, 0, 0):
            return True
        return False

    def flip(self, old_x: int, old_y: int, new_x: int, new_y: int):
        old_cell_neighbors = self.cells[old_x * self.rows + old_y].neighbours()
        if (new_x, new_y) in old_cell_neighbors and \
                self.color(new_x, new_y) == (0, 0, 0) and \
                self.color(old_x, old_y) != (0, 0, 0):
            return True
        return False

    def color(self, x: int, y: int):
        return self.cells[x * self.rows + y].get_color()

    def neighbor_colors(self, neighbors: list):
        return \
            sum([1 if self.cells[cell[0] * self.rows + cell[1]].get_color() == (0, 0, 0) else 0 for cell in neighbors])

    def horizontal_terminal(self, first_x: int, first_y: int):
        second_x, second_y = first_x, first_y + 1
        third_x, third_y = first_x, first_y + 2
        if self.color(first_x, first_y) == self.color(second_x, second_y) and \
                self.color(first_x, first_y) == self.color(third_x, third_y):
            first_neighbors = self.cells[first_x * self.rows + first_y].neighbours()
            second_neighbors = self.cells[second_x * self.rows + second_y].neighbours()
            third_neighbors = self.cells[third_x * self.rows + third_y].neighbours()
            if self.neighbor_colors(first_neighbors) == 0 and \
                    self.neighbor_colors(second_neighbors) == 0 and \
                    self.neighbor_colors(third_neighbors) == 0:
                return True
            return False
        return False

    def vertical_terminal(self, first_x: int, first_y: int):
        second_x, second_y = first_x + 1, first_y
        third_x, third_y = first_x + 2, first_y
        if self.color(first_x, first_y) == self.color(second_x, second_y) and \
                self.color(first_x, first_y) == self.color(third_x, third_y):
            first_neighbors = self.cells[first_x * self.rows + first_y].neighbours()
            second_neighbors = self.cells[second_x * self.rows + second_y].neighbours()
            third_neighbors = self.cells[third_x * self.rows + third_y].neighbours()
            if self.neighbor_colors(first_neighbors) == 0 and \
                    self.neighbor_colors(second_neighbors) == 0 and \
                    self.neighbor_colors(third_neighbors) == 0:
                return True
            return False
        return False

    def forward_diag_terminal(self, first_x: int, first_y: int):
        second_x, second_y = first_x + 1, first_y + 1
        third_x, third_y = first_x + 2, first_y + 2
        if self.color(first_x, first_y) == self.color(second_x, second_y) and \
                self.color(first_x, first_y) == self.color(third_x, third_y):
            first_neighbors = self.cells[first_x * self.rows + first_y].neighbours()
            second_neighbors = self.cells[second_x * self.rows + second_y].neighbours()
            third_neighbors = self.cells[third_x * self.rows + third_y].neighbours()
            if self.neighbor_colors(first_neighbors) == 0 and \
                    self.neighbor_colors(second_neighbors) == 0 and \
                    self.neighbor_colors(third_neighbors) == 0:
                return True
            return False
        return False

    def back_diag_terminal(self, first_x: int, first_y: int):
        second_x, second_y = first_x + 1, first_y - 1
        third_x, third_y = first_x + 2, first_y - 2
        if self.color(first_x, first_y) == self.color(second_x, second_y) and \
                self.color(first_x, first_y) == self.color(third_x, third_y):
            first_neighbors = self.cells[first_x * self.rows + first_y].neighbours()
            second_neighbors = self.cells[second_x * self.rows + second_y].neighbours()
            third_neighbors = self.cells[third_x * self.rows + third_y].neighbours()
            if self.neighbor_colors(first_neighbors) == 0 and \
                    self.neighbor_colors(second_neighbors) == 0 and \
                    self.neighbor_colors(third_neighbors) == 0:
                return True
            return False
        return False

    def terminal_state(self):
        check_cells = [cell.get_pos() for cell in self.cells if cell.get_color() != (0, 0, 0)]
        horizontal = [(x, y) for (x, y) in check_cells if y == 0 or y == 1]
        vertical = [(x, y) for (x, y) in check_cells if x == 0 or x == 1]
        forward_diag = [(x, y) for (x, y) in check_cells if (x == 0 or x == 1) and (y == 0 or y == 1)]
        back_diag = [(x, y) for (x, y) in check_cells if (x == 0 or x == 1) and (y == 2 or y == 3)]
        horizontal_win = [(x, y) for (x, y) in horizontal if self.horizontal_terminal(x, y)]
        vertical_win = [(x, y) for (x, y) in vertical if self.vertical_terminal(x, y)]
        forward_diag_win = [(x, y) for (x, y) in forward_diag if self.forward_diag_terminal(x, y)]
        back_diag_win = [(x, y) for (x, y) in back_diag if self.back_diag_terminal(x, y)]
        if len(horizontal_win) > 0 or len(vertical_win) > 0 or len(forward_diag_win) > 0 or len(back_diag_win) > 0:
            return True
        return False

    def valid_flips(self, player_colors: list):
        cells = [cell.get_pos() for cell in self.cells if cell.get_color() == player_colors[0]
                 or cell.get_color() == player_colors[1]]
        neighbours = [cell.get_neighbours() for cell in cells]
        neighbours = [[(x, y) for (x, y) in neighbour if self.cells[x * self.rows + y].get_color() == (0, 0, 0)]
                      for neighbour in neighbours]
        valid_flips = {}
        for cell, neighbour_list in zip(cells, neighbours):
            valid_flips[cell] = neighbour_list

    def turn(self, place_coords: tuple, place_color: tuple, flip_from_coords: tuple = None,
             flip_to_coords: tuple = None, new_color: tuple = None):
        if self.first_turn:
            if self.place(place_coords[0], place_coords[1]):
                self.first_turn = False
                self.cells[place_coords[0] * self.rows + place_coords[1]].set_color(place_color)
                self.update_board(place_coords[0], place_coords[1], place_color)
                return True
            return False
        else:
            if self.flip(flip_from_coords[0], flip_from_coords[1], flip_to_coords[0], flip_to_coords[1]):
                print('----FLIP MOVE IS VALID----')
                if self.place(place_coords[0], place_coords[1]):
                    print('----PLACE MOVE IS VALID----')
                    self.cells[flip_from_coords[0] * self.rows + flip_from_coords[1]].set_color((0, 0, 0))
                    self.cells[flip_to_coords[0] * self.rows + flip_to_coords[1]].set_color(new_color)
                    self.update_board(flip_from_coords[0], flip_from_coords[1], (0, 0, 0))
                    self.update_board(flip_to_coords[0], flip_to_coords[1], new_color)
                    self.cells[place_coords[0] * self.rows + place_coords[1]].set_color(place_color)
                    self.update_board(place_coords[0], place_coords[1], place_color)
                    return True
                return False
            return False

    def clear_board(self):
        self.cells = [cell.set_color((0, 0, 0)) for cell in self.cells]
