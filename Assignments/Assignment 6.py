# cow and bull
import random

# def cow_bull_game(secret_number, guess):
#     cows = 0
#     bulls = 0

#     for i in range(len(secret_number)):
#         if guess[i] == secret_number[i]:
#             bulls += 1
#         elif guess[i] in secret_number:
#             cows += 1

#     return cows, bulls

# def play_game():
#     secret_number = str(random.randint(1000, 9999))
#     print("Welcome to the Cow-Bull Game!")
#     print("Try to guess the 4-digit secret number.")

#     attempts = 0
#     while True:
#         guess = input("Enter your guess: ")
#         attempts += 1

#         if len(guess) != 4 or not guess.isdigit():
#             print("Please enter a 4-digit number.")
#             continue

#         cows, bulls = cow_bull_game(secret_number, guess)

#         print(f"Cows: {cows}, Bulls: {bulls}")

#         if bulls == 4:
#             print("Congratulations! You've guessed the number correctly!")
#             print(f"Number of attempts: {attempts}")
#             break

# play_game()
# -------------------------------------------------------------
# palindrome

def isPalindrome(s):
	return s == s[::-1]

s = "malayalam"
ans = isPalindrome(s)

if ans:
	print("Yes")
else:
	print("No")
	
# ---------------------------------------------------------------

def fibonacci(n):
    fib_sequence = [0, 1]
    
    
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    
    return fib_sequence


print(fibonacci(10))  

print(fibonacci(9))


