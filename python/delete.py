

from connecttomysqldb import *
from helper import *



def delete(conn, eid):
   
    cursor = conn.cursor()

   
    query = '''DELETE FROM employee WHERE id = %s;'''

    try:
        record = get_by_id(cursor, eid)
        if record is None:
            print('Employee id = {} not found'.format(eid))
        else:
           
            cursor.execute(query, [eid])
          
            conn.commit()

            print('Employee id = {} deleted successfully'.format(eid))
    except(Exception, Error) as error:
        print(error)
    finally:
        if conn is not None:
            cursor.close()
            conn.close()
            print('\nConnection closed')



if __name__ == '__main__':
    # connect to database and delete a record
    delete(connect(), 5)
