# Los elfos están jugando con un tren 🚂 mágico que transporta regalos.
# Este tren se mueve en un tablero representado por un array de strings.
#
# El tren está compuesto por una locomotora (@), seguida de sus vagones (o),
# y debe recoger frutas mágicas (*) que le sirve de combustible. El movimiento del tren sigue las siguientes reglas:
#
# Recibirás dos parámetros board y mov.
#
# board es un array de strings que representa el tablero:
#
#    @ es la locomotora del tren.
#    o son los vagones del tren.
#    * es una fruta mágica.
#    · son espacios vacíos.
#
# mov es un string que indica el próximo movimiento del tren desde la cabeza del tren @:
#
#    'L': izquierda
#    'R': derecha
#    'U': arriba
#    'D': abajo.
#
# Con esta información, debes devolver una cadena de texto:
#
#   'crash': Si el tren choca contra los bordes del tablero o contra sí mismo.
#   'eat': Si el tren recoge una fruta mágica (*).
#   'none': Si avanza sin chocar ni recoger ninguna fruta mágica.


from typing import List, Literal


def move_train(
    board: List[str], mov: Literal["U", "D", "R", "L"]
) -> Literal["none", "crash", "eat"]:
    # Code here
    row, col = 0, 0
    for i, row in enumerate(board):
        if "@" in row:
            row, col = i, row.index("@")
            print(row, col)
            break

    match mov:
        case "U":
            row -= 1
        case "D":
            row += 1
        case "L":
            col -= 1
        case "R":
            col += 1

    if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
        return "crash"
    match board[row][col]:
        case "*":
            return "eat"
        case "·":
            return "none"
        case _:
            return "crash"


if __name__ == "__main__":
    board: List[str] = ["·····", "*····", "@····", "o····", "o····"]

    print(move_train(board, "U"))  # -> eat
    print(move_train(board, "D"))  # -> crash
    print(move_train(board, "L"))  # -> crash
    print(move_train(board, "R"))  # -> none
