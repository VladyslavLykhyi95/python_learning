some_string = input("Please enter some text: ")

if len(some_string) % 2 == 0:
    print(some_string[len(some_string)//2:], some_string[:len(some_string)//2], sep="")
else:
    print(some_string[len(some_string) // 2+1:], some_string[:len(some_string) // 2+1], sep="")