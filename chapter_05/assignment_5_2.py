largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    else:
        try:
            float(num)
        except ValueError:
            print("Invalid input")
            continue
    if largest is None or smallest is None:
        largest = smallest = num
    elif float(num) > float(largest):
        largest = num
    elif float(num) < float(smallest):
        smallest = num
print("Maximum is", largest)
print("Minimum is", smallest)
