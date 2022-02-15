# from pprint import pprint
#
# # num_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# #
# # for r in range(len(num_list)):
# #     for c in range(len(num_list[0])):
# #         if num_list[r][c] == 5:
# #             print(num_list[r-1][c], num_list[r+1][c], num_list[r][c-1], num_list[r][c+1])
#
#
# # num_list = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]
#
# matrix = []
# # for n in range(5):
# #     matrix_temp = [k + 5*n for k in range(1, 6)]          #삼항연산자
# #     matrix.append(matrix_temp)
# # print(matrix)
# print((0 & 1))
#
#
# matrix = [[k + 5*n for k in range(1, 6)] for n in range(5)]
# # print(matrix)
#
#
# rd = [0, -1, 0, +1]  # 우 하 좌 상
# cd = [1, 0, -1, 0]
# sum_d = 0
#
# for r in range(len(matrix)):
#     for c in range(len(matrix[0])):
#         for k in range(4):
#             row_d = r + rd[k]
#             col_d = c + cd[k]
#             if 0 <= row_d < len(matrix) and 0 <= col_d < len(matrix[0]):
#                 if matrix[r][c] < matrix[row_d][col_d]:
#                     sum_d -= matrix[r][c] - matrix[row_d][col_d]
#                 else:
#                     sum_d += matrix[r][c] - matrix[row_d][col_d]
#
#         print(sum_d)
#
#
for j in range(99,-1, -1):
    print(j, end=' ')

# print(1)