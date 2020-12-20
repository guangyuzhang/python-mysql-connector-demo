import logging
from logging.handlers import RotatingFileHandler
import mysql.connector
import config
from datetime import datetime

########################################################################################################################
# PROCEDURES:
# Step 1: Select the version from tbl_versions
# Step 2: Print the result
# Step 3: Update the version to '2.0.0' and release_date to today.
########################################################################################################################
def main(logger):
    cnx = None
    cursor = None
    try:
        cnx = mysql.connector.connect(**config.myems_demo_db)
        cursor = cnx.cursor()
        cursor.execute("SELECT * FROM tbl_versions")
    except mysql.connector.Error as err:
        if err.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
            logger.error("Something is wrong with your user name or password" + str(err))
        elif err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
            logger.error("Database does not exist" + str(err))
        else:
            logger.error("Error in select SQL syntax" + str(err))
        if cursor:
            cursor.close()
        if cnx:
            cnx.close()
        return
    else:
        for item in cursor.fetchall():
            print(item)
    today = datetime.today()
    update = ('UPDATE tbl_versions '
              'SET version = %s , release_date = %s')
    update_data = ('2.0.0', today)
    try:
        cursor.execute(update, update_data)
        cnx.commit()
    except mysql.connector.Error as err:
        logger.error("Error in update SQL syntax" + str(err))
    else:
        logger.info("update success in:" + str(datetime.now()))
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
