# # import logging
# # from logging.handlers import RotatingFileHandler
# import mysql.connector
# import config
#
#
# ########################################################################################################################
# # PROCEDURES:
# # Step 1: Select all Contacts from tbl_contacts
# # Step 2: Print the result
# # Step 3: Insert your contact into tbl_contacts
# ########################################################################################################################
# def main(logger):
#     # TODO
#     connect = None
#     cursor = None
#     try:
#         connect = mysql.connector.connect(**config.myems_demo_db)
#         cursor = connect.cursor()
#         sql_query = "select id,name,uuid,email,phone,description from tbl_contacts"
#         sql_insert = "insert into tbl_contacts (name,uuid,email,phone,description) values (%s,%s,%s,%s,%s)"
#         val = ("zhenhuiCao", "1","823914102@qq.com",'15730322347',"test")
#         cursor.execute(sql_query)
#         for res in cursor.fetchall():
#             print(res)
#         cursor.execute(sql_insert, val)
#         connect.commit()
#         print(cursor.rowcount, "条记录已插入")
#     except Exception as e:
#         logger.error("Error in insert process" + str(e))
#     else:
#         logger.info("insert success")
#     finally:
#         if cursor:
#             cursor.close()
#         if connect:
#             connect.close()
#
#
#
# if __name__ == "__main__":
#     """main"""
#     # create logger
#     logger = logging.getLogger('mysql-connector-demo')
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
#
#     main(logger)
