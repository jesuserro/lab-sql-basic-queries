import mysql.connector
from mysql.connector import errorcode
import configparser

# Read database configuration from db.cfg
config = configparser.ConfigParser()
config.read('db.cfg')

try:
    db_config = {
        'user': config['database']['user'],
        'password': config['database']['password'],
        'host': config['database']['host'],
        'database': config['database']['database']
    }
except KeyError as e:
    print(f"Missing key in configuration file: {e}")
    exit(1)

# Read the SQL schema file
try:
    with open('data/sakila-schema.sql', 'r') as file:
        sql_commands = file.read()
except FileNotFoundError as e:
    print(f"SQL schema file not found: {e}")
    exit(1)

# Split the SQL commands by delimiter
commands = sql_commands.split('DELIMITER ;')

# Connect to the MySQL database and execute the SQL commands
try:
    cnx = mysql.connector.connect(**db_config)
    cursor = cnx.cursor()
    for command in commands:
        subcommands = command.split(';')
        for subcommand in subcommands:
            if subcommand.strip():
                cursor.execute(subcommand)
                print(f"Executed: {subcommand.strip()}")
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