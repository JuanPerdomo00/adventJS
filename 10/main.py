# Los elfos programadores están creando un pequeño ensamblador mágico para controlar las máquinas del taller de Santa Claus.
#
# Para ayudarles, vamos a implementar un intérprete sencillo que soporte las siguientes instrucciones mágicas:
#
#    MOV x y: Copia el valor x (puede ser un número o el contenido de un registro) en el registro y
#    INC x: Incrementa en 1 el contenido del registro x
#    DEC x: Decrementa en 1 el contenido del registro x
#    JMP x y: Si el valor del registro x es 0 entonces salta a la instrucción en el índice y y sigue ejecutándose el programa desde ahí.
#
# Comportamiento esperado:
#
#    Si se intenta acceder, incrementar o decrementar a un registro que no ha sido inicializado, se tomará el valor 0 por defecto.
#    El salto con JMP es absoluto y lleva al índice exacto indicado por y.
#    Al finalizar, el programa debe devolver el contenido del registro A. Si A no tenía un valor definido, retorna undefined.

# import re


# def compile(instructions):
#    glb = {}
#    ip = 0
#    while ip < len(instructions):
#        instruction = instructions[ip]
#        types = re.findall(
#            r"^\s*(MOV|INC|DEC|JMP)\s+(-?\d+|[A-Za-z]+)\s*([A-Za-z0-9]*)\s*$",
#            instruction,
#        )
#
#        if not types:
#            ip += 1
#            continue
#
#        commd, argone, argtwo = types[0]
#
#        if commd == "MOV":
#            if argtwo:
#                glb[argtwo] = (
#                    int(argone)
#                    if argone.isdigit() or (argone[0] == "-" and argone[1:].isdigit())
#                    else glb.get(argone, 0)
#                )
#
#        elif commd == "INC":
#            if argone in glb:
#                glb[argone] += 1
#            else:
#                glb[argone] = 1
#
#        elif commd == "DEC":
#            if argone in glb:
#                glb[argone] -= 1
#            else:
#                glb[argone] = -1
#
#        elif commd == "JMP":
#            if argone in glb and glb[argone] == 0:
#                ip = int(argtwo)
#                continue
#
#        ip += 1
#
#    return glb.get("A", "undefined")


import re


def compile(instructions):
    glb = {}
    n_instructions = len(instructions)
    i = 0

    while i < n_instructions:
        instruction = instructions[i]

        # Verificar formato de la instrucción
        types = re.findall(
            r"^\s*(MOV|INC|DEC|JMP)\s+(-?\d+|[A-Za-z]+)\s*([A-Za-z0-9]*)\s*$",
            instruction,
        )

        if types:
            command, argone, argtwo = types[0]

            if command == "MOV":
                glb[argtwo] = (
                    int(argone)
                    if argone.isdigit() or (argone[0] == "-" and argone[1:].isdigit())
                    else glb.get(argone, 0)
                )
            elif command == "INC":
                glb[argone] = glb.get(argone, 0) + 1
            elif command == "DEC":
                glb[argone] = glb.get(argone, 0) - 1
            elif command == "JMP":
                if glb.get(argone, 0) == 0:
                    i = int(argtwo)
                    continue
        else:
            command, *operands = instruction.split()
            dest = operands[-1]
            if command == "MOV":
                source = operands[0]
                try:
                    value = int(source)
                except ValueError:
                    value = glb.get(source, 0)
                glb[dest] = value
            elif command == "INC":
                glb[dest] = glb.get(dest, 0) + 1
            elif command == "DEC":
                glb[dest] = glb.get(dest, 0) - 1
            elif command == "JMP":
                source, value = operands
                if glb.get(source, 0) == 0:
                    i = int(value)
                    continue

        i += 1

    return glb.get(
        "A", None
    )  # if "A" in glb else undefined <- the test pass with this????:


if __name__ == "__main__":
    instructions = [
        "MOV -1 C",  # copia -1 al registro 'C'
        "INC C",  # incrementa el valor del registro 'C'
        "JMP C 1",  # salta a la instrucción en el índice 1 si 'C' es 0
        "MOV C A",  # copia el registro 'C' al registro 'A'
        "INC A",  # incrementa el valor del registro 'A'
    ]

    instructionstwo = ["MOV 0 A", "INC A"]
    instructionsthree = [
        "INC A",
        "INC A",
        "DEC A",
        "MOV A B",
    ]
    instructionsfour = ["MOV 5 B", "DEC B", "MOV B A", "INC A"]

    print(compile(instructions))  # 2
    print(compile(instructionstwo))  # 1
    print(compile(instructionsthree))  # 1
    print(compile(instructionsfour))  # 5
    print(
        compile(
            [
                "INC C",
                "DEC B",
                "MOV C Y",
                "INC Y",
            ]
        )
    )  # undefined

    print(compile(["MOV 2 X", "DEC X", "DEC X", "JMP X 1", "MOV X A"]))  # -2

    print(compile(["MOV 3 C", "DEC C", "DEC C", "DEC C", "JMP C 3", "MOV C A"]))  # -1
