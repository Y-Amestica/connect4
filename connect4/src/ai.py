import random
from game import is_valid_location, get_next_open_row, drop_piece, winning_move

def ai_move(board, row_count, column_count):
    valid_columns = [c for c in range(column_count) if is_valid_location(board, c, row_count)]
    
    # Estrategia simple: elegir una columna aleatoria
    if valid_columns:
        return random.choice(valid_columns)
    
    return None  # Si no hay columnas disponibles

def make_ai_move(board, row_count, column_count, turn):
    ai_col = ai_move(board, row_count, column_count)
    if ai_col is not None:
        row = get_next_open_row(board, ai_col, row_count)
        drop_piece(board, row, ai_col, turn)
        return row, ai_col  # Devuelve la fila y columna donde se colocó la ficha
    return None, None  # Si no hay movimiento válido
