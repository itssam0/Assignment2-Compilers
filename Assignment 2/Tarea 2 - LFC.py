def parse_input(file_content):
    index = 0
    num_cases = int(file_content[index].strip())
    index += 1
    cases = []

    for _ in range(num_cases):
        k, m = map(int, file_content[index].strip().split())
        index += 1

        productions = {}
        for _ in range(k):
            line = file_content[index].strip()
            non_terminal, *derivations = line.split()
            productions[non_terminal] = derivations
            index += 1

        strings = []
        for _ in range(m):
            strings.append(file_content[index].strip())
            index += 1

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

# Usar estas funciones para cargar y procesar datos
file_content = [
    '4\n',
    '5 5\n',
    'S AB BA SS AC BD\n',
    'C SB\n',
    'D SA\n',
    'A a\n',
    'B b\n',
    'aabbab\n',
    'aabb\n',
    'ab\n',
    'aa\n',
    'b\n',
    '4 3\n',
    'S AB AC SS\n',
    'C SB\n',
    'A a\n',
    'B b\n',
    'abab\n',
    'aaabbbaabbab\n',
    'aabab\n',
    '2 6\n',
    'S AS b\n',
    'A a\n',
    'ab\n',
    'aaaaaaaa\n',
    'aaaaaaaaaaab\n',
    'b\n',
    'bb\n',
    'abb\n',
    '3 3\n',
    'S aSc AB\n',
    'A aAb ab\n',
    'B bBc bc\n',
    'aabbbbcc\n',
    'aaabbbbbbccc\n',
    'abc\n'

]
cases = parse_input(file_content)

results = []
for productions, strings in cases:
    results_case = []
    for string in strings:
        result = cky_algorithm(productions, string)
        results_case.append(result)
    results.append(results_case)

results
