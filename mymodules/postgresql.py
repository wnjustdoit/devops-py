#!/usr/bin/env python3

import psycopg2


def get_connection(user, password, database, host, port):
    return psycopg2.connect(user=user, password=password, database=database, host=host, port=port)


def get_cursor(connection):
    return connection.cursor()


def close_cursor(cursor):
    cursor.close()


def close_connection(connection):
    connection.close()


def write_db(sql, params, user, password, database, host='127.0.0.1', port='5432'):
    connection = None
    cursor = None
    try:
        connection = get_connection(user, password, database, host, port)
        cursor = get_cursor(connection)
        cursor.execute(sql, params)
        connection.commit()
        count = cursor.rowcount
        print(count, "Record written successfully into table")
    except (Exception, psycopg2.Error) as error:
        if (connection):
            print("Failed to write record into table", error, params)
    finally:
        # closing database connection.
        if (cursor):
            close_cursor(cursor)
        if (connection):
            close_connection(connection)
            print("PostgreSQL connection is closed")


def select_all(sql, params, user, password, database, host='127.0.0.1', port='5432'):
    connection = None
    cursor = None
    try:
        connection = get_connection(user, password, database, host, port)
        cursor = get_cursor(connection)
        cursor.execute(sql, params)
        records = cursor.fetchall()
        for row in records:
            print('row = ', row)
        return records
    except (Exception, psycopg2.Error) as error:
        if (connection):
            print("Failed to insert record into table", error)
    finally:
        # closing database connection.
        if (cursor):
            close_cursor(cursor)
        if (connection):
            close_connection(connection)
            print("PostgreSQL connection is closed")

# if __name__ == '__main__':
#     write_db("""delete from test where id = %s""", (1),
#              'wangnan', 'postgres', 'devops')
#     write_db("""insert into test(id, name) values(%s, %s)""", (1, '张三'),
#              'wangnan', 'postgres', 'devops')
#     write_db("""update test set name = %s where id = %s""", ('张三1', 1),
#              'wangnan', 'postgres', 'devops')
#     select_all("""select * from test""", (),
#                'wangnan', 'postgres', 'devops')
