# num = [20,25,1,3]

# for x in num:
#     print(x)

# num2 = [
#             [10,20,50,75,3],
#             [5,14,26,22,41]
#         ]

# for x1 in num2:
#     for x2 in x1:
#         print(x2)


# number = int(input("input number "))
# fib = []
# a, b = 0, 1
# count = 0
# while count < number:
#     fib.append(a)
#     a, b = b, a + b
#     count += 1
# print(fib)



number = int(input("input number "))
a,b = 0, 1
count = 0
print(a)
while count < number:
    c = a+b
    print(c)
    a = b
    b = c
    count += 1