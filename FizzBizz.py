# gather inputs
number = int(input("Enter number: "))

# Output Fizz or Buzz based on divisibility
if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
        #This must go first or else the other statements will trigger first
elif number % 3 == 0:
    print("Fizz")
elif number % 5 == 0:
    print("Buzz")
