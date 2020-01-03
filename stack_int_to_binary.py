from stack import Stack

def binarification(num):
    s = Stack()

    while num > 0:
        rem = num % 2
        s.push(rem)
        num = num // 2

    binary = ""
    while not s.isEmpty():
        binary += str(s.pop())

    return binary

def __main__():
    decimal = int(input("Enter a decimal number: "))
    binarified = binarification(decimal)
    print("Binary representation of " + str(decimal) + ": " + binarified)

if __name__ == __main__():
    __main__()
