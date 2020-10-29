import sqlite3
from sqlite3 import Error

#TODO: Convert the helper class into classes so that it can be possible
# minimize code through inheritance
def con():
    try:
        conn = sqlite3.connect('titus.db')
        if conn:
            print("connection successful")
            return conn
    except Error:
        print(f"Connection failed {Error}")
def return_uid(account_number):
    con_obj = con()
    mycursor = con_obj.cursor()
    # test2 = f"select case when exists ( select * from [accounts] where 'account_number' = {account_number}) then cast (1 as bit) else cast (0 as BIT) end"
    test1 = f"select user_id from accounts where account_number='{account_number}'"
    mycursor.execute(test1)
    var = mycursor.fetchone()
    # print(var)
    if var[0]:
        print("Account Number Exists!")
        return var[0]

    else:
        print("Account Not Exist...")
        # print(var[0])
        return None
    con_obj.close()
# account = "Happy"
# val = return_uid(account)
# print(val)
