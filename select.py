import logging
from logging.handlers import RotatingFileHandler
import mysql.connector
import config
from datetime import datetime

########################################################################################################################
# PROCEDURES:
# Step 1: Select all space from tbl_spaces
# Step 2: Print the result
########################################################################################################################
def main(logger):
    cnx = None
    cursor = None
    try:
        cnx = mysql.connector.connect(**config.myems_demo_db)
        cursor = cnx.cursor()
        cursor.execute("SELECT * FROM tbl_spaces")
    except mysql.connector.Error as err:
        if err.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
            logger.error("Something is wrong with your user name or password" + str(err))
        elif err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
            logger.error("Database does not exist" + str(err))
        else:
            logger.error("Error in selectc SQL syntax" + str(err))
    else:
        for item in cursor.fetchall():
            print(item)
        logger.info("selecte success in:" + str(datetime.now()))
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
