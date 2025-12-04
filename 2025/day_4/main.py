# (a + b) % 10
# (a - b) % 10
# range 0-9


def decode_santa_pin(code: str) -> str:
    strn = []
    lstr = "".join(c for c in code if c not in "[]")

    i = 0
    while i < len(lstr):
        if lstr[i].isalnum():
            num = int(lstr[i])
            i += 1

            add = 0
            sub = 0

            while i < len(lstr) and lstr[i] == "+":
                add += 1
                i += 1
            while i < len(lstr) and lstr[i] == "-":
                sub += 1
                i += 1

            result = (num + add - sub) % 10
            strn.append(str(result))

        elif lstr[i] == "<":
            if strn:
                strn.append(strn[-1])
            i += 1

    result = "".join(strn)
    return result if len(result) == 4 else None


"""
1 + +
0 1 2  
code[0].isalnum() == true, op = 1
if char == "+":
    while code[3] == "+":
        add += "+"
        continue

"""


if __name__ == "__main__":
    # decode_santa_pin("[1++]")
    # decode_santa_pin("[2-]")
    # decode_santa_pin("[3+]")
    # decode_santa_pin("[4+][<]")
    print(decode_santa_pin("[1++][2-][3+][<]"))
    print(decode_santa_pin("[9+][0-][4][<]"))
    print(decode_santa_pin("[1+][2-]"))
