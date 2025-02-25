import mysql.connector
from mysql.connector import errorcode

# Read database configuration from db.cfg
import configparser

config = configparser.ConfigParser()
config.read('db.cfg')

db_config = {
    'user': config['database']['user'],
    'password': config['database']['password'],
    'host': config['database']['host'],
    'database': config['database']['database']
}

# Read the SQL schema file
with open('data/sakila-schema.sql', 'r') as file:
    sql_commands = file.read()

# Connect to the MySQL database and execute the SQL commands
try:
    cnx = mysql.connector.connect(**db_config)
    cursor = cnx.cursor()
    for result in cursor.execute(sql_commands, multi=True):
        if result.with_rows:
            print("Rows produced by statement '{}':".format(result.statement))
            print(result.fetchall())
        else:
            print("Number of rows affected by statement '{}': {}".format(result.statement, result.rowcount))
    cnx.commit()
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    cursor.close()
    cnx.close()