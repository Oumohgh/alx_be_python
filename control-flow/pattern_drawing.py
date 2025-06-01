

# the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initi the row counter
row = 0

# while loop for each row
while row < size:
    # Use a for loop to print '*' in each column of the row
    for col in range(size):
        print("*", end="")
    print()  # Move to the next line after each row
    row += 1
