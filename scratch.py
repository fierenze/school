#print(1)
#print("Hello, world!")
#print(True)
#print(None)

#a = int(input("Input a: "))
#b = int(input("Input b: "))
#c = int(input("Input c: "))

#D = b ** 2 + a + c

#print(D)

# for i in [1,5,2,0,9,3,4,"asdasd", 3.657, '2323', True, None]:
#     print(i)
#
# for i in range(10):
#     print("Pavel")
#
# for i in range(-123, 11, 7):
#     print(i)

print('\n')

x = 1024 * 4
while x > 0:
    if x == 256:
        break
    print(x)
    x = x // 4

print('\n')
x = 1024 * 4
while x > 0:
    x = x // 4
    if x == 256:
        continue
    print(x)
