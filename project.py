#SOFT6017 Project 2018
#Author João Carvalho
#Student number: R00158576

#Import random module
import random

#Function that checks if user inputs at least one character
def read_non_empty_string(prompt):

    is_true = True

    while is_true:

        name = input(prompt)

        if len(name)>0:

            is_true=False

        else:

            print("\nPlease insert at least one character")

    return name

#Function that checks if user inputs a non negative float
def read_non_negative_float(prompt):

    is_true = True

    while is_true:

        try:

            number = float(input(prompt))

            if number > 0:

                is_true = False

            else:

                print("\nPlease insert a non negative number")

        except:

            print("\nPlease insert a numeric value")

    return number

#Function that checks if user inputs a non negative integer
def read_non_negative_int(prompt):

    is_true = True

    while is_true:

        try:

            number = int(input(prompt))

            if number > 0:

                is_true = False

            else:

                print("\nPlease insert a non negative number")

        except:

            print("\nPlease insert a numeric value")

    return number

# function to validate that x lies between minimum and maximum inclusive
def check_if_valid(minimum, maximum, x):

    return minimum <= x <= maximum

#Function that prints welcome greeting to the user
def welcome(greeting):

    print("=" * len(greeting) + "\n" + greeting + "\n" + "=" * len(greeting))

#Function that reads data from a file and appends three lines to three different lists
def get_data(file_name):

    in_file = open(file_name + ".txt", 'r')

    bank_account = []

    account_balance = []

    account_name = []

    while True:

        line = in_file.readline().rstrip()

        if line == "":

            break

        bank_account.append(int(line))

        line = in_file.readline().rstrip()

        account_balance.append(float(line))

        line = in_file.readline().rstrip()

        account_name.append(line)

    in_file.close()

    return  bank_account, account_balance, account_name

# function to get the user's choice
def get_choice():

    menu = "\nWould you like to" + "\n\t1: Open an account" \
                                "\n\t2: Close an account" \
                                "\n\t3: Withdraw money" \
                                "\n\t4: Deposit money" \
                                "\n\t5: Generate a report for management" \
                                "\n\t6: Quit" \
                                "\n\tInsert option >>> "

    is_true = True

    while is_true:

        try:

            choice = int(input(menu))

            if check_if_valid(1, 6, choice):

                is_true = False

            else:

                print("\nValues 1-6 please...")

        except:

            print("\nMust be numeric...")

    return choice

#Function that creates a new bank account
def create_bank_account(bank_account, account_balance, account_name):

    name = read_non_empty_string("\nPlease insert your name >>> ")

    account_number = random.randint(111111, 999999)

    balance = 0

    if account_number not in bank_account:

        account_name.append(name)

        bank_account.append(account_number)

        account_balance.append(balance)

        print("\nCongratulations an account was created under the name " + name + " with the account number " \
              + str(account_number) + " with a balance of " + str(format(balance, ".2f")) + " Euros")

    else:

        print("A bank account with that number already exists")

#Function that deletes a bank account
def delete_account(bank_account, account_balance, account_name):

    account_number = read_non_negative_int("\nInsert the number of the account you want to delete >>> ")

    if account_number in bank_account:

        for i in bank_account:

            if i == account_number:
                index = bank_account.index(i)

                bank_account.remove(i)

                account_balance.pop(index)

                account_name.pop(index)

        print("\nCongratulations account with number " + str(account_number) + " was removed")

    else:

        print("\nNo account found with the number that you provided")

#Function that withdraws money from a bank account
def withdraw_money(bank_account, account_balance):

    account_number = read_non_negative_int("\nInsert the number of your bank account >>> ")

    if account_number in bank_account:

        withdraw_amount = read_non_negative_float("\nInsert the amount you want to withdraw >>> ")

        for i in bank_account:

            if i == account_number:

                index = bank_account.index(i)

                account_balance[index] -= withdraw_amount

        print("\nWe withdraw with success " + str(format(withdraw_amount, ".2f")) + " Euros from your bank account")

    else:

        print("\nNo account found with the number that you provided")

#Function to deposit money on the bank account
def deposit_money(bank_account, account_balance):

    account_number = read_non_negative_int("\nInsert the number of your bank account >>> ")

    if account_number in bank_account:

        deposit_amount = read_non_negative_float("\nInsert the amount you want to deposit >>> ")

        for i in bank_account:

            if i == account_number:
                index = bank_account.index(i)

                account_balance[index] += deposit_amount

        print("\nWe deposited with success " + str(format(deposit_amount, ".2f")) + " Euros in your bank account")

    else:

        print("\nNo account found with the number that you provided")

#Function that presents a report for management
def management_report(bank_account, account_balance, account_name, welcome):

    total_deposit = sum(account_balance)

    largest_deposit = max(account_balance)

    indexes = []

    count = 0

    for i in account_balance:

        if i == largest_deposit:
            indexes.append(count)

        count += 1

    count = 0

    welcome("Report for Management")

    for i in bank_account:
        print(format("\nAccount number: ", "20s") + str(i) + format("\nAccount Balance: ", "20s")
              + str(format(account_balance[count], ".2f")) + format("\nAccount Owner: ", "20s")
              + account_name[count] + "\n\n")

        count += 1

    print("\nTotal amount deposited: " + str(total_deposit))

    print("\nThe largest('s) amount on deposit:", end = "")

    for i in indexes:
        print(" " + str(account_balance[i]) + " - " + account_name[i])

#Function that exits the program and writes the data from the lists to the file
def finish(bank_account, account_balance, account_name, file_name):

    in_file = open(file_name + ".txt", 'w')

    for i in range(len(bank_account)):
        in_file.write(str(bank_account[i]) + "\n" + str(account_balance[i]) + "\n" + str(account_name[i]) + "\n")

    quit()


#Function main that starts the program execution
def main():

    welcome("Welcome to Super Bank")

    bank_account, account_balance, account_name = get_data("bank")

    while True:

        choice = get_choice()

        # Condition that processes choice 1 of creating a new bank account
        if choice == 1:

            create_bank_account(bank_account, account_balance, account_name)


        # Condition that processes choice 2 of deleting a current bank account
        elif choice == 2:

            delete_account(bank_account, account_balance, account_name)

        # Condition that processes choice 3 of withdrawing money from a bank account
        elif choice == 3:

            withdraw_money(bank_account, account_balance)

        # Condition that processes choice 4 of depositing money on a bank account
        elif choice == 4:

            deposit_money(bank_account, account_balance)

        # Condition that processes choice 5 of presenting a report for management
        elif choice == 5:

            management_report(bank_account, account_balance, account_name, welcome)

        # Condition that processes choice 6 exiting program and writing data from lists to file
        else:

            finish(bank_account, account_balance, account_name, "bank")

main()