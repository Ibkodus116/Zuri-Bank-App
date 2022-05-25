# ------------------------------------------------------------------------
# to do things, Bank Authy app
#       _____________________________
#      |_________Register___________|
#     |-username and password email|
#    |-Genrate user ID            |
#   |____________________________|


#     ________________________________
#    |Login                          |
#   |-username or email and password|
#  |-bank operations               |
# |_______________________________|
# ------------------------------------------------------------------------
from xml.dom import UserDataHandler
import random
from pkg_resources import to_filename
import userData
import validation


# userData = {
# #     7184847452 : ["odusanya", "Adewale", "wap", "aaaa", 2000, 1234], # first_Name, last_Name,userMail, userPassword, acct_balance, fourDigitPin
# #     7184847931 : ["ibk", "Ade", "paw", "bbbb", 2500, 1111] # first_Name, last_Name,userMail, userPassword, acct_balance, fourDigitPin
# }


def initialise():
    # condition = False
    # while condition == False:
    print("welcome to myBank")
    haveAccount = int(input("Do you have an account with us: 1(Yes) 2(No) \n"))
    if (haveAccount == 1):
        # condition =True
        login()
    elif (haveAccount == 2):
        # condition =True
        register()
    else:
        print("you have selected an invalid option")
        # init()


def register():
    first_Name = input("What's your First name \n")
    last_Name = input("What's your Last name \n")
    userMail = input("input a valid Email \n")
    userPassword = input("Choose a Password \n")
    fourDigitPin = (input("Choose a transaction pin \n"))
    acct_balance = 0
    accountNumber = generateAccountNumber()

    # --------------------------------------------------------
    is_user_created = userData.create(
        accountNumber, first_Name, last_Name, userMail, userPassword, str(acct_balance), fourDigitPin)

    if (is_user_created):
        print("Your Account has been created")
        print("Your Account number is %d" % accountNumber)
    else:
        print("Something went wrong, please try agian")

    # --------------------------------------------------------
    # print(input("press Enter to proceed to login..."))
    print(userData)
    login(accountNumber)
    # exit()


def login():
    global enter_acct_number
    enter_acct_number = input("Enter your Account Number to login \n")
    # for accountNumber, userData in userData.items(): ///was trying to loop

    is_valid_account = validation.acct_number_validation(enter_acct_number)

    if is_valid_account:

        userPassword = input("input your Password \n")

        user = userData.authenticated_user(enter_acct_number, userPassword)

        if user:
            bankOperation(user)

    else:
        print("Account number isn't valid please check account Number and try again")
        initialise()


def check(user_acct_number):
    print("Hi %s %s, your account number is %d" % (
        userData[user_acct_number][0], userData[user_acct_number][1], userData[user_acct_number]))
    print("Your acct balance is %d" % userData[user_acct_number][4])


def bankOperation(user_acct_number):
    print("Hi, %s %s what operation will you like to perform" % (
        user_acct_number[0], user_acct_number[1]))
    print("1. withdraw \t \t 2. deposit")
    print("3. account balance \t 4. log out")
    bankOperationInput = int(input("choose an option \n"))
    if (bankOperationInput == 1):
        withdraw(enter_acct_number)
    if (bankOperationInput == 2):
        deposit(enter_acct_number)
    if (bankOperationInput == 3):
        balance(enter_acct_number)
    if (bankOperationInput == 4):
        logout()
    else:
        print("you've selected an invalid option! Try again")
        bankOperation(user_acct_number)


def withdraw(enter_acct_number):
    # user =
    amount = int(input("Enter amount to wihdraw \n"))


# ----------------------------DEPOSIT-----------------------------------------
def deposit(user_acct_number):
    amount = int(input("how much will you like to deposit \n"))
    previous_balance = userData.user_acct_balance(user_acct_number)
    new_balance = amount + previous_balance
    

    print("your Deposit was successful, your account balance is %d" %
          new_balance)
    # userData[user_acct_number][4] = str(new_balance)
        #   Coming back to write a try and except 
    backToOppration = int(
        input("Do you want to perform another transaction 1.Yes 2. No \n"))
    if (backToOppration == 1):
        bankOperation(enter_acct_number)
    elif (backToOppration == 2):
        print("Thank you for banking with us!")
        exit()
    else:
        print("You've selected an invalid option please try again")
        deposit(user_acct_number)
# -------------------------CHECK ACCOUNT BALANCE----------------------------------


def balance(user_acct_number):
    pin = int(input("To check your account balance input your Four Digit PIN \n"))
    if (pin == user_acct_number[5]):
        print("your account balance is %d" % userData[user_acct_number][4])
    backToOppration = int(
        input("Do you want to perform another transaction 1.Yes 2. No \n"))
    if (backToOppration == 1):
        bankOperation(enter_acct_number)
    elif (backToOppration == 2):
        print("Thank you for banking with us!")
        exit()
    else:
        print("You've selected an invalid option please try again")
        deposit()


# ---------------------------------------------------------------------
def logout():
    print("thank you for banking with us")
    register()
# ---------------------------------------------------------------------


def generateAccountNumber():
    return random.randrange(111111111, 9999999999)


# accountNumber = generateAccountNumber()

initialise()
# register()
# acct_number_validation("123456789a")
# bankOperation()
# print(accountNumber)
