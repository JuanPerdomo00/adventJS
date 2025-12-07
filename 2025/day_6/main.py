from typing import List, Dict
from collections import Counter

# def match_gloves(gloves: List[Dict[str, str]]) -> List[str]:
#     aux = []
#     arr = []
#     i = 0
#     while i < len(gloves):
#         if len(aux) == 0:
#             aux.append(gloves[i]["hand"])
#             aux.append(gloves[i]["color"])

#         if aux[0] != gloves[i]["hand"] and gloves[i]["color"] == aux[1]:
#             arr.append(gloves[i]["color"])
#             del aux[0]
#             del aux[0]
#             del gloves[i]
#             continue

#         i += 1

#     return arr


def match_gloves(gloves: List[Dict[str, str]]) -> List[str]:
    count = Counter()
    for g in gloves:
        key = (g["hand"], g["color"])
        print(key)
        count[key] += 1

    pairs = []
    colors = set(g["color"] for g in gloves)
    print(colors)
    for color in colors:
        left = count[("L", color)]
        right = count[("R", color)]
        print(left, right)
        pairs.extend([color] * min(left, right))

    return pairs


if __name__ == "__main__":
    print(
        match_gloves(
            [
                {"hand": "L", "color": "red"},
                {"hand": "R", "color": "red"},
                {"hand": "R", "color": "green"},
                {"hand": "L", "color": "blue"},
                {"hand": "L", "color": "green"},
            ]
        )
    )

    # gloves2 = [
    #    {"hand": 'L', "color": 'gold'},
    #    {"hand": 'R', "color": 'gold'},
    #    {"hand": 'L', "color": 'gold'},
    #    {"hand": 'L', "color": 'gold'},
    #    {"hand": 'R', "color": 'gold'}
    # ]
#
# print(match_gloves(gloves2))

# gloves3 = [
#    {"hand": 'R', "color": 'green'},
#    {"hand": 'L', "color": 'red'},
#    {"hand": 'R', "color": 'red'},
#    {"hand": 'L', "color": 'green'}, #
#    {"hand": 'L', "color": 'red'}
# ]
##
# print(match_gloves(gloves3))
