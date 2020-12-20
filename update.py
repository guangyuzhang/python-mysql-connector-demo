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
    # TODO
    cnx = None
    cursor = None
    try:
        cnx = mysql.connector.connect(**config.myems_demo_db)
        cursor = cnx.cursor()
        query=(" select * from tbl_versions " )
        cursor.execute(query)
        for item in cursor.fetchall():
            print(item)
        today_time = datetime.now()
        update_date=('2.0.0',today_time)
        update = "update tbl_versions set version=%s,release_date=%s where id='1'"
        cursor.execute(update,update_date)
        cnx.commit()
    except Exception as e:
        logger.error("Error in select process" + str(e))
    else:
        logger.info("update success")
        print("update success")
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
