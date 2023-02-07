

from connecttomysqldb import *
from helper import *



def delete_all(conn):
    
    cursor = conn.cursor()

    
    query = '''DELETE FROM employee;'''

    try:
        count = get_records_count(cursor)
        if count == 0:
            print('No data present in db. Skipping delete all')
        else:
          
            cursor.execute(query)
           
            conn.commit()

            print('All data deleted successfully')
    except(Exception, Error) as error:
        print(error)
    finally:
        if conn is not None:
            cursor.close()
            conn.close()
            print('\nConnection closed')



if __name__ == '__main__':
    
    delete_all(connect())
