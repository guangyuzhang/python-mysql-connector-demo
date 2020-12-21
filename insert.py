import logging
from logging.handlers import RotatingFileHandler
import mysql.connector
import config


########################################################################################################################
# PROCEDURES:
# Step 1: Select all Contacts from tbl_contacts
# Step 2: Print the result
# Step 3: Insert your contact into tbl_contacts
########################################################################################################################
def main(logger):
    # TODO

    mydb = mysql.connector.connect(**config.config)
    mycursor = mydb.cursor()

    insert = ("INSERT INTO tbl_contacts "
              "(id,name,uuid,email,phone,description) "
              "VALUES(%s,%s,%s,%s,%s,%s)")
    insert_data = {
            'id': 327,
            'name': 'Dongchuan Yang',
            'uid': 'asdf3e34-e3d0-234d-w3e2-w3e2e44r5twg4',
            'email': '1277885105@qq.com',
            'phone': '+8615723072896',
            'description': 'building ',
        }
    mycursor.execute(insert, insert_data)
    mydb.commit()

    mycursor.cloce()
    mydb.close()


if __name__ == "__main__":
    """main"""
    # create logger
    logger = logging.getLogger('mysql-connector-demo')
    # specifies the lowest-severity log message a logger will handle,
    # where debug is the lowest built-in severity level and critical is the highest built-in severity.
    # For example, if the severity level is INFO, the logger will handle only INFO, WARNING, ERROR, and CRITICAL
    # messages and will ignore DEBUG messages.
    logger.setLevel(logging.ERROR)
    # create file handler which logs messages
    fh = RotatingFileHandler('mysql-connector-demo.log', maxBytes=1024 * 1024, backupCount=1)
    # create formatter and add it to the handlers
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    # add the handlers to logger
    logger.addHandler(fh)

    main(logger)
