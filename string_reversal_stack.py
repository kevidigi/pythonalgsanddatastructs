from stack import Stack

def reverse_string(input_string):
    string_stack = Stack()
    output_string = ""
    for c in input_string:
        string_stack.push(c)

    while not string_stack.isEmpty():
        output_string += string_stack.pop()

    return output_string

def __main__():

    input_string = input("Enter a string to reverse: ")
    print(reverse_string(input_string))

if __name__ == "__main__":
    __main__()
