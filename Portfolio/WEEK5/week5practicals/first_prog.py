number = input("Enter a number: ")#taking the user to input a number

#converting the input to integer data type
number = int(number)

print("The numbered entered was", number)
#checking if the number is even or odd and displaying the result
if (number % 2) == 0:
     print("That is an even number")
else:
     print("That is an odd number")
# Checking if the number is divisible by 10 and displaying the result
if (number % 10) == 0:
    print("That number is divisible by 10")
else:
    print("That number is not divisible by 10")
