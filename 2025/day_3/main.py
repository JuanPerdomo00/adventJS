import os
import time


def draw_gift(size: int, symbol: str) -> str:
    border = symbol * size
    gift = [border]
    gift += [symbol + " " * (size - 2) + symbol] * (size - 2)
    gift += [border]
    return "\n".join(gift) if size >= 2 else "" if size == 1 else []


if __name__ == "__main__":
    for gf in range(1, 10):
        print(f"Size: {gf}")
        print(draw_gift(gf, '#'))

    colors = ["\033[90m", "\033[97m", "\033[96m", "\033[91m", "\033[94m"]
    res = "\033[00m"
    while False:
        terminal_width = os.get_terminal_size().columns

        for i in range(1, terminal_width + 1, 2):
            os.system("cls" if os.name == "nt" else "clear")
            # gift = draw_gift(i, f"{colors[i % len(colors)]}#{res}")
            gift = draw_gift(i, "#")

            for line in gift.split("\n"):
                print(line.center(terminal_width))

            time.sleep(0.01)
        time.sleep(0.1)
