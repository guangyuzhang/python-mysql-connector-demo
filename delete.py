import logging
from logging.handlers import RotatingFileHandler
import mysql.connector
import config


########################################################################################################################
# PROCEDURES:
# Step 1: Select all Energy Categories from tbl_energy_categories
# Step 2: Print the result
# Step 3: Delete '中水' from tbl_energy_categories
########################################################################################################################
def main(logger):
    connect = None
    cursor = None
    try:
        connect = mysql.connector.connect(**config.myems_demo_db)
        cursor = connect.cursor()
        sql_query = "select id,name,uuid,unit_of_measure,kgce,kgco2e from tbl_energy_categories"
        sql_delete = "DELETE FROM tbl_energy_categories WHERE name =%s"
        val = ("中水",)
        cursor.execute(sql_query)
        for res in cursor.fetchall():
            print(res)
        cursor.execute(sql_delete, val)
        connect.commit()
        print(cursor.rowcount, "条记录已删除")
    except Exception as e:
        logger.error("Error in delete process" + str(e))
    else:
        logger.info("delete success")
    finally:
        if cursor:
            cursor.close()
        if connect:
            connect.close()

if __name__ == "__main__":
    """main"""
    # # create logger
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