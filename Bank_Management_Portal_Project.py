import sqlite3






conn = sqlite3.connect(':memory:')

c = conn.cursor()

c.execute('''CREATE TABLE bank(account integer ,name text, balance real ,branch text,PRIMARY KEY(account))''')

c.execute('''CREATE TABLE trans(account integer, deposit real, withdrawal real ,FOREIGN KEY(account) REFERENCES bank(account),
PRIMARY KEY(account))''')

c.execute("INSERT INTO bank VALUES('101','Thomas','2105.5','Jaipur')")
c.execute("INSERT INTO bank VALUES('102','John','4505.5','Jodhpur')")
c.execute("INSERT INTO bank VALUES('103','Arthur','905.5','Delhi')")


c.execute("INSERT INTO trans VALUES('101', '0.0' , '0.0')")
c.execute("INSERT INTO trans VALUES('102', '0.0' , '0.0')")
c.execute("INSERT INTO trans VALUES('103', '0.0' , '0.0')")


acc = ''
temp_user_balance = 0.0
temp_user_deposit = 0.0
temp_user_withdrawal = 0.0


### FUNCTIONS ###
def insert():
    try:
        add = ''
        while add != 'n':
            acc = input("Enter Account No:")
            name = input("Enter Name :")
            bal = input("Enter Balance:")
            branch = input("Enter Branch name:")
            with conn:
                c.execute("INSERT INTO bank VALUES (?,?,?,?)",(acc , name, bal, branch))
            add = input('Add More Data y/n:')
        welcome()   
    except sqlite3.IntegrityError:
           print('Account Number Already Exist. Enter New Account Number')
           insert() 
    
    
def read():
    c.execute("SELECT * FROM bank LEFT JOIN trans ON bank.account = trans.account")
    data = c.fetchall()
    for i in data:
        print(i)
    menu = input('Press Any Key for Main Menu:')
    welcome()


def update():
    add = ''
    while add != 'n':
        with conn:
            w = input("Select Column for Update eg. account, balance, branch:")
            x = input(f"Enter Row Value from {w}:")
            y = input('Enter What you want to update eg. account, balance, branch:')
            z = input(f"Enter New Value for {y}:")
            c.execute(f"UPDATE bank SET {y}=:y WHERE {w}=:w",{'w':x,'y':z})
            add = input('Update More Data y/n:')    

    welcome()       

def delete():
    with conn:
        w = input("Select Column eg. account, balance, branch :")
        x = input(f"Enter Row Value From {w} to delete :")
        c.execute(f"DELETE FROM bank WHERE {w}=:w",{'w':x})
        read()


def user_account():
    with conn:
        global acc
        acc= input('Enter your account number:')

        try:
            c.execute("SELECT * FROM bank LEFT JOIN trans ON bank.account = trans.account WHERE bank.account=:acc",{'acc':acc})
            details = c.fetchone()
            global temp_user_balance
            global temp_user_deposit
            global temp_user_withdrawal
            temp_user_balance = details[2]
            temp_user_deposit = details[5]
            temp_user_withdrawl = details[6]
            print(f"Hello {details[1]} \n Account No : {details[0]} \n Balance    : {details[2]}\n Branch     : {details[3]}")
            selectusermenu()
        except TypeError:
            print('X-- Enter Valid Account Number --X')
            user_account()
        

def deposit():
    with conn:
        global temp_user_balance
        global temp_user_deposit
        amount = input('Enter your amount:')
        temp_user_balance +=  float(amount)
        temp_user_deposit +=  float(amount)
        c.execute(f"UPDATE bank SET balance=:amount WHERE account=:w",{'w':acc,'amount':temp_user_balance})
        c.execute(f"UPDATE trans SET deposit=:amount WHERE account=:w",{'w':acc,'amount':temp_user_deposit})
        print(f"Amount {amount} has been deposited in account no {acc}.")

def withdrawal():
    with conn:
        global temp_user_balance
        global temp_user_withdrawal
        amount = input('Enter your amount:')
        temp_user_balance -= float(amount)
        temp_user_withdrawal -= float(amount)
        c.execute(f"UPDATE bank SET balance=:amount WHERE account=:w",{'w':acc, 'amount':temp_user_balance})
        c.execute(f"UPDATE trans SET withdrawal=:amount WHERE account=:w",{'w':acc,'amount':temp_user_withdrawal})
        print(f"Amount {amount} has been withdrawl in account no {acc}.")
        
    
    

def transfer():
    with conn:
        
        accTo = input('Enter Recipent Account no: ')
        amount = input('Enter Amount:')
        try:
                
            global temp_user_balance
            global temp_user_withdrawal
            temp_user_balance -= float(amount)
            temp_user_withdrawal -= float(amount)
            c.execute(f"UPDATE bank SET balance=:amount WHERE account=:w",{'w':acc, 'amount':temp_user_balance})
            c.execute(f"UPDATE trans SET withdrawal=:amount WHERE account=:w",{'w':acc,'amount':temp_user_withdrawal})


            c.execute("SELECT * FROM bank LEFT JOIN trans ON bank.account = trans.account WHERE bank.account=:acc",{'acc':accTo})
            details = c.fetchone()
            other_user_balance = details[2]
            other_user_deposit = details[5]

            other_user_balance +=  float(amount)
            other_user_deposit +=  float(amount)
            c.execute(f"UPDATE bank SET balance=:amount WHERE account=:w",{'w':accTo,'amount':other_user_balance})
            c.execute(f"UPDATE trans SET deposit=:amount WHERE account=:w",{'w':accTo,'amount':other_user_deposit})
            print(f"Amount {amount} has been transferred to {details[1]} Account No {accTo}")
        except TypeError:transfer()
    
        
def selectusermenu():
    print(f"Select Option \n 1 Deposit  \n 2 Withdrawal  \n 3 Transfer \n 4 Main Menu")
    userquery = input(">>>")
    selectuseroption(userquery)

def selectmainmenu():
    print(f"Select Option \n 1 Insert Data  \n 2 Show Database  \n 3 Update Data \n 4 Delete Data \n 5 User Account")
    query = input(">>>")
    selectoption(query)
def welcome():
    print("----------X----------")
    print("Welcome to Red Bank")
    selectmainmenu()
def selectoption(query):
    if query == '1':insert(),
    elif query == '2':read(),
    elif query == '3':update(),
    elif query == '4':delete(),
    elif query == '5':user_account(),
    else:print('X-- Select Valid Option: --X')
    selectmainmenu()
def selectuseroption(query):
    if query == '1':deposit(),
    elif query == '2':withdrawal(),
    elif query == '3':transfer(),
    elif query == '4':selectmainmenu()
    else:print('X-- Select Valid Option --X')
    selectusermenu()
welcome()









