import logging
from logging.handlers import RotatingFileHandler
import mysql.connector
import config
from datetime import *

########################################################################################################################
# PROCEDURES:
# Step 1: Select the version from tbl_versions
# Step 2: Print the result
# Step 3: Update the version to '2.0.0' and release_date to today.
########################################################################################################################
def main(logger):
    # TODO
    try:
        cnx = mysql.connector.connect(**config.myems_demo_db)
    except mysql.connector.Error as e:
        print('connect fails{]'.format(e))
    cursor = cnx.cursor()
    try:
        mysql_query = 'select * from tbl_versions'
        cursor.execute(mysql_query)
        for item in cursor.fetchall():
            print(item)
        update_ver = "update tbl_versions set version=%s,release_date=%s where id='1'"
        time = datetime.now()
        data_ver = ('2.0.0',time)
        cursor.execute(update_ver,data_ver)
        cnx.commit()
    except mysql.connector.Error as e:
        logger.error('update error!'+str(e))
        print('update error!{}'.format(e))
    else:
        logger.info("update success")
        print("update success!")
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
    # main()