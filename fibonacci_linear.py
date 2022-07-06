# **Requirements**
# * Given a term (n), determine the value of x(n).
# * In the *fibonacci_linear.py* program, create a function called *fibonnaci*. The function should take in an integer and return the value of x(n).
# * This problem must be solved **WITHOUT** the use of recursion.
# **Constraints**
# n >= 0

def fibonacci_linear(n):
    if n == 0:
        return 0
    else:
        result = 0
        prev_num = 1
        while n > 0:
            temp = result
            result = result + prev_num
            prev_num = temp
            n = n -1
    return result
print(fibonacci_linear(12))