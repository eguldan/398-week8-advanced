#!/usr/bin/env python3

# new function to show Coveralls going down
def randomFunction(arg):
    val1 = 'Travis Scott'
    val2 = 'Beach House'
    val3 = 'The Weeknd'

    if val1 == val2:
        print('Cool beans')


def calculate(arg):
    stack = []

    tokens = arg.split()

    for token in tokens:
        try:
            stack.append(int(token))
        except ValueError:
            val2 = stack.pop()
            val1 = stack.pop()
            if token == '+':
                result = val1 + val2
            elif token == '-':
                result = val1 - val2
            elif token == '^':
                result = val1 ** val2

            stack.append(result)
    
    if len(stack) > 1:
        raise ValueError('Too many arguments on the stack')
    
    return stack[0]

def main():
    while True:
        try:
            calculate(input("rpn calc> "))
            print(result)
        except ValueError:
            pass

if __name__ == '__main__':
    main()

