largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" : break
    try:
        no = int(num)
    except:
        print("Invalid input")
    if largest is None:
        largest = no
    if largest < no:
        largest = no
    if smallest is None:
        smallest = no
    if smallest > no:
        smallest = no

print("Maximum is", largest)
print("Minimum is",smallest)
