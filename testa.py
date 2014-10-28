__author__ = 'ondrej'



def test_function():
    a = 10
    b = 20
    return a * b


name = "Ondrej"
surname = "Budac"

done = False
while not done:
    try:
        a = int(input("Enter a positive integer"))
        if a > 0:
            done = True
        else:
            print("The integer you entered is not positive")
    except ValueError:
        print("You didn't input an integer")
    finally:
        print("Something went wrong, please repeat")









