def parse_input():
    num_cases = int(input().strip())  # número de casos
    cases = []

    for _ in range(num_cases):
        k, m = map(int, input().strip().split())  # k (número de no terminales), m (número de cadenas a analizar)

        productions = {}
        for _ in range(k):
            line = input().strip()
            non_terminal, *derivations = line.split()
            productions[non_terminal] = derivations

        strings = []
        for _ in range(m):
            strings.append(input().strip())

        cases.append((productions, strings))

    return cases

def cky_algorithm(productions, string):
    n = len(string)
    table = [[set() for _ in range(n + 1)] for _ in range(n + 1)]

    # Paso 1: Rellenar la diagonal con los no terminales que pueden producir los símbolos de la cadena
    for i in range(n):
        for non_terminal, derivations in productions.items():
            if string[i] in derivations:
                table[i][i + 1].add(non_terminal)

    # Paso 2: Rellenar el resto de la tabla
    for length in range(2, n + 1):  # longitud de la subcadena
        for i in range(n - length + 1):
            j = i + length
            for k in range(i + 1, j):  # división de la subcadena
                for non_terminal, derivations in productions.items():
                    for derivation in derivations:
                        if len(derivation) == 2:
                            left, right = derivation[0], derivation[1]
                            if left in table[i][k] and right in table[k][j]:
                                table[i][j].add(non_terminal)

    # Si el símbolo inicial 'S' está en el conjunto superior derecho de la tabla, la cadena puede ser generada
    return 'yes' if 'S' in table[0][n] else 'no'


cases = parse_input()


for productions, strings in cases:
    for string in strings:
        result = cky_algorithm(productions, string)
        print(result)
