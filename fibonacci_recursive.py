def fibonacci(n):
    if n == 0:
        return n
    elif n == 1:
        return 1
    else:
        return(fibonacci(n-1) + fibonacci(n-2))

print(fibonacci(10))

# if we wanted to make a list of fibonacci numbers, the length of the input number.
# fibonacci_sequence= []
# for num in range(0, 5):
#     fibonacci_sequence.append(fibonacci(num))
# print(fibonacci_sequence)

