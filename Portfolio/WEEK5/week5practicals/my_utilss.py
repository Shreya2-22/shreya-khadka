import sys

def average(values):
    """ Calculates the average of the given list. """
    total = sum(map(float, values))
    return total / len(values) if len(values) > 0 else 0

if __name__ == "__main__":
    # Executed only if my_utils.py is run directly from the command line
    arguments = sys.argv[1:]  # Exclude the script name
    if arguments:
        avg = average(arguments)
        print("Average of provided arguments is:", avg)
    else:
        print("No arguments provided.")