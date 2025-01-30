def main():
    width = int(input())
    height = int(input())
    
    for i in range(width):
        for j in range(height):
            if j == height-1:
                print("*")
            else:
                print("*", end="")

if __name__== "__main__":
    main()