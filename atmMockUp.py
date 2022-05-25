acctNum = int (input("what is your Account No \n"))
allowedAcct = [1111,2222,3333,4444,5555]
acctNames = ["Ibukun","Tolu","Tope","Paul","Praise"]
allowedPin = ["aaaa","bbbb","cccc","dddd","eeee"]
if(acctNum in allowedAcct):
    # acctPin = input("what is your pin \n")
    nameId = allowedAcct.index(acctNum) #getting the index of the account number entered from the accoutn numnber list
    # print(nameId)
    # if(acctPin == allowedPin[nameId]):
    print("%s, welcome to our bank" %acctNames[nameId])
    print("Please select an option")
    print("1. Cash withdrawal \t 2. Cash transfer")
    print("3. Cash deposit \t 4. Mobile top up")
    print("5. Change Pin \t\t 6. Others")
    selectedOption = int(input("input a number to proceed: \n"))
    if (selectedOption == 1):
        print("%s, welcome to our bank" %acctNames[nameId])
        print("Select Account type")
        print("1. Saving")
        print("2. Current")
        selectedOptionForAcctType = int(input("input a number to proceed: \n"))
        if (selectedOptionForAcctType == 1 or selectedOptionForAcctType == 2):
            print("%s, welcome to our bank" %acctNames[nameId])
            amount = input("Enter Amount: \n")
            if amount.isdigit():
                acctPin = input("input your pin: \n")
                if(acctPin == allowedPin[nameId]):
                    print("%s, welcome to our bank" %acctNames[nameId])
                    print("Transaction successfull please take your cash")
                else:
                    print("incorrect password please try again")
            else:
                print("please input a valid amount")    
        else:
            print("Invalid selection please try again")
    elif(selectedOption == 2):
        print("%s, welcome to our bank" %acctNames[nameId])
        reciverAccctNo = input("Enter The Receiver Account Number \n")
        if reciverAccctNo.isdigit():
            print("Select the Receiver Account type")
            print("1. Saving")
            print("2. Current")
            selectedOptionForAcctType = int(input("inpute a number to proceed: \n"))
            if (selectedOptionForAcctType == 1 or selectedOptionForAcctType == 2):
                print("%s, welcome to our bank" %acctNames[nameId])
                amount = input("Enter amount to trasfer: \n")
                if amount.isdigit():
                    acctPin = input("input your pin: \n")
                    if(acctPin == allowedPin[nameId]):
                        print("Hi %s, you have succefully transfered the sum of $%s to account Number %s." %(acctNames[nameId],amount,reciverAccctNo))
                        print("Thank you for banking with us")
                    else:
                        print("incorrect password please try again")
                else:
                    print("please enter a valid amount.")
            else:
                print("invalid input please try again")
        else:
            print("Please enter a valid account number")
    elif(selectedOption == 3):
        print("Cash deposited, thank you for banking with us.")
    elif(selectedOption == 4):
        print("%s, Welcome to our bank" %acctNames[nameId])
        print("Please select an option")
        print("Choose your network")
        print("1. MTN \t 2. Airtel")
        print("3. GLO \t 4. Etisalat")
        rechargeOption = int(input("select an option \n"))
        if (rechargeOption == 1 or rechargeOption == 2 or rechargeOption == 3 or rechargeOption == 4):
            rechargeNumber = input("Enter the phone number to recharge \n")
            print("%s Has been recharged successful." %rechargeNumber)
            print("Thank you for banking with us.")
        else:
            print("Invalid selection please try again")
    elif(selectedOption == 5):
        print("pin changed successfully")
    elif(selectedOption == 6):
        print("thank you for banking wiht us")
    else:
        print("Invalid selection please try again")
    # else:
    #     print("incorrect password please try again")
else:
    print("Invalid Acct number please try again")