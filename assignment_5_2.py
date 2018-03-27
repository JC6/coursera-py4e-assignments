largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    elif largest is None:
        largest = num
    elif smallest is None:
        smallest = num
    else:
        try:
            if float(num) > float(largest):
                largest = num
            elif float(num) < float(smallest):
                smallest = num
        except ValueError:
            print("Invalid input")

print("Maximum is", largest)
print("Minimum is", smallest)
