def main():
    length = int(input())
    text = input()

    list = ["a", "e", "i", "o", "u"]

    result = 0
    for i in range(length):
        if (text[i] in list):
            result += 1

    print(result)

if __name__== "__main__":
    main()