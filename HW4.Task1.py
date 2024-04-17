"""Напишите функцию для транспонирования матрицы"""



def trans_matrix(matrix):
      trans_matrix = [[0 for j in range(len(matrix))] for i in range(len(matrix[0]))]
      for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                  trans_matrix[j][i] = matrix[i][j]
      return trans_matrix



matrix = [[1,2], [3,4], [5,6]]

print(trans_matrix(matrix))