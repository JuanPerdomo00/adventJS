def organizeShoes(shoes):
    # if len({i["size"] for i in shoes}) == 1:
    #    return [shoes[0]["size"]] * 2

    # container = {}
    # for shoe in shoes:
    #    ty, size = shoe.values()

    #    print(ty, size)
    sizes = {}
    for shoe in shoes:
        sizes.setdefault(shoe["size"], {"I": 0, "R": 0})[shoe["type"]] += 1
    return [
        size
        for size, types in sizes.items()
        for _ in range(min(types["I"], types["R"]))
    ]


if __name__ == "__main__":
    shoes = [
        {"type": "I", "size": 38},
        {"type": "R", "size": 38},
        {"type": "R", "size": 42},
        {"type": "I", "size": 41},
        {"type": "I", "size": 42},
    ]

    shoes2 = [
        {"type": "I", "size": 38},
        {"type": "R", "size": 38},
        {"type": "I", "size": 38},
        {"type": "I", "size": 38},
        {"type": "R", "size": 38},
    ]

    shoes3 = [
        {"type": "I", "size": 38},
        {"type": "R", "size": 36},
        {"type": "R", "size": 42},
        {"type": "I", "size": 41},
        {"type": "I", "size": 43},
    ]

    print(organizeShoes(shoes))  # [38, 42]
    print(organizeShoes(shoes2))  # [38, 38]
    print(organizeShoes(shoes3))  # []
