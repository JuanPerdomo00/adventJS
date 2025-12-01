def remove_snow(s: str) -> str:
    # Code here
    # from collections import Counter

    # counts = Counter(s)
    # new = ""
    # for char in s:
    #    if counts[char] != 2:
    #        if char not in new:
    #            new += char
    # return new

    # Counter no mantiene el orden Xd
    new = []

    for char in s:
        if new and new[-1] == char:
            new.pop()
        else:
            new.append(char)

    return "".join(new)


if __name__ == "__main__":
    print(remove_snow("zxxzoz"))  # oz
    print(remove_snow("abcdd"))  # abc
    print(remove_snow("zzz"))  # z
    print(remove_snow("a"))  # a
    print(remove_snow("abbaca"))  # ca
