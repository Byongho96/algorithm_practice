PRIORITY = {"*": 0, "/": 0, "+": 1, "-": 1, "(": 2, ")": 2}


def main(inorder: str):
    inorder += ")"
    stack = ["("]
    postorder = ""

    for c in inorder:
        if c.isalpha():
            postorder += c
        elif c == "(":
            stack.append(c)
        elif c == ")":
            while stack[-1] != "(":
                postorder += stack.pop()
            stack.pop()
        else:
            while PRIORITY[stack[-1]] - 1 < PRIORITY[c]:
                postorder += stack.pop()
            stack.append(c)

    return postorder


if __name__ == "__main__":
    print(main(input()))
