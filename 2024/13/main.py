# Los elfos del Polo Norte han creado un robot 🤖 especial que ayuda a Papá Noel a distribuir regalos dentro de un gran almacén.
# El robot se mueve en un plano 2D y partimos desde el origen (0, 0).
#
# Queremos saber si, tras ejecutar una serie de movimientos, el robot vuelve a estar justo donde empezó.
#
# Las órdenes básicas del robot son:
#
#    L: Mover hacia la izquierda
#    R: Mover hacia la derecha
#    U: Mover hacia arriba
#    D: Mover hacia abajo
#
# Pero también tiene ciertos modificadores para los movimientos:
#
#    *: El movimiento se realiza con el doble de intensidad (ej: *R significa RR)
#    !: El siguiente movimiento se invierte (ej: R!L se considera como RR)
#    ?: El siguiente movimiento se hace sólo si no se ha hecho antes (ej: R?R significa R)
#
# Nota: Cuando el movimiento se invierte con ! se contabiliza el movimiento invertido y no el original.
# Por ejemplo, !U?U invierte el movimiento de U, por lo que contabiliza que se hizo el movimiento D pero no el U.
# Así !U?U se traduce como D?U y, por lo tanto, se haría el movimiento U final.
#
# Debes devolver:
#
#    true: si el robot vuelve a estar justo donde empezó
#    [x, y]: si el robot no vuelve a estar justo donde empezó, devolver la posición donde se detuvo


def is_robot_back(moves: str) -> bool | list[int]:
    origen = [0, 0]
    copy_origen = origen.copy()

    steps = {
        "L": lambda x, opt=0: x.__setitem__(0, x[0] - 1)
        if opt == 0
        else x.__setitem__(0, (x[0] - 1) + opt),
        "R": lambda x, opt=0: x.__setitem__(0, x[0] + 1)
        if opt == 0
        else x.__setitem__(0, (x[0] + 1) + opt),
        "U": lambda y, opt=0: y.__setitem__(1, y[1] + 1)
        if opt == 0
        else y.__setitem__(1, (y[1] + 1) + opt),
        "D": lambda y, opt=0: y.__setitem__(1, y[1] - 1)
        if opt == 0
        else y.__setitem__(1, (y[1] - 1) + opt),
    }

    executed_moves = set()
    previous_move = None
    i = 0

    while i < len(moves):
        move = moves[i]

        if move == "*":
            if i + 1 < len(moves) and moves[i + 1] in steps:
                steps[moves[i + 1]](copy_origen, opt=1)
                i += 1

        elif move == "!":
            if previous_move:
                print(previous_move)
                if previous_move == "L":
                    steps["R"](copy_origen)
                elif previous_move == "R":
                    steps["L"](copy_origen)
                elif previous_move == "U":
                    steps["D"](copy_origen)
                elif previous_move == "D":
                    steps["U"](copy_origen)

        elif move == "?":
            if previous_move not in executed_moves:
                if previous_move in steps:
                    steps[previous_move](copy_origen)
                    executed_moves.add(previous_move)

        elif move in steps:
            steps[move](copy_origen)
            executed_moves.add(move)
            previous_move = move

        i += 1

    return True if copy_origen == origen else copy_origen



def test():
    print(is_robot_back("R"), [1, 0])
    assert is_robot_back("R") == [1, 0]

    print(is_robot_back("RL"), True)
    assert is_robot_back("RL") == True

    print(is_robot_back("RLUD"), True)
    assert is_robot_back("RLUD") == True

    print(is_robot_back("*RU"), [2, 1])
    assert is_robot_back("*RU") == [2, 1]

    print(is_robot_back("R*U"), [1, 2])
    assert is_robot_back("R*U") == [1, 2]

    print(is_robot_back("LLL!R"), [-4, 0])
    assert is_robot_back("LLL!R") == [-4, 0]

    print(is_robot_back("R?R"), [1, 0])
    assert is_robot_back("R?R") == [1, 0]

    print(is_robot_back("U?D"), True)
    assert is_robot_back("U?D") == True

    print(is_robot_back("R!L"), [2, 0])
    assert is_robot_back("R!L") == [2, 0]

    print(is_robot_back("U!D"), [0, 2])
    assert is_robot_back("U!D") == [0, 2]

    print(is_robot_back("R?L"), True)
    assert is_robot_back("R?L") == True

    print(is_robot_back("U?U"), [0, 1])
    assert is_robot_back("U?U") == [0, 1]

    print(is_robot_back("*U?U"), [0, 2])
    assert is_robot_back("*U?U") == [0, 2]

    print(is_robot_back("U?D?U"), True)
    assert is_robot_back("U?D?U") == True

    # Ejemplos paso a paso:
    print(is_robot_back("R!U?U"), [1, 0])
    # 'R'  -> se mueve a la derecha
    # '!U' -> se invierte y se convierte en 'D'
    # '?U' -> se mueve arriba, porque no se ha hecho el movimiento 'U'
    assert is_robot_back("R!U?U") == [1, 0]

    print(is_robot_back("UU!U?D"), [0, 1])
    # 'U'  -> se mueve arriba
    # 'U'  -> se mueve arriba
    # '!U' -> se invierte y se convierte en 'D'
    # '?D' -> no se mueve, ya que ya se hizo el movimiento 'D'
    assert is_robot_back("UU!U?D") == [0, 1]


if __name__ == "__main__":
    test()
