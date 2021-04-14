import time
import random
time_now=time.time()
allowedUsers ={}
def welcome():
    print("Welcome, Please select an option")
    print("1. Login")
    print("2. Register")

    actionSelect = int(input("Select an option \n"))

    if(actionSelect == 1):
        login()

    elif(actionSelect ==2):

        register()
    else:
        print('Invalid Option Selected, Please try again')
    welcome()


def login():
    accountowner = int(input("Please Enter your account number \n"))
    password = input("Input your password \n")

    for accountNumber, userinfo in allowedUsers.items():
        if(accountNumber == accountowner):
            if(userinfo[3] == password):
                bankOperations(userinfo)
    else:
        print('Accouunt Number or Password Incorrect, Please try again')
        login()

def register():
    email = input("please enter your email address \n")
    firstname = input("please enter your first name \n")
    lastname = input("please enter your Last name \n")
    Password = input("please set a password \n")

    accountNumber = generatingAccountNumber()

    allowedUsers[accountNumber] = [firstname, lastname, email, Password ]
    print(allowedUsers[accountNumber])
    print("Your Account has been created, Please Hold")
    time.sleep(2.5)
    print("Your account number is: %d" % accountNumber)
    print("please Login")
    login()



def bankOperations(user):
    print(f"Welcome, {user[0], user[1]}. Current date and time is {time.ctime(time_now)}.")
    print('These are the available options')
    print('.1 Withdrawal')
    print('.2 Deposit')
    print('.3 Complaints')
    print('.4 Logout')

    selectedOption = int(input('Please select an option:  \n'))

    if (selectedOption ==1):
        input(' How much would you like to withdraw?  \n')
        print("Please take your cash")
        time.sleep(2)
        more_options()
        bankOperations()
    elif (selectedOption ==2):
        # print('you selected %s' % selectedOption)
        # bankOperations()
        Deposit= input(' How much would you like to deposit?  \n')
        print(f"Your current balance is: {Deposit}")
        time.sleep(2)
        more_options()
        bankOperations()
    elif (selectedOption ==3):
        input(' What issue will you like to report?  \n')
        print("Thank you for contacting us")
        time.sleep(2)
        more_options()
    elif (selectedOption == 4):
        exit()
    else:
        print('Invalid Option Selected, Please try again')
def generatingAccountNumber():

    return random.randrange(1000000,99999999)

def more_options():
    print('Do you want to perform another transaction')
    print('1.YES')
    print('2. NO')
    availableOption =int(input('Please select an option: \n'))
    if (availableOption == 1):

        login()

    elif (availableOption == 2):
        print("Thank you for banking with us")
        exit()

    else:
        print('Invalid Option Selected, Please try again')


welcome()
