from sys import stdout


def createFrame(names):
    # Code here
    # ***************
    # * midu        *
    # * madeval     * -> Test Midu
    # * educalvolpz *
    # ***************
    #
    #
    # ***************
    # * midu        *
    # * madeval     * -> Jakepys
    # * educalvolpz *
    # ***************

    # big_str_inarr: int = len(max(names, key=len))
    # frame = [
    #     2 * "*" + big_str_inarr * "*" + 2 * "*",
    #     [f"* {i.ljust(big_str_inarr)} *" for i in names],
    #     2 * "*" + big_str_inarr * "*" + 2 * "*",
    # ]

    # print('\n'.join(frame))
    # Calcular el tamaño máximo de nombre

    # Refactor
    big_str_inarr: int = len(max(names, key=len))
    border = "*" * (big_str_inarr + 4)
    framed_names = [f"* {i.ljust(big_str_inarr)} *" for i in names]
    frame = [border] + framed_names + [border]
    return "\n".join(frame)


if __name__ == "__main__":
    print(createFrame(["midu", "madeval", "educalvolpz"]))
    print(createFrame(["a", "bb", "ccc", "dddd"]))
    print(createFrame(["Jakepys"]))
