################################################################
# Project: BankAccount
# File: main.py
# Description: This program asks user to input beginning balance and
# debits and these will be deducted from the beginning balance
# Author: Chiquita Zephaniah
# Version: 1.0
# Date: November 13, 2022
################################################################

import Util
print("Bank Account")
def main():
    keep_going = True
    total = 0
    # get first input
    string_input = input("Please enter your beginning balance of a bank account: ")
    # start loop
    while keep_going == True:
        # edit input
        if Util.is_numeric(string_input):
            # if good, process input
            beginning_balance = float(string_input)
            print(beginning_balance)
            keep_going = False
        else:
            # otherwise, issue error message
            print("Input must be numeric")
            string_input = input("Please enter your beginning balance of a bank account: ")

    keep_going = True
    while keep_going == True:
        # whether input is valid or not, get another input
        string_input = \
            input("Please enter the debit or enter \"q\" to quit ")
        if string_input == "q":
            keep_going = False

        elif Util.is_numeric(string_input):
            debit = float(string_input)
            print(debit)
            total = total + debit
        else:
            print("Input must be numeric")


    # calculate and output the remaining balance
    balance = beginning_balance - total
    print(f"Balance: {balance:.2f}")


main()
