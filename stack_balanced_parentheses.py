from stack import Stack

def match(p1, p2):
    if p1 == "(" and p2 == ")":
        return True
    elif p1 == "[" and p2 == "]":
        return True
    elif p1 == "{" and p2 == "}":
        return True
    else:
        return False

def isBalanced(string):
    s = Stack()
    is_balanced = True
    index = 0

    while index < len(string) and is_balanced:
        par = string[index]
        if par in "({[":
            s.push(par)
        else:
            if s.isEmpty():
                is_balanced = False
            else:
                top = s.pop()
                if not match(top, par):
                    is_balanced = False

            
        index += 1

    if s.isEmpty() and isBalanced:
        return True
    else:
        return False

def __main__():
    inString = input("Enter a series of parentheses: ")
    print(isBalanced(inString))


if __name__ == "__main__":
    __main__()




