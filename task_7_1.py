# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов
# класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки
# первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.

class Matrix:
    def __init__(self, my_ls):
        self.matrix = my_ls

    def __str__(self):
        result = []
        my_str = ''
        for el in self.matrix:
            for il in el:
                result.append(il)
                result.append(" ")
            result.append("\n")
        for s in result:
            my_str += str(s)
        return my_str

    def __add__(self, other):
        lcl_mtrx = [[]]
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            return "Мы можем ссуммировать только равных размерностей матрицы"

        for i in range(0, len(self.matrix)):
            for j in range(0, len(self.matrix[i])):
                lcl_mtrx[i].append(self.matrix[i][j] + other.matrix[i][j])
            lcl_mtrx.append([])
        return Matrix(lcl_mtrx)


my_matrix = Matrix([[1, 0, 2], [5, 0, 4]])
my_matrix_0 = Matrix([[7, 18, 22], [51, 1, 16]])

my_matrix_1 = Matrix([[1, 0, 2, 5], [5, 0, 4, 6]])

print(my_matrix)
print(my_matrix_0)

print(my_matrix_1)
print(f"Сумма матриц: \n{my_matrix + my_matrix_0}")
print(my_matrix + my_matrix_1)


