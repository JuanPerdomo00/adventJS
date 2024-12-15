# Los renos necesitan moverse para ocupar los establos,
# pero no puede haber más de un reno por establo.
# Además, para que los renos estén cómodos,
# debemos minimizar la distancia total que recorren para acomodarse.
#
# Tenemos dos parámetros:
#
#    reindeer: Un array de enteros que representan las posiciones de los renos.
#    stables: Un array de enteros que representan las posiciones de los establos.
#
# Hay que mover cada reno, desde su posición actual, hasta un establo. 
# Pero hay que tener en cuenta que sólo puede haber un reno por establo.
#
# Tu tarea es calcular el mínimo número de movimientos necesarios para que todos los renos acaben en un establo.
#
# Nota: Ten en cuenta que el array de establos siempre tendrá el mismo tamaño que el array de renos y que siempre los establos serán únicos.


def min_moves_to_stables(reindeer, stables):
    # Code here
    reindeer = sorted(reindeer)
    stables = sorted(stables)
    return sum([abs(stables[i] - reindeer[i]) for i in range(len(reindeer))])

if __name__ == "__main__":
    print(min_moves_to_stables([2, 6, 9], [3, 8, 5]))  # 3
    print(min_moves_to_stables([1, 1, 3], [1, 8, 4]))  # 8
