import mysql.connector
import delete
import insert
import select
import update
import logging
from logging.handlers import RotatingFileHandler
myems_demo_db = {
    'user': 'sql12382808',
    'password': 'CvugQvJ8pr',
    'host': 'sql12.freemysqlhosting.net',
    'database': 'sql12382808',
    'port': 3306,
}

# if __name__ == "__main__":
#     """main"""
#     # create logger
#     logger = logging.getLogger('mysql-connector-demo1')
#     # specifies the lowest-severity log message a logger will handle,
#     # where debug is the lowest built-in severity level and critical is the highest built-in severity.
#     # For example, if the severity level is INFO, the logger will handle only INFO, WARNING, ERROR, and CRITICAL
#     # messages and will ignore DEBUG messages.
#     logger.setLevel(logging.ERROR)
#     # create file handler which logs messages
#     fh = RotatingFileHandler('mysql-connector-demo.log', maxBytes=1024 * 1024, backupCount=1)
#     # create formatter and add it to the handlers
#     formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#     fh.setFormatter(formatter)
#     # add the handlers to logger
#     logger.addHandler(fh)
#     delete.main(logger)
#     select.main(logger)
#     insert.main(logger)
#     update.main(logger)