# n = input()
# if len(n) > 3:
#     n1 = n[::-1]
#     n2 = ''
#     for i in range(len(n1)):
#         if (i+1) % 3 == 0 :
#             n2 += n1[i]
#             n2 += ','
#         else:
#             n2 += n1[i]
#     n3 = n2[::-1]
#     if n3[0] == ',':
#         print(n3[1::])
#     else:
#         print(n3)
# else:
#     print(n)

# Задача Иосифа Флавия

# n = int(input())
# k = int(input())
#
# def joseph(n, k):
#     res = 0
#     for i in range(1, n + 1):
#         res = (res + k) % i
#     return res + 1
#
# print(joseph(n, k))

# Координатные четверти

# n = int(input())
# x_y_list = []
# for i in range(n):
#     x_y_list.extend(map(int, input().split()))
# # print(x_y_list)
# sum1, sum2, sum3, sum4 = 0, 0, 0, 0
#
# for i in range(0, n * 2, 2):
#     if x_y_list[i] > 0 and x_y_list[i + 1] > 0:
#         sum1 += 1
#     elif x_y_list[i] < 0 and x_y_list[i + 1] > 0:
#         sum2 += 1
#     elif x_y_list[i] < 0 and x_y_list[i + 1] < 0:
#         sum3 += 1
#     elif x_y_list[i] > 0 and x_y_list[i + 1] < 0:
#         sum4 += 1
# print(f"Первая четверть: {sum1}")
# print(f"Вторая четверть: {sum2}")
# print(f"Третья четверть: {sum3}")
# print(f"Четвертая четверть: {sum4}")

# Больше предыдущего

# s = input()
# l = s.split()
# print(l)
# result = 0
# for i in range(len(l)-1):
#     if int(l[i]) < int(l[i + 1]):
#         result += 1
# print(result)
#
# Назад, вперёд и наоборот

# s = input()
# l = s.split()
#
# if len(l) % 2 == 0:
#     for i in range(0, len(l)-1, 2):
#         l[i], l[i + 1] = l[i + 1], l[i]
# else:
#     for i in range(0, len(l)-2, 2):
#         l[i], l[i + 1] = l[i + 1], l[i]
# print(' '.join(l))

# Шифр Цезаря для английского алфавита

def rot(word_num):
    global text
    l_text = text.split()
    for i in range(len(l_text)):
        for c in l_text[i]:
            if c.isalpha() == False:
                l_text[i] = l_text[i].replace(c, '')
    return len(l_text[word_num])

def encrypt(rot, text):
    encrypted_text = ''
    for c in text:
        if 65 <= ord(c) <= 90:
            if ord(c) + rot > 90:
                encrypted_text += chr(ord(c) + rot - 26)
            elif ord(c) + rot <= 90:
                encrypted_text += chr(ord(c) + rot)
        elif 97 <= ord(c) <= 122:
            if ord(c) + rot > 122:
                encrypted_text += chr(ord(c) + rot - 26)
            elif ord(c) + rot <= 122:
                encrypted_text += chr(ord(c) + rot)
        else:
            encrypted_text += c
    return encrypted_text
text = input()
l_text = text.split()
encrypted_text = []
for i in range(len(l_text)):
    encrypted_text.append(encrypt(rot(i), l_text[i]))
print(' '.join(encrypted_text))