import random

def pc_guess(num):
    low = 0
    high = 200
    guess = 100  #This is a starting number
    while guess != num:  #while - repeat the execution of the code until the right answer will be found / != not equal
        guess = (low+high)//2  #Instead of checking all numbers from 0 to 200, first guess is 100 and is divided in half between next low or high numbers
        print("PC tries to guess...", guess)
        if guess > num:
            high = guess
            print("Your number is higher")
        elif guess < num:
            low = guess + 1
            print("Your number is lower")

    print("PC guessed number", guess, "and it was correct!")


def main():
    num = int(input("Enter a number: "))
    if num < 0 or num > 200:
        print("Must be in range [1, 200]")
    else:
        pc_guess(num)

if __name__ == '__main__':
    main()