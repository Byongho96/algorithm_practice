if __name__ == "__main__":
    string = input()

    answer = len(string)
    for i in range(1, answer):
        if string[i] == "-":
            answer -= 1
        elif string[i] == "=":
            if i > 1 and string[i - 2] == "d" and string[i - 1] == "z":
                answer -= 2
            else:
                answer -= 1
        elif string[i] == "j":
            if string[i - 1] == "l" or string[i - 1] == "n":
                answer -= 1

    print(answer)
