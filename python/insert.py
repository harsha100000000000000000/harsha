

from connecttomysqldb import *
from helper import *



def insert(conn):
    cursor = conn.cursor()

   
    query = '''
    INSERT INTO employee (id, first_name, last_name, email, gender, phone) VALUES (%s, %s, %s, %s, %s, %s);
    '''

    try:
        count = get_records_count(cursor)
        if count > 0:
            print('Default data present. Skipping insert')
        else:
            data = [
                (1, 'Marga', 'Cronchey', 'mcronchey0@pen.io', 'F', '314-289-7265'),
                (2, 'Theda', 'Mushrow', 'tmushrow1@whitehouse.gov', 'F', '804-163-9834'),
                (3, 'Marielle', 'Bonicelli', 'mbonicelli2@sitemeter.com', 'F', '624-922-2416'),
                (4, 'Locke', 'Watkinson', 'lwatkinson3@accuweather.com', 'M', '456-260-1052'),
                (5, 'Blakelee', 'Wilcot', 'bwilcot4@twitpic.com', 'M', '608-344-4090')
            ]

           
            cursor.executemany(query, data)
            
            conn.commit()

            print('{} records inserted'.format(cursor.rowcount))
    except(Exception, Error) as error:
        print(error)
    finally:
        if conn is not None:
            cursor.close()
            conn.close()
            print('\nConnection closed')



if __name__ == '__main__':
   
    insert(connect())
