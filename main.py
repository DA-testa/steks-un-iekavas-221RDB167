# python3
# Renars Misuns 8.grupa 221RDB167

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])




def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]




def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(Bracket(next, i + 1))


        elif next in ")]}":
            if not opening_brackets_stack:
                return i + 1
            top = opening_brackets_stack.pop()
            if not are_matching(top.char, next):
                return i + 1
    if opening_brackets_stack:
        return opening_brackets_stack[0].position
    else:
        return "Success"


def main():
    type = input().strip()
    if type.isdigit() and int(type) in range(6):
        number = type
        path = "/workspaces/steks-un-iekavas-221RDB167/test/" + number
        with open (path, "r") as f:
            text = f.read().strip()
    elif type == "I":
        text = input("Enter brackets: ")
    else:
        print("Invalid input type")
        return


    mismatch = find_mismatch(text)
    print(mismatch)




if __name__ == "__main__":
    main()
