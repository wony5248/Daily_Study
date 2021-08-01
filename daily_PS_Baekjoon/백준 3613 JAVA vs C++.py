string = input()
if not string.isalpha():
    print("Error!")
string = list(string)
if "_" in string:
    for i in range(len(string)-1):
        if string[i] == "_":
            string[i+1].upper()
print(string)