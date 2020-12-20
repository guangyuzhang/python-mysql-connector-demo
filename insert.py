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
    try:
        cnx = mysql.connector.connect(**config.myems_demo_db)
    except mysql.connector.Error as e:
        print('connect fails{]'.format(e))
    cursor = cnx.cursor()
    try:
        mysql_query = 'select * from tbl_contacts'
        cursor.execute(mysql_query)
        for item in cursor.fetchall():
            print(item)
        add_con = ('INSERT INTO tbl_contacts '
                      '(id,name,uuid,email,phone,description) '
                      'VALUES(%(id)s,%(name)s,%(uid)s,%(email)s,%(phone)s,%(description)s)')
        data_con = {
            'id':None,
            'name':'zhongtianlin',
            'uid': str(uuid.uuid1()),
            'email': 'ztl@qq.com',
            'phone': '63351',
            'description': 'building ',
        }
        cursor.execute(add_con,data_con)
        cnx.commit()
    except mysql.connector.Error as e:
        logger.error('insert error!'+str(e))
        print('insert error!{}'.format(e))
    else:
        logger.info("insert success")
        print("insert success!")
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
    fh =logging.handlers.RotatingFileHandler('mysql-connector-demo.log', maxBytes=1024 * 1024, backupCount=1)
    # create formatter and add it to the handlers
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    # add the handlers to logger
    logger.addHandler(fh)

    main(logger)
    # main()