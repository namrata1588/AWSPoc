import sys
import logging
import pyodbc

logger=logging.getLogger()


try:
    conn=pyodbc.connect("DRIVER={ODBC Driver 13 for SQL Server}; SERVER=mydbint.c0o7ubjnd3mm.ap-south-1.rds.amazonaws.com;PORT=1433;DATABASE=rdsadmin;UID=namana;PWD=emids123")
except:
    logger.error("Error:unexpected error:could not connect to sql server")
    print('Exception')
    sys.exit()

logger.info("success:connection to successful")
print('Sucess')
def handler_name():
    print('temp')
    crsr = conn.cursor()
    rows = crsr.execute("select @@VERSION").fetchall()
    print(rows)
    logger.info(rows)
    crsr.close()
    conn.close()
handler_name()
