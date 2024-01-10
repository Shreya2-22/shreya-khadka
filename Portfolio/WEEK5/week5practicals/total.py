import sys

# storing the total number of arguments
count = len(sys.argv)


total = 0
average = 0


if count > 1:  # If count is 1, only script name is present
    count -= 1  # Exclude the script name from the count

    # Calculate total sum of arguments
    while count > 0:
        total += float(sys.argv[count])
        count -= 1

    # Calculate average
    average = total / (len(sys.argv) - 1)
    
    # Print total and average
    print("Total is:", total)
    print("Average is:", average)
else:
    # If no arguments (excluding script name) were passed
    print("No arguments were provided.")
