s = input().split()
a = int(s[0])
b = int(s[1])
print(a * b - 1)


# import itertools
# S = ['1', '2', '3', '4', '5', '6', '7']
# for S in itertools.combinations(S, 6):
#     print(" ".join(S))

#
# def yield_test():
#     yield 1
#     yield 2
#     yield 2
#     yield 3
#
#
# for _ in yield_test():
#     print(_)

# # val = list()
# # arr = list()
# # n = int(input())
# #
# # for i in range(0, n):
# #     val.append(int(input()))
# #     arr.append(0)
#
#
# val = input().split()
# val = list(map(int, val))
# n = val[0]
# arr = []
# for i in range(0, n):
#     arr.append(0)
#
# def dfs(arr2, index, n2, k, j, val2):
#     # print(arr2, index, n2, k, j, val2)
#     if k == 0:
#         for k1 in range(0, index):
#             print(arr2[k1], end = " ")
#         print()
#     elif j == n2:
#         return
#     else:
#         arr2[index] = val2[j]
#         dfs(arr2, index + 1, n2, k - 1, j + 1, val2)
#         dfs(arr2, index, n2, k, j + 1, val2)
#
#
# dfs(arr, 0, n, 6, 0, val)
#
#
#
# #
# #
# # val = list()
# # arr = list()
# # n = int(input())
# #
# # for i in range(0, n):
# #     val.append(int(input()))
# #     arr.append(0)
# #
# #
# # def dfs(arr2, index, n2, k, j, val2):
# #     print(arr2, index, n2, k, j, val2)
# #     if k == 0:
# #         for k in range(0, index):
# #             print(arr2[k] + " ")
# #         print("\n")
# #     elif j == n2:
# #         return
# #     else:
# #         arr2[index] = val2[j]
# #
# #         dfs(arr2, index + 1, n2, k - 1, j + 1, val2)
# #         dfs(arr2, index, n2, k, j + 1, val2)
# #
# #
# # dfs(arr, 0, n, 6, 0, val)
