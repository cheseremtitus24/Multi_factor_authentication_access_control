import sqlite3
from sqlite3 import Error

def con():
    try:
        conn = sqlite3.connect('titus.db')
        if conn:
            print("Connection successful")
            return conn
    except Error:
        print(f"Connection failed {Error}")
def return_card_pin(account_number,UID):
    con_obj = con()
    #TODO: Think of all scenarios i.e. when uid not exist or account_number passed in not exist fix below
    mycursor = con_obj.cursor()
    #TODO: How to trim string input in python
    account = str(account_number)
    user_id = str(UID)
    test_exist = f"select case when exists ( select pin from [card_auth] where account_number = '{account}' and user_id = '{user_id}') then cast (1 as bit) else cast (0 as BIT) end"
    pin_retrieve = f"select pin from card_auth where account_number='{account}' and user_id = '{user_id}'"
    mycursor.execute(test_exist)

    var = mycursor.fetchone()
    if var[0]:
        print("Entry Exists!")
        print(var[0])
        mycursor.execute(pin_retrieve)
        pin = mycursor.fetchone()
        print(pin[0])
        return pin[0]

    else:
        print("Account Not Exist...")
        # print(var[0])
        return False
    con_obj.close()

# return_card_pin("Happy ",'3')