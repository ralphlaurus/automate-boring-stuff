
# search online meaning of the problem
def collatz(number):

    if (number % 2) == 0:
        # print(number // 2)
        return number // 2
    elif (number % 2 == 1):
        # print(3 * number + 1)
        return 3 * number + 1

try:
    print("Enter number: ")
    n = int(input())
    while n != 1:
        n = collatz(n)
        print(n)
except ValueError:
    print("Invalid input!")





