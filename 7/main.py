def fix_packages(packages):
    pila = []
    for char in packages:
        if char == ")":
            temp = []
            while pila and pila[-1] != "(":
                temp.append(pila.pop())
            pila.pop()
            pila.extend(temp)
        else:
            pila.append(char)

    return "".join(pila)


if __name__ == "__main__":
    print("========================")
    print(f"paquete: {'a(cb)de'}")
    print(fix_packages("a(cb)de"))  # ➞ "abcde"

    print("========================")

    print(f"paquete: {'a(bc(def)g)h'}")
    print(fix_packages("a(bc(def)g)h"))

    print("=========================")
    print(f"paquete: {'abc(def(gh)i)jk'}")
    print(fix_packages("abc(def(gh)i)jk"))

    print("=========================")
    print(f"paquete: {'a(b(c))e'}")
    print(fix_packages("a(b(c))e"))
    print("========================")
