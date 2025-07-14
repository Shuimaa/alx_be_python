# Ask the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Use a while loop to handle rows
while row < size:
    # For each row, print stars using a for loop
    for col in range(size):
        print("*", end="")
    print()  # Move to next line after each row
    row += 1
