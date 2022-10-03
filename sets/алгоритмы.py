'''
n = int(input())
Числа Фиб:

arr = [1] * (n+1)

for i in range(2, n+1):
    arr[i] = arr[i-1] + arr[i-2]

print(arr[-1])


arr = [1, 1]
i = 1
while i < n:
    arr = [arr[1], arr[0] + arr[1]]
    i += 1
print(arr[-1])

Простые числа:

flag = True
if n % 2 == 0:
    flag = False
for i in range(3, int(n**0.5)+1, 2):
    if n % i == 0:
        flag = False
        break
if flag:
    print("Простое")
else:
    print("Не простое")


'''
#
# res = 0
# s = input()
# roman = {
#         "I":1,
#         "V":5,
#         "X":10,
#         "l":50,
#         "C":100,
#         "D":500,
#         "M":1000
#     }
#
# for i in range(len(s)-1):
#     cur = s[i]        # Текущий элемент
#     next = s[i+1]
#     if cur == 'I':
#         if next == 'V' or next == 'X':
#             res -= roman[cur]
#         else:
#             res += roman[cur]
#
#     elif cur == 'X':
#         if next == 'L' or next == 'C':
#             res -= roman[cur]
#         else:
#             res += roman[cur]
#
#     elif cur == 'C':
#         if next == 'D' or next == 'M':
#             res -= roman[cur]
#         else:
#             res += roman[cur]
#     else:
#         res += roman[cur]
#
# print(res)
l = {1, 2, 3, 4, 5, 6}
l.add(12)
l.add(12)
print(l)
