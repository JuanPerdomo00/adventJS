from typing import List

def draw_rice(indices: List[int], length: int):
    lone, reindeer, spaces = (
        ["~"] * length,
        "r",
        [i for i in range(len(indices))][::-1],
    )
    race = [
        spaces[i] * " "
        + "".join(lone[: indices[i]] + [reindeer] + lone[indices[i] + 1 :])
        + f" /{i+1}"
        if indices[i] != 0
        else spaces[i] * " " + "".join(lone) + f" /{i+1}"
        for i in range(len(indices))
    ]
    return "\n".join(race)


if __name__ == "__main__":
    print(draw_rice([0, 5, -3], 10))

    #   ~~~~~~~~~~ /1
    #  ~~~~~r~~~~ /2 --> Pass
    # ~~~~~~~r~~ /3

    print(draw_rice([2, -1, 0, 5], 8))
    #    ~~r~~~~~ /1
    #   ~~~~~~~r /2
    #  ~~~~~~~~ /3
    # ~~~~~r~~ /4

    print(draw_rice([3, 7, -2], 12))
    #   ~~~r~~~~~~~~ /1
    #  ~~~~~~~~r~~~ /2
    # ~~~~~~~~~r~~ /3

    print(draw_rice([0, 0, 0], 6))
    #   ~~~~~~ /1
    #  ~~~~~~ /2
    # ~~~~~~ /3
