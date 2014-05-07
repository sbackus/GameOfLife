
"""
  the following transitions occur:
  1. Any live cell with fewer than two live neighbours dies, as if caused by under-population.
  2. Any live cell with two or three live neighbours lives on to the next generation.
  3. Any live cell with more than three live neighbours dies, as if by overcrowding.
  4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
"""
def is_alive(alive, neighbors):
  """
    given a boolean for the alive state and a number of neighbors neighbors, is_alive returns 
    True if the cell lives and False if the cell dies or remains dead.
    >>> is_alive(True,1)
    False
    >>> is_alive(True,2)
    True
    >>> is_alive(True,3)
    True
    >>> is_alive(True,4)
    False
    >>> is_alive(False,3)
    True
    >>> is_alive(False,2)
    False
    >>> is_alive(False,4)
    False

  """
  if alive:
    return neighbors < 4 and neighbors > 1
  else:
    return neighbors == 3

"""
  given x and y coordinates, neighbors returns a list of tuple representing the coordinates of the neighbors
"""   
def neighbors(x,y):
  """
    >>> neighbors(5,5)
    [(4, 4), (4, 5), (4, 6), (5, 4), (5, 6), (6, 4), (6, 5), (6, 6)]
  """
  return [(x-1,y-1),(x-1,y),(x-1,y+1),(x,y-1),(x,y+1),(x+1,y-1),(x+1,y),(x+1,y+1)]

"""
  returns the number of neighbors for a cell on a board. between 0 and 8.
"""
def number_of_neighbors(cell, board):
  """
    >>> number_of_neighbors((1,1), [])
    0
    >>> number_of_neighbors((1,1), [(1,1)])
    0
    >>> number_of_neighbors((1,1), [(1,2)])
    1
    >>> number_of_neighbors((1,1), [(1,1), (1,2), (2,1)])
    2
  """
  return len(set(board) & set(neighbors(cell[0],cell[1])))

""" 
   next board takes a list of coordinates representing a game board
   and returns another list of coordinates for the next generation
"""
def next_board(board):
  """
    >>> small_line = [(1, 1), (1, 2)]
    >>> next_board(small_line)
    []
    >>> long_line = [(1,1),(1,2),(1,3)]
    >>> next_board(long_line)
    [(1, 2), (0, 2), (2, 2)]
    >>> u_shape = [(1, 1), (2, 2), (1, 3)]
    >>> next_board(u_shape)
    [(2, 2), (1, 2)]
  """
  next_board = []
  all_cells = []
  for cell in board:
    all_cells = set(all_cells) | set(neighbors(cell[0],cell[1]))
    if is_alive(True, number_of_neighbors(cell,board)):
      next_board.append(cell)
  dead_cells = (set(all_cells)-set(board))
  for cell in dead_cells:    
    if is_alive(False, number_of_neighbors(cell,board)):
      next_board.append(cell)
  return next_board

if __name__ == "__main__":
    import doctest
    doctest.testmod()
