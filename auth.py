#Register
# - first name, last name, email, password

#Generate account

#Login
# - Accountnumber & password

#Bank Operation

#initializing the system

import random

database = {} #dictionary

def init():
    print('Welcome')
    time_date()
    haveaccount = int(input('Do you have account with us: 1 (Yes) 2 (No) \n'))
    if(haveaccount == 1):
        login()
    elif(haveaccount == 2):
        register()
    else:
        print('You have selected and invalid option')
        init()
        
def login():
    print('Enter your login details')
    input('Enter Account number \n')
    input('Enter Password \n')
    print('Welcome To Bank')
    time_date()
    bankoperation()
    
def register():
    print('***** Registration form *****')
    first_name = input('what is your Fisrt name \n')
    last_name = input('What is your Last name \n')
    email = input('Enter your email adresss \n')
    password = input('create your password \n')

    accountnumber = generateaccountnumber()

    database[accountnumber] = [ first_name, last_name, email, password ]

    print(accountnumber)
    login()

def bankoperation():
    selectedoption = int(input('How can we serve you today: 1 (Deposit) 2 (Withdrawal) 3 (Transfer) 4 (Buy airtime) \n'))
    if(selectedoption == 1):
        account_type()
        input('Enter amount \n')
        print('Money deposited')
    elif(selectedoption == 2):
        account_type()
        input('Enter withdrawal amount \n')
        print('Take your cash')
    elif(selectedoption == 3):
        int(input('Enter account number \n'))
        input('Enter amount')
        account_type()
        print('Transfer successful')
    elif(selectedoption == 4):
        network()
        input('Enter amount \n')
        print('Recharge successful')

def account_type():
    account = int(input('Select your account type: 1 (Savings) 2 (Current) \n'))
    if(account == 1):
        print('Savings account')
    elif(account == 2):
        print('Current account')

def network():
    mobile_network = int(input('Select mobile carrier: 1 (MTN) 2(AIRTEL) 3 (GLO) 4 (9mobile) \n'))

def generateaccountnumber():
    return random.randrange(1111111111, 9999999999)

def time_date():
    from datetime import datetime
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print('Date and Time =', dt_string)


#### Actual Banking System ####


init()
    
