


def get_records_count(cursor):
    
    cursor.execute('''SELECT * FROM employee;''')
    return len(cursor.fetchall())



def get_by_id(cursor, eid):
   
    query = '''SELECT * FROM employee WHERE id = %s;'''
   
    cursor.execute(query, [eid])
    return cursor.fetchone()
