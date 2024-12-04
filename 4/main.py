def createXmasTree(height, ornament):
    # Code here
    spaces = [i // 2 * "_" for i in range(1, height * 2, 2)][::-1]
    tree_blocks: list[str] = [ornament * i for i in range(1, height * 2, 2)]
    branchs = [spaces[i] + tree_blocks[i] + spaces[i] for i in range(len(tree_blocks))]
    trunk = [
        (len(max(branchs, key=len)) // 2) * "_"
        + i
        + "_" * (len(max(branchs, key=len)) // 2)
        for i in "##"
    ]

    return "\n".join(branchs + trunk[:-1]) + "\n" + trunk[-1]


if __name__ == "__main__":
    print(f"height: {5}, ornament: {'*'}")
    print(createXmasTree(5, "*"))
    print(f"height: {3}, ornament: {'+'}")
    print(createXmasTree(3, "+"))
    print(f"height: {4}, ornament: {'#'}")
    print(createXmasTree(4, "#"))
    print(f"height: {6}, ornament: {'@'}")
    print(createXmasTree(6, "@"))
    print(f"height: {1}, ornament: {'*'}")
    print(createXmasTree(1, "*"))

# Midu
# ____*____
# ___***___
# __*****__
# _*******_
# *********
# ____#____
# ____#____

# Jakepys
# ____*____
# ___***___
# __*****__
# _*******_
# *********
# ____#____
# ____#____
