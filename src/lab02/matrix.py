
def transpose(mat: list[list[float | int]]) -> list[list]:
    """ Поменять строки и столбцы местами. Пустая матрица [] → [].
    Если матрица «рваная» (строки разной длины) — ValueError """
    if len(mat) == 0:
        return []

    lgh = len(mat[0])
    
    for row in mat:
        if len(row) != lgh:
            raise ValueError=
    
    matr = []
    for j in range(lgh):
        res = []
        for i in range(len(mat)):
            res.append(mat[i][j])
        matr.append(res)
    return matr

def row_sums(mat: list[list[float | int]]) -> list[float]:
    """ Сумма по каждой строке. Требуется прямоугольность """
    if mat:

        lgh = len(mat[0])
    
        for row in mat:
            if len(row) != lgh:
                raise ValueError
            
    return [sum(row) for row in mat]
    

def col_sums(mat: list[list[float | int]]) -> list[float]:
    """Сумма по каждому столбцу.Требуется прямоугольность"""
    if len(mat)==0:
        return []

    lgh = len(mat[0])
    
    for row in mat:
        if len(row) != lgh:
            raise ValueError

    result = []
    for j in range(lgh):
        s = 0
        for i in range(len(mat)):
            s += mat[i][j]
        result.append(s)
    return result

""" print(transpose([[1, 2, 3]]))
print(transpose([[1], [2], [3]]))
print(transpose([[1, 2], [3, 4]]))
print(transpose([]))
print(transpose([[1, 2], [3]])) """

""" print(row_sums([[1, 2, 3], [4, 5, 6]]))
print(row_sums([[-1, 1], [10, -10]]))
print(row_sums([[0, 0], [0, 0]]))
print(row_sums([[1, 2], [3]])) """


""" print(col_sums([[1, 2, 3], [4, 5, 6]]))
print(col_sums([[-1, 1], [10, -10]]))
print(col_sums([[0, 0], [0, 0]]))
print(col_sums([[1, 2], [3]])) """