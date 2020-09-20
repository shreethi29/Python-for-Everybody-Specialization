largest = -1
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" :
        break
    try:
        n=float(num)
    except:
        print("Invalid input")
    if smallest is None:
        smallest=n
    elif n>largest:
        largest=n
    elif n<smallest:
        smallest=n
print("Maximum is",int(largest))
print("Minimum is",int(smallest))