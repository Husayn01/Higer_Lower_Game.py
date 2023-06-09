import random
from art import logo
from art import vs
from data import data

print(logo)

# Initialize variables
A = "A"
B = "B"
score = 0
shouldContinue = True
accountTwo = random.choice(data)

def accountOneFunc(data, alphaOne):
    """
    Prints information about the first account to be compared.
    Args:
        data (dict): Data of the account.
        alphaOne (str): Label for the first account (A).
    """
    name = data["name"]
    description = data["description"]
    country = data["country"]
    print(f"Compare {alphaOne}: {name}, a {description}, from {country}")

def accountTwoFunc(data, alphaTwo):
    """
    Prints information about the second account to be compared.
    Args:
        data (dict): Data of the account.
        alphaTwo (str): Label for the second account (B).
    """
    name = data["name"]
    description = data["description"]
    country = data["country"]
    print(f"Against {alphaTwo}: {name}, a {description}, from {country}")

def checkAnswer():
    """
    Checks if the user's answer is correct.
    Returns:
        bool: True if the user's answer is correct, False otherwise.
    """
    if accountOneFollowers > accountTwoFollowers:
        return guess == "a"
    else:
        return guess == "b"

while shouldContinue:
    accountOne = accountTwo
    accountTwo = random.choice(data)

    # Ensure the same account is not selected for comparison
    if accountOne == accountTwo:
        accountTwo = random.choice(data)

    accountOneFunc(data=accountOne, alphaOne=A)
    print(vs)
    accountTwoFunc(data=accountTwo, alphaTwo=B)

    guess = input("Who has more followers? Type A or B: \n").lower()
    accountOneFollowers = accountOne["follower_count"]
    accountTwoFollowers = accountTwo["follower_count"]
    print(accountOneFollowers)
    print(accountTwoFollowers)

    isCorrect = checkAnswer()

    if isCorrect:
        score += 1
        print(f"Current score: {score}")
        print("You are right")
    else:
        print(f"Current score: {score}")
        shouldContinue = False
        print("You are wrong")
