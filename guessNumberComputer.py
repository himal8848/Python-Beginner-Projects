import random

#Guess from User
def guess(num):
    random_number = random.randint(1,num)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Enter a number between 1 and {num}: "))
        if guess < random_number:
            print("sorry,Too low")
        elif guess > random_number:
            print("Sorry,Too high")
    print("Yes,you have entered correct number")

guess(10)

#Computer Guess

def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != "c":
        if low != high:
            guess = random.randint(low,high)
        else:
            guess = low
        feedback = input(f"The number {guess} is ,Too high(H),Too Low(L)").lower()
        if feedback == "h":
            high = guess-1
        elif feedback == "l":
            low = guess + 1
    print("Yes,you are correct")
computer_guess(1000)
