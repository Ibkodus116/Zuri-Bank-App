# Create record
# Update record
# read record
# delete record
# CURD - this is called the CURD opperation
# Find User

import os
from posixpath import split
import re  # This is needed to be imported when you want to delete a file in DB
import validation
user_db_path = "data/user_record/"


def create(user_account_number,first_Name, last_Name, userMail, userPassword, fourDigitPin, acct_balance):
    # print("Creat a new user record")
    # Creat a file
    
    user_data = first_Name + "," + last_Name + "," + userMail + "," + userPassword + "," + str(acct_balance) + fourDigitPin 

    if check_acct_no(user_account_number):
        return False

    if check_mail(userMail):
        print("User already exist")
        return False

    completion_state = False

    try:
        # name of the file should be accountNumber.txt
        # Saves the file in txt format. The "x" is a parameter used in creating folder
        f = open(user_db_path + str(user_account_number) + ".txt", "x")

    except FileExistsError:  # if saving to file fails, then delete created file
        # delete(user_account_number)
        # Check content of file before deleting
        # if it has a user details don't delete it
        does_file_contain_data = read(user_db_path + str(user_account_number) + ".txt")
        
        if not does_file_contain_data:
            delete(user_account_number)


    else:
        # add the user details to the file
        f.write(str(user_data))  # this line of code continues from the top
        # return true
        completion_state = True

    finally:
        # When creating a database it's neccesary to close the file at the end.
        f.close()
        return completion_state


def read(user_account_number):
    # find user with account number
    # fetch the content of the file
    is_valid_account_number = validation.acct_number_validation(
        user_account_number)

    try:

        if is_valid_account_number:

            # this open the folder to read, the "r" parameter make the reading possible
            f = open(user_db_path + str(user_account_number) + ".txt", "r")
            # print("read user record")
        else:
            # this will run when is valid account return false
            f = open(user_db_path + user_account_number, "r")

    except FileNotFoundError:
        print("This file wasn't found")
    except FileExistsError:
        print("This file doesn't exist")
    except TypeError:
        print("accct number isn't valid")
    # finally:
    #     print("thank you")
    else:
        return f.readline()

    return False



def update(user_account_number):
    # find user with account number
    # fetch the content of the file
    # update the content of the file
    # save the file
    print("Update user record")




def delete(user_account_number):
    is_file_deleted = False
    # find user with account number
    # if (os.path.exists(user_db_path + str (user_account_number) + '.txt')):

    try:
        os.remove(user_db_path + str(user_account_number) + '.txt')
        # delete the user record
        # Return true
        print("delete user record")
        is_file_deleted = True
        print("File was deleted succesfully")

    except FileNotFoundError:
        print("this file was never created")

    finally:
        return print(is_file_deleted)




def check_mail(email):
    # this lists out all the info in the dataBase
    all_user = os.listdir(user_db_path)

    for user in all_user:
        user_info = str.split(read(user), ",")

        if email in user_info:
            return True

    return False




def check_acct_no(acct_number):
    # this lists out all the info in the dataBase
    all_user = os.listdir(user_db_path)
    # print("a user alreadyy has this email")

    for user in all_user:
        user_info = str(acct_number) + ".txt"

        if user == user_info:
            return True

    # print("user printed --> %s" %user)
    return False


def authenticated_user(user_account_number, user_password):
    if check_acct_no(user_account_number):
        user = str.split(read(user_account_number), ",")

        if user_password == user[3]:
            return user

    return False



# def user_acct_balance(user_account_number):
#     if check_acct_no(user_account_number):
#         user = str.split(read(user_account_number), ",")

        
    # return (int(user[4]))


# print(read(5223641681))

# read(["522364168dl",3445])
# print(check_acct_no(5630716206))
# print(user_acct_balance(5630716206))
