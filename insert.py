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
    cnx = None
    cursor = None
    try:
        cnx = mysql.connector.connect(**config.myems_demo_db)
        cursor = cnx.cursor()

        query = ("SELECT * FROM tbl_contacts")

        cursor.execute(query)

        for (id, name, uuid, email, phone, description) in cursor:
            print("id:{}, name:{}, uuid:{}, email:{}, phone:{}, description:{}".format(id, name, uuid, email, phone, description))

        query = ("INSERT INTO tbl_contacts VALUES (%s, %s, %s, %s, %s, %s)")

        insert_date = (None,'ZY','5c5ce6e8-8d00-46b3-9602-4e1520a8bDSW', '2533470000@qq.com', '+8613888886666', 'Building #2')

        cursor.execute(query,insert_date)

        cnx.commit()

    except Exception as e:
        cnx.rollback()
        logger.error(str(e))

    finally:
        if cursor:
            cursor.close()
        if cnx:
            cursor.close()


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
