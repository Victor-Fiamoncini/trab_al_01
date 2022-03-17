"""
Função main, onde o arquivo começa a ser interpretado
"""
def main():
    try:
        matrix_01 = [
            [1, 6, 9],
            [3, 7, 2],
            [8, -8, 0],
            [-9, 5, 7],
        ]

        matrix_02 = [
            [10, 4, 9],
            [-5, -7, 0],
            [-5, -7, 0],
            [0, 2, -12],
        ]

        result = sum(a=matrix_01, b=matrix_02)

        print(result)
    except Exception as ex:
        print(f'Ocorreu o seguinte erro: {ex}')

"""
Retorna a ordem da matrix informada.
"""
def matrix_order(matrix):

    matrix_lines_length = len(matrix)
    matrix_columns_length = len(matrix[0])

    return matrix_lines_length, matrix_columns_length

"""
Soma as duas matrizes informadas através de dois laços de repetição encadeados.
A rotina vai criando novas linhas zeradas previamente às somas.
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


if __name__ == "__main__":
    main()
