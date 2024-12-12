# Estás en un mercado muy especial en el que se venden árboles de Navidad 🎄.
# Cada uno viene decorado con una serie de adornos muy peculiares,
# y el precio del árbol se determina en función de los adornos que tiene.
#
#    *: Copo de nieve - Valor: 1
#    o: Bola de Navidad - Valor: 5
#    ^: Arbolito decorativo - Valor: 10
#    #: Guirnalda brillante - Valor: 50
#    @: Estrella polar - Valor: 100
#
# Normalmente se sumarían todos los valores de los adornos y ya está…
#
# Pero, ¡ojo! Si un adorno se encuentra inmediatamente a la izquierda de otro de mayor valor,
# en lugar de sumar, se resta su valor.


def calculate_price(ornaments: str) -> int | None:
    # Code here
    obj_ornaments = {"*": 1, "o": 5, "^": 10, "#": 50, "@": 100}
    order_ornamets = [obj_ornaments[orn] for orn in ornaments if orn in obj_ornaments]
    if any(i not in obj_ornaments for i in ornaments):
        return None
    return sum(
        [
            -v if i < len(order_ornamets) - 1 and v < order_ornamets[i + 1] else v
            for i, v in enumerate(order_ornamets)
        ]
    )


if __name__ == "__main__":
    print(calculate_price("***"))  # 3   (1 + 1 + 1)
    print(calculate_price("*o"))  # 4   (5 - 1)
    print(calculate_price("o*"))  # 6   (5 + 1)
    print(calculate_price("*o*"))  # 5   (-1 + 5 + 1)
    print(calculate_price("#@Z"))  # None
