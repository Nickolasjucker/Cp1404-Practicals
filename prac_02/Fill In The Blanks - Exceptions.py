"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""

finished = False
while not finished:
    try:
        result = input("what is your result?: ")
        finished = True
    except ValueError:
        print("Please enter a valid integer.")
print("Valid result is:", result)