import tkinter as tk
from tkinter import messagebox
from game import create_board, drop_piece, is_valid_location, get_next_open_row, winning_move
from ai import make_ai_move  # Importa la lógica de la IA

# Variables globales
turn = 1  # Jugador 1 empieza

def on_click(col, board, row_count, column_count, board_widgets, column_buttons):
    global turn

    # Movimiento del Jugador 1
    if turn == 1 and is_valid_location(board, col, row_count):
        row = get_next_open_row(board, col, row_count)
        drop_piece(board, row, col, turn)

        # Actualizar interfaz
        visual_row = row_count - 1 - row
        board_widgets[visual_row][col].config(bg="red")

        # Verificar si el Jugador 1 ganó
        if winning_move(board, turn, row_count, column_count):
            tk.messagebox.showinfo("Fin del juego", "¡Jugador 1 ha ganado!")
            if messagebox.askyesno("Reiniciar", "¿Quieres jugar otra vez?"):
                reset_game(board, row_count, column_count, board_widgets, column_buttons)
            else:
                for button in column_buttons:
                    button.config(state="disabled")
            return

        # Cambiar turno a la IA
        turn = 2
        window.after(1000, lambda: ai_turn(board, row_count, column_count, board_widgets, column_buttons))  # Espera un segundo antes de que la IA haga su movimiento

def ai_turn(board, row_count, column_count, board_widgets, column_buttons):
    global turn

    # Movimiento de la IA (turno 2)
    ai_row, ai_col = make_ai_move(board, row_count, column_count, turn)
    if ai_col is not None:
        visual_row = row_count - 1 - ai_row
        board_widgets[visual_row][ai_col].config(bg="blue")

        # Verificar si la IA ganó
        if winning_move(board, turn, row_count, column_count):
            tk.messagebox.showinfo("Fin del juego", "¡La IA ha ganado!")
            if messagebox.askyesno("Reiniciar", "¿Quieres jugar otra vez?"):
                reset_game(board, row_count, column_count, board_widgets, column_buttons)
            else:
                for button in column_buttons:
                    button.config(state="disabled")
            return

        # Cambiar turno de vuelta al Jugador 1
        turn = 1

def reset_game(board, row_count, column_count, board_widgets, column_buttons):
    global turn

    # Reiniciar tablero
    for r in range(row_count):
        for c in range(column_count):
            board_widgets[r][c].config(bg="green")
    board[:] = 0

    # Reactivar botones de columna
    for button in column_buttons:
        button.config(state="normal")

    turn = 1  # Jugador 1 empieza primero

# Iniciar el juego
def start_game():
    global window, turn

    # Crear ventana de juego
    window = tk.Tk()
    window.title("Conecta los 4")

    row_count, column_count = 6, 7  # Tamaño estándar del tablero
    board = create_board(row_count, column_count)
    board_widgets = [[None for _ in range(column_count)] for _ in range(row_count)]

    # Dibujar tablero
    for r in range(row_count):
        for c in range(column_count):
            cell = tk.Label(window, text=" ", width=12, height=6, borderwidth=3, relief="groove", bg="green")
            cell.grid(row=r, column=c)
            board_widgets[r][c] = cell

    # Crear botones de columna
    column_buttons = []
    for c in range(column_count):
        btn = tk.Button(window, text=f"Col {c + 1}", command=lambda c=c: on_click(c, board, row_count, column_count, board_widgets, column_buttons))
        btn.grid(row=row_count, column=c)
        column_buttons.append(btn)

    reset_button = tk.Button(window, text="Reiniciar Juego", command=lambda: reset_game(board, row_count, column_count, board_widgets, column_buttons), bg="yellow")
    reset_button.grid(row=row_count + 1, column=0, columnspan=column_count, pady=10)

    window.mainloop()

# Menú principal
main_window = tk.Tk()
main_window.title("Conecta los 4 - Menú Principal")

new_game = tk.Button(main_window, text="Nuevo Juego", command=start_game, font=("Arial", 14), width=20, height=2, bg="lightblue")
new_game.pack(pady=40)

main_window.mainloop()