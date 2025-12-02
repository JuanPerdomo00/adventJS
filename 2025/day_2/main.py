def manufacture_gifts(gifts_to_produce):
    return (
        "".join(
            f"{gift['toy']}," * gift["quantity"]
            for gift in gifts_to_produce
        )
        .rstrip(",")
        .split(",")
        if any(g["quantity"] > 0 for g in gifts_to_produce)
        else []
    )


if __name__ == "__main__":
    prd1 = [
        {"toy": "car", "quantity": 3},
        {"toy": "doll", "quantity": 1},
        {"toy": "ball", "quantity": 2},
    ]
    prd2 = [
        {"toy": "train", "quantity": 0},
        {"toy": "bear", "quantity": -2},
        {"toy": "puzzle", "quantity": 1},
    ]

    prd3 = []
    print(manufacture_gifts(prd1), len(manufacture_gifts(prd1)))
    print(manufacture_gifts(prd2), len(manufacture_gifts(prd2)))
    print(manufacture_gifts(prd3), len(manufacture_gifts(prd3)))
