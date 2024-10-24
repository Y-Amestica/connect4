import numpy as np

# Crear tablero
def create_board(rows, columns):
    return np.zeros((rows, columns))

# Colocar ficha
def drop_piece(board, row, col, piece):
    board[row][col] = piece

# Verificar si columna está disponible
def is_valid_location(board, col, row_count):
    return board[row_count-1][col] == 0

# Encontrar fila siguiente disponible en columna
def get_next_open_row(board, col, row_count):
    for r in range(row_count):
        if board[r][col] == 0:
            return r

# Verificar si hay un ganador
def winning_move(board, piece, row_count, column_count):
    # Verificar filas
    for r in range(row_count):
        for c in range(column_count - 3):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True
    # Verificar columnas
    for c in range(column_count):
        for r in range(row_count - 3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True
    # Verificar diagonales positivas
    for r in range(row_count - 3):
        for c in range(column_count - 3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True
    # Verificar diagonales negativas
    for r in range(row_count - 3):
        for c in range(3, column_count):
            if board[r][c] == piece and board[r+1][c-1] == piece and board[r+2][c-2] == piece and board[r+3][c-3] == piece:
                return True
    return False
