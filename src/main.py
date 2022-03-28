from copy import deepcopy

"""
Função main, onde o arquivo começa a ser interpretado
"""
def main():
    try:
        matrix_01 = [
            [2, 1, 6, 2],
            [3, 4, 9, 0],
            [2, 0, -5, 10],
            [4, -2, -7, 1],
        ]

        result = inverse(matrix_01)

        print(result)
    except Exception as ex:
        print(f'Ocorreu o seguinte erro: {ex}')

"""
Calcula a matrix identidade da matriz informada.
"""
def identity(matrix):
    matrix_lines_length, _ = matrix_order(matrix)

    for line_index in matrix:
        if len(line_index) != matrix_lines_length:
            raise Exception('A matriz deve ser quadrada')

    indentity_matrix = []

    for line_index in range(0, len(matrix)):
        indentity_matrix.append([])

        for column_index in range(0, len(matrix)):
            if line_index == column_index:
                indentity_matrix[line_index].append(1)
            else:
                indentity_matrix[line_index].append(0)

    return indentity_matrix

"""
Calcula a matrix inversa da matriz informada.
"""
def inverse(matrix):
    if determinant(matrix) == 0:
        raise Exception('O determinante da matriz informada é 0, portanto ela não possui inversa')

    copied_matrix = deepcopy(matrix)
    indentity_matrix = identity(copied_matrix)

    return indentity_matrix

"""
Particiona a matriz informada através do índice da linha e da coluna informadas.
Utilizada para obter a matriz reduzida para o cálculo do determinante por meio de Laplace.
"""
def sliced_matrix(matrix, line_index, column_index):
    # Utilizei a função "deepcopy" para poder copiar o conteúdo que está endereço de memória da matriz original para um novo endereço de memória (o da matrix reduzida), não afetando assim os valores da matriz original.
    new_sliced_matrix = deepcopy(matrix)

    new_sliced_matrix.remove(matrix[line_index])

    for new_column_index in range(len(new_sliced_matrix)):
        new_sliced_matrix[new_column_index] \
            .remove(new_sliced_matrix[new_column_index][column_index])

    return new_sliced_matrix

"""
Calcula o determinante da matriz informada por meio dos cofatores (Laplace) caso sua ordem for >= 3.
Caso contrário fará o cálculo por meio da regra de Sarrus.
"""
def determinant(matrix):
    matrix_lines_length, matrix_columns_length = matrix_order(matrix)

    for line_index in matrix:
        if len(line_index) != matrix_lines_length:
            raise Exception('A matriz deve ser quadrada')

    if matrix_lines_length == 2:
        two_order_matrix_determinant = matrix[0][0] * matrix[1][1] - \
            matrix[0][1] * matrix[1][0]

        return two_order_matrix_determinant

    high_order_matrix_determinant = 0

    for column_index in range(matrix_columns_length):
        cofactor = (-1) ** (0 + column_index) * \
            matrix[0][column_index] * determinant(sliced_matrix(matrix, 0, column_index))

        high_order_matrix_determinant += cofactor

    return high_order_matrix_determinant

"""
Multiplica as duas matrizes informadas através de três laços de repetição encadeados.
A rotina cria novas linhas zeradas e vai adicionando colunas zeradas na mesma, previamente às somas das multiplicações.
"""
def multiplication(a, b):
    a_lines_length, a_columns_length = matrix_order(a)
    b_lines_length, b_columns_length = matrix_order(b)

    if a_columns_length != b_lines_length:
        raise Exception('A matriz "A" possui uma quantidade de linhas diferentes da quantidade de colunas da matriz "B"')

    c = []

    for a_line_index in range(a_lines_length):
        empty_line = []
        c.append(empty_line)

        for b_column_index in range(b_columns_length):
            c[a_line_index].append(0)

            for counter in range(a_columns_length):
                c[a_line_index][b_column_index] += a[a_line_index][counter] * b[counter][b_column_index]

    return c

"""
Retorna a ordem da matrix informada.
"""
def matrix_order(matrix):
    matrix_lines_length = len(matrix)
    matrix_columns_length = len(matrix[0])

    return matrix_lines_length, matrix_columns_length

"""
Soma as duas matrizes informadas através de dois laços de repetição encadeados.
A rotina cria novas linhas zeradas previamente às somas.
"""
def sum(a, b):
    a_lines_length, a_columns_length = matrix_order(a)
    b_lines_length, b_columns_length = matrix_order(b)

    if a_lines_length != b_lines_length or a_columns_length != b_columns_length:
        raise Exception('As matrizes informadas possuem ordens diferentes')

    c = []

    for line_index in range(a_lines_length):
        empty_line = [0] * a_columns_length
        c.append(empty_line)

        for column_index in range(a_columns_length):
            c[line_index][column_index] = a[line_index][column_index] + \
                b[line_index][column_index]

    return c

"""
Substrai as duas matrizes informadas através de dois laços de repetição encadeados.
A rotina cria novas linhas zeradas previamente às subtrações.
"""
def subtraction(a, b):
    a_lines_length, a_columns_length = matrix_order(a)
    b_lines_length, b_columns_length = matrix_order(b)

    if a_lines_length != b_lines_length or a_columns_length != b_columns_length:
        raise Exception('As matrizes informadas possuem ordens diferentes')

    c = []

    for line_index in range(a_lines_length):
        empty_line = [0] * a_columns_length
        c.append(empty_line)

        for column_index in range(a_columns_length):
            c[line_index][column_index] = a[line_index][column_index] - \
                b[line_index][column_index]

    return c


if __name__ == "__main__":
    main()
