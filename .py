# importing random
import random

# taking input from user
user_pass = input("Enter your password: ")

# storing alphabet letter to use thm to crack password
password = [1,2,3,4,5,6,7,8,9,0]

# initializing an empty string
guess = ""


# using while loop to generate many passwords until one of
# them does not match user_pass
while (guess != user_pass):
    guess = ""
    # generating random passwords using for loop
    for letter in range(len(user_pass)):
        guess_letter = password[random.choice(password)]
        guess = str(guess_letter) + str(guess)
    # printing guessed passwords
    print(guess)
    
# printing the matched password
print("Your password is",guess)
