from random import randrange


def user_guess():
    while True:
        try:
            guess = int(input("please enter a number from 1 to 10\n"))
            if guess <= 0 or guess > 10:
                print("please enter a number from 1 to 10")
                continue
            return int(guess)
        except ValueError:
            print("please only enter a number from 1 to 10")
            pass

def random_number():
    return randrange(10)


def higher_or_lower(winning_number):
    guess = user_guess()
    while guess != winning_number:
        if guess < winning_number:
            print(str(guess) + " was too low, please guess again!")
            guess = user_guess()
        else:
            print(str(guess) + " was too high, please guess again!")
            guess = user_guess()
    return "Your guess of " + str(guess) + " is correct!"


print(higher_or_lower(random_number()))

# def get_result(guess, random):
#     if guess < random:
#         print("Guess: " + str(guess) + ". Actual: " + str(random) + ". Your guess was too low")
#     elif guess > random:
#         print("Guess: " + str(guess) + ". Actual: " + str(random) + ". Your guess was too high")
#     else:
#         print("Your guess of: " + str(guess) + " was correct!")
#
#
# get_result(user_guess(), random_number())