def draw_tree(height, ornament, frequency):
    position = 1
    lines = []

    for row in range(1, height + 1):
        stars_count = 2 * row - 1
        spaces_left = height - row

        line = ' ' * spaces_left

        for _ in range(stars_count):
            if position % frequency == 0:
                line += ornament
            else:
                line += '*'
            position += 1

        lines.append(line.rstrip())

    trunk = ' ' * (height - 1) + '#'
    lines.append(trunk)

    return '\n'.join(lines)


"""
5 - 5 = 0
5 - 4 = 1
5 - 3 = 2
5 - 2 = 3
5 - 1 = 4

"""

if __name__ == "__main__":
    #     *
    #    o*o
    #   *o*o*
    #  o*o*o*o
    # *o*o*o*o*
    #     #

    print(draw_tree(5, 'o', 2))

    print(draw_tree(3, '@', 3))
    print(draw_tree(100, '🦀', 1))
