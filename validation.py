# ___________________________________________________________________________
def acct_number_validation(user_acct_number):  # Validation block ---        |
    # check if acct number is 10 digit             very important            |
    # check if acct number isn't empty                                       |
    # check if acct number is an integer                                     |
                                                                        #    |
    if user_acct_number:                                                #    |
                                                                        #    |
        try:                                                            #    |
            int(user_acct_number)                                       #    |
                                                                        #    |
            if len(str(user_acct_number)) == 10:                        #    |
                return True                                             #    |
                                                                        #    |
              # print("Acct number can't be less or more than 10 digit")#    |
        except ValueError:                                              #    |
                return False                                            #    |
        except TypeError:                                               #    |
            # print("this can't be converted to an intiger")            #    |
                return False                                            #    |
                                                                        #    |
                                                                        #    |
    else:                                                               #    |
        # print("Acct number can't be emtpy")                           #    |
        return False                                                    #    |
# ___________________________________________________________________________|