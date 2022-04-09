def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    s=input()
    for i in range(len(s)-1,-1,-1):
        print(s[i],end="")
    return 0

if __name__ == '__main__':
    main()
