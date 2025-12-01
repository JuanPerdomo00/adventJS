def filter_gifts(gifts: list[str]):
    return [g for g in gifts if "#" not in g]


if __name__ == "__main__":
    gifts1 = ['car', 'doll#arm', 'ball', '#train']
    gifts2 = ['#broken', '#rusty']
    print(filter_gifts(gifts1))
    print(filter_gifts(gifts2))
