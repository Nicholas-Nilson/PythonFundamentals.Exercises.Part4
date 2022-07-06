input_range = range(1,101)

def fizz_buzz(range_to_check):
    '''Fizz & Buzz; partners in crime, multiples of 15 are in shambles'''
    fizz_buzz_range = range_to_check
    for num in fizz_buzz_range:
        if (num % 15 ==0):
            print("FizzBuzz")
        elif (num % 3 == 0):
            print("Fizz")
        elif (num % 5 == 0):
            print("Buzz")
        else:
            print(num)

fizz_buzz(input_range)