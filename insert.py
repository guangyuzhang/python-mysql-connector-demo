import logging
from logging.handlers import RotatingFileHandler
import mysql.connector
import config
import uuid


########################################################################################################################
# PROCEDURES:
# Step 1: Select all Contacts from tbl_contacts
# Step 2: Print the result
# Step 3: Insert your contact into tbl_contacts
########################################################################################################################
def main(logger):
    # TODO
    cnx = None
    cursor = None
    try:
        cnx = mysql.connector.connect(**config.myems_demo_db)
        cursor = cnx.cursor()
        cursor.execute("select * from  tbl_contacts")
        for item in cursor.fetchall():
            print(item)
        insert = ('INSERT INTO tbl_contacts '
                      '(id,name,uuid,email,phone,description) '
                      'VALUES(%s,%s,%s,%s,%s,%s)')
        uuid_number=str(uuid.uuid1())

        insert_data = (None, 'malizheng', uuid_number, 'mlz@myems.io', '+8615736158996', 'Building ')
        cursor.execute(insert,insert_data)
        cnx.commit()
    except Exception as e:
        logger.error("Error in insert process" + str(e))
    else:
        logger.info("insert success ")
        print("insert success")
    finally:
        if cursor:
            cursor.close()
        if cnx:
            cnx.close()


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
