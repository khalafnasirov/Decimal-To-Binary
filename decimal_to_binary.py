n = ""
remainders = []

while True:
    n = input("Enter a number: ")
    if not n.isdigit():
        print("Please enter valid number")
    else:
        n = int(n)
        break

while True:
    remainders.append(n % 2)
    n = int(n / 2)
    if n < 1:
        for i in range(8 - remainders.__len__()):
            remainders.append(0)
        remainders.reverse()
        break

print("Result")
print(remainders)
