board = [
      [7, 8, 0, 4, 0, 0, 1, 2, 0],
      [6, 0, 0, 0, 7, 5, 0, 0, 9],
      [0, 0, 0, 6, 0, 1, 0, 7, 8],
      [0, 0, 7, 0, 4, 0, 2, 6, 0],
      [0, 0, 1, 0, 5, 0, 9, 3, 0],
      [9, 0, 4, 0, 6, 0, 0, 0, 5],
      [0, 7, 0, 3, 0, 0, 0, 1, 2],
      [1, 2, 0, 0, 0, 7, 4, 0, 0],
      [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

def solve(b):

      find = find_empty(b)
      if not find:
            return True
      else:
            row, col = find 

      for i in range(1, 10):
            if valid(b, i, (row, col)):
                  b[row][col] = i

                  if solve(b):
                        return True

                  b[row][col] = 0

      return False

def valid(b, num, pos):
      
      for i in range(len(b[0])):
            if b[pos[0]][i] == num and pos[1] != i:
                  return False

      for i in range(len(b)):
            if b[i][pos[1]] == num and pos[0] != i:
                  return False

      box_x = pos[1] // 3
      box_y = pos[0] // 3

      for i in range(box_y * 3, box_y * 3 + 3):
            for j in range(box_x * 3, box_x * 3 + 3):
                  if b[i][j] == num and (i,j) != pos:
                        return False

      return True

def print_board(b):
    for i in range(len(b)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - -")


        for j in range(len(b[0])):
            if j % 3 == 0 and j != 0:
                    print (" | ", end="")


            if j == 8:
                    print(b[i][j])
            else:
                    print(str(b[i][j]) + " ", end="")

def find_empty(b):
      for i in range(len(b)):
            for j in range(len(b[0])):
                  if b[i][j] == 0:
                        return (i, j)

      return None           

print_board(board)
solve(board)
print("___________________")
print_board(board)