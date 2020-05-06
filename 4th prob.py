str = input("Enter a string\n")
for index in range(len(str)):
    if index % 2 == 0:
        print(str[index], end='')