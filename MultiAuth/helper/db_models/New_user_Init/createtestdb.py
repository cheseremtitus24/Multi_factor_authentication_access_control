import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def main():
    database = r"cheserem.db"

    sql_create_users_table = """ CREATE TABLE IF NOT EXISTS users (
                                        user_id INTEGER PRIMARY KEY, first_name VARCHAR(254), last_name VARCHAR(254), National_ID VARCHAR(254) unique, contact_number VARCHAR(15), Email TEXT
                                    ); """
    sql_create_accounts_table = """ CREATE TABLE IF NOT EXISTS accounts( account_number VARCHAR(10) PRIMARY KEY, user_id INTEGER," \
               "account_type varchar (254) DEFAULT 'Saving_Account', balance decimal NOT NULL DEFAULT 0, " \
               "CHECK(balance >= 0), FOREIGN KEY (user_id) REFERENCES users(user_id) ON UPDATE CASCADE ON DELETE " \
               "RESTRICT) ); """
    sql_create_atms_table = """ CREATE TABLE IF NOT EXISTS atms( atm_number VARCHAR(254) PRIMARY KEY ,atm_place VARCHAR(254),atm_cash_limit VARCHAR(254)); """
    sql_create_account_open_table = """ CREATE TABLE IF NOT EXISTS account_open(create_date VARCHAR(25), user_id INTEGER, account_number VARCHAR(254), atm_number VARCHAR(254), FOREIGN KEY (user_id) REFERENCES users(user_id) ON UPDATE CASCADE on DELETE RESTRICT,FOREIGN KEY (account_number) REFERENCES accounts(account_number) ON UPDATE CASCADE on DELETE RESTRICT ); """
    sql_create_card_auth_table = """CREATE TABLE IF NOT EXISTS card_auth(user_id INTEGER,account_number varchar(254),
    pin INTEGER(4), FOREIGN KEY (user_id) REFERENCES users(user_id) ON UPDATE CASCADE); """
    sql_create_face_rec_table = """ CREATE TABLE IF NOT EXISTS rec_auth (user_id INTEGER, user varchar(254), FOREIGN KEY (user_id) REFERENCES users(user_id) ON UPDATE CASCADE); """
    sql_create_transaction_table = """ CREATE TABLE IF NOT EXISTS transact(creation_date VARCHAR(25), user_id INTEGER, account_number VARCHAR(254), atm_number VARCHAR(254),transaction_type VARCHAR(100), FOREIGN KEY (user_id) REFERENCES users(user_id) ON UPDATE CASCADE on DELETE RESTRICT,FOREIGN KEY (account_number) REFERENCES accounts(account_number) ON UPDATE CASCADE on DELETE RESTRICT ); """

    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create users table
        create_table(conn, sql_create_users_table)

        # create accounts table
        create_table(conn, sql_create_accounts_table)

        # create atms table
        create_table(conn, sql_create_atms_table)

        # create account_open table
        create_table(conn, sql_create_account_open_table)
        #
        # # create card_auth table
        create_table(conn, sql_create_card_auth_table)
        #
        # # create face_rec table
        create_table(conn, sql_create_face_rec_table)
        #
        # # create transaction table
        create_table(conn, sql_create_transaction_table)
    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()
