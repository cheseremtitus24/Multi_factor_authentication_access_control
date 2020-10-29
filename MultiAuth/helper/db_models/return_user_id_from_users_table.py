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
def get_user_id(National_ID,last_name):
    con_obj = con()
    # TODO: Think of all scenarios i.e. when uid not exist or account_number passed in not exist fix below
    mycursor = con_obj.cursor()
    # TODO: How to trim string input in python
    ID = str(National_ID)
    name = str(last_name)
    test_exist = f"select case when exists ( select user_id from [users] where National_ID = '{ID}' and last_name = '{name}') then cast (1 as bit) else cast (0 as BIT) end"
    user_id_retrieve = f"select user_id from users where National_ID='{ID}' and last_name = '{name}'"
    mycursor.execute(test_exist)

    var = mycursor.fetchone()
    if var[0]:
        print("Entry Exists!")
        print(var[0])
        mycursor.execute(user_id_retrieve)
        user_id = mycursor.fetchone()
        print(user_id[0])
        return user_id[0]

    else:
        print("Account Not Exist...")
        # print(var[0])
        return False
    con_obj.close()

# return_card_pin("Happy ",'3')

