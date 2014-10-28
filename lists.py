__author__ = 'ondrej'

l1 = [1, 2, 3, 4]
l2 = ['this', 'is', 'awesome']

for word in l2:
    print(word)


def factorial(n):
    try:
        assert(isinstance(n, int))
        if n < 0:
            return 0
        elif n == 0:
            return 1
        else:
            return n * factorial(n-1)
    except AssertionError:
        print("factorial couldn't be computed")
        return 0

print(str(factorial(5.0)))

myFile = open("tubas.txt", "w")
myFile.write("Hello tubas")
myFile.close()