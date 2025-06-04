row = int(input("Enter the size of the pattern: "))
i = 1
while i <= row:
    j = 1
    while j <= row :
        print("*", end="")
        j = j + 1
    print()
    i = i + 1
