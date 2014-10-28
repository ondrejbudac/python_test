__author__ = 'ondrej'

minval = int(0)
maxval = int(10)
while minval < maxval:
    guess = (maxval + minval) // 2
    print("My guess, it is " + str(guess))
    ans = int(input("Is it correct? (0: yes, 1: no, my number is bigger, 2: no, my number is smaller): "))
    if ans == 0:
        break
    elif ans == 1:
        minval = guess + 1
    else:
        maxval = guess - 1
print("I knew it was " + str(minval) + " all along")


