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
    # TODO
    cnx = None
    cursor = None
    try:
        cnx = mysql.connector.connect(**config.myems_demo_db)
        cursor = cnx.cursor()

        query = ("SELECT * FROM tbl_energy_categories")

        cursor.execute(query)

        for (id, name, uuid, unit_of_measure, kgce, kgco2e) in cursor:
            print("id:{}, name:{}, uuid:{}, unit_of_measure:{}, kgce:{}, kgco2e:{}".format(id, name, uuid, unit_of_measure, kgce, kgco2e))

        query = ("DELETE FROM tbl_energy_categories WHERE name=%(name)s")

        cursor.execute(query,{"name":"中水"})

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
