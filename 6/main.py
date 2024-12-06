def in_box(box):
    # search_gift = [i for i in box if "*" in i]

    # return (
    #    True
    #    if "*" in "".join(search_gift).strip()[1:-1]
    #    else False
    #    if "*" in box[0] or "*" in box[-1]
    #    else False
    # )
    # return ''.join(search_gift).strip()[1:-1]
    return any("*" in line[1:-1] for line in box[1:-1])


if __name__ == "__main__":
    print(in_box(["###", "#*#", "###"]))  # True

    print(in_box(["####", "#* #", "#  #", "####"]))  # True

    print(in_box(["*####", "#   #", "#   #*", "####"]))  # false

    print(in_box(["#####", "#   #", "#   #", "#   #", "#####"]))

    print(in_box(["#*#", "###", "###"]))

    print(in_box(["##*##", "#   #", "#   #", "#   #", "#####"]))
