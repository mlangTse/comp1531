import numpy

my_list = []
for i in range(5):
        my_list.append(int(input(f"Enter {chr(ord('a') + i)}: ")))


print("Minimum: ", min(my_list))
print("Product of first 4 numbers: ", numpy.prod(my_list[:4]))
print("Product of last 4 numbers", numpy.prod(my_list[1:]))

'''
if __name__ == '__main__':
    a = input("Enter a: ")
    a = int(a)
    b = input("Enter b: ")
    b = int(b)
    c = input("Enter c: ")
    c = int(c)
    d = input("Enter d: ")
    d = int(d)
    e = input("Enter e: ")
    e = int(e)
    my_list = [a, b, c, d, e]
    my_min = 999999
    for i in range(0, 5):
        if my_list[i] < my_min:
            my_min = my_list[i]
    print("Minimum: " + str(my_min))
    print("Product of first 4 numbers: ")
    product = 1
    for i in range(0, 4):
        product = product * my_list[i]
    print(f"  {product}")

    print("Product of last 4 numbers")
    product = 1
    for i in range(1, 5):
        product = product * my_list[i]
    print(f"  {product}")
'''