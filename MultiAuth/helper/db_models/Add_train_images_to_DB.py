import os
import sqlite3
from datetime import datetime
from sqlite3 import Error

def con(db):
    try:
        con = sqlite3.connect(f"{db}")
        print("Connection to Auth DB success")
        return con
    except Error:
        print(Error)

def query_Accounts_for_uid_n_account():
    connection = con('titus.db')
    mycursor = connection.cursor()
    query = "Select user_id, account_number from accounts where user_id = 3"
    mycursor.execute(query)
    holder = mycursor.fetchmany()
    for item in holder:
        print(holder)
    # print(holder)

def save_classification_to_table(classification):
    connection = con('rec_auth')
    mycursor = connection.cursor()
    wakati = datetime.now() #Save current time of update
    # query =
    # TODO: How to insert classifications with
    # matching User ID in the correct rows
    # You'll need a table with mappings btwn userid and account_number
    # Solved!!! make use of Accounts TABLE
    '''
    Solution STEPS
    1. Query the table and save account and user id in a dictionary
    2. use a for loop to add classifications to db
    3. make use of switch case for correct mapping before inserting to db
    
    '''



def traverse_images_return_classifications():
    #Get the current working directory
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    #look for the images directory
    image_dir = os.path.join(BASE_DIR,"../../images")
    #save classification in a list
    classifications = list()
    for root, dirs, files in os.walk(image_dir):
        for dir in dirs:
            classifications.append(dir)
    print(classifications)
    return classifications


def face_auth_table(value):
    classifications = traverse_images_return_classifications()
    status = save_classification_to_table(classifications)

query_Accounts_for_uid_n_account()

