from copy import deepcopy
import math

"""
Função main, onde o arquivo começa a ser interpretado
"""
def main():
    try:
        A = [
            [2, 1, 6, 2, 4],
            [3, 4, 9, 0, 4],
            [2, 0, -5, 10, 4],
            [4, -2, -7, 1, 4],
            [4, -2, -7, 1, 10],
        ]

        B = [
            [2, 1, 6, 2],
            [3, 4, 9, 0],
            [2, 0, -5, 10],
            [4, -2, -7, 1],
        ]

        C = [
            [2, 1, 6],
            [3, 4, 9],
            [2, 0, -5],
        ]

        D = [
            [2, 1],
            [3, 4],
        ]

        matrix = A

        det = determinant_validation(matrix, 1, 1)
        cof = cofactor(matrix)

        print(det, '\n')
        print(cof, '\n')
    except Exception as ex:
        print(f'Ocorreu o seguinte erro: {ex}')

"""
Calcula o determinante da matriz informada por meio dos cofatores (Laplace) caso sua ordem for >= 3.
Caso contrário fará o cálculo por meio da regra de Sarrus.
"""
def determinant_calculation(matrix):
    counter = 2
    determinant = 0

    matrix_lines_length, matrix_column_length = matrix_order(matrix)

    if matrix_lines_length == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    for line_index in range(0, matrix_column_length):
        # Utilizei a função "deepcopy" para poder copiar o conteúdo que está endereço de memória da matriz original para um novo endereço de memória (o da matrix reduzida), não afetando assim os valores da matriz original.
        copied_matrix = deepcopy(matrix)
        copied_matrix.pop(0)

        for column_index in range(0, len(copied_matrix)):
            copied_matrix[column_index].pop(line_index)

        determinant = determinant + (-1) ** (counter) * matrix[0][line_index] * determinant_calculation(copied_matrix)
        counter += 1

    return determinant

"""
Valida se a matriz informada está apta para ocorrer o cálculo do determinante.
"""
def determinant_validation(matrix, line_index, column_index):
    matrix_lines_length, _ = matrix_order(matrix)

    if line_index < 0 or column_index < 0 or matrix_lines_length <= 1:
        return Exception('A matriz informada é inválida')

    for index in matrix:
        if len(index) != matrix_lines_length:
            raise Exception('A matriz informada deve ser quadrada')

    formatted_matrix = []

    for i in range(matrix_lines_length):
        if i != line_index - 1:
            temp_matrix = []

            for j in range(len(matrix[i])):
                if j != (column_index - 1):
                    temp_matrix.append(matrix[i][j])

            formatted_matrix.append(temp_matrix)

    return determinant_calculation(formatted_matrix)

"""
Calcula a matrix dos cofatores a partir da matriz informada.
"""
def cofactor(matrix):
    cofactor_matrix = []

    matrix_lines_length, _ = matrix_order(matrix)

    for line_index in range(matrix_lines_length):
        cofactor_matrix.append([])

        for column_index in range(matrix_lines_length):
            determinant = determinant_validation(matrix, line_index + 1, column_index + 1)

            cofactor_matrix[line_index].append(int(math.pow(-1, line_index + column_index) * determinant))

    return cofactor_matrix

"""
Calcula a matrix inversa a partir da matriz dos cofatores.
"""
def inverse(matrix):
    if determinant_calculation(matrix) == 0:
        raise Exception('O determinante da matriz informada é 0, portanto ela não possui inversa')

    pass

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

"""
Chamada da função main
"""
if __name__ == "__main__":
    main()
