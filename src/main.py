"""
Função main, onde o arquivo começa a ser interpretado
"""
from re import A


def main():
    try:
        matrix_01 = [
            [2],
            [3],
        ]

        matrix_02 = [
            [1, 2, 0],
        ]

        result = multiplication(a=matrix_01, b=matrix_02)

        print(result)
    except Exception as ex:
        print(f'Ocorreu o seguinte erro: {ex}')


"""
Multiplica as duas matrizes informadas através de três laços de repetição encadeados.
A rotina cria novas linhas zeradas e vai adicionando colunas zeradas na mesma, previamente às somas das multiplicações.
"""
def multiplication(a, b):
    a_lines_length, a_columns_length = matrix_order(a)
    b_lines_length, b_columns_length = matrix_order(b)

    if a_columns_length != b_lines_length:
        raise Exception('A matriz A possui uma quantidade de linhas diferentes da quantidade de colunas da matriz B')

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
