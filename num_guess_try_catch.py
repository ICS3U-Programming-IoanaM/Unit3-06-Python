#!/usr/bin/env python3
# Copyright (c) 2022 Ioana Marinescu All rights reserved.
# Created By: Ioana Marinescu
#
# Date: Oct. 31, 2022
# random number guessing game with try catch


import random


def main():
    # variables
    user_num_string = input("Please enter a number from 0 to 9: ")
    rand_num = random.randint(0, 9)

    # exception handling
    try:
        user_num_int = int(user_num_string)

    # if the user didn't input a number
    except ValueError:
        print(f"{user_num_string} is not a number! Please enter a valid input")

    # if user imputed an integer
    else:

        # if user imputed a number out of range
        if user_num_int < 0 or user_num_int > 9:
            print("Please input a number between 0 and 9!")

        # user imputed number within range
        else:
            # user guessed right
            if user_num_int == rand_num:
                print(f"Correct! {user_num_int} is the right number!")

            # user didn't input right number
            else:
                print(f"Incorrect! The right number is {rand_num}.")

    # final message to user
    finally:
        print("thank you for playing!")


if __name__ == "__main__":
    main()
