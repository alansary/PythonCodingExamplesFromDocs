#!/usr/bin/python3

from sqlite3 import dbapi2


def main():
    # <sqlite3.Connection object at 0x7ff8f7266490> <class 'sqlite3.Connection'> - Open db instance
    # SQLiteDB: empty
    connection = dbapi2.connect("SQLiteDB")

    # <sqlite3.Cursor object at 0x7f5e273c43b0> <class 'sqlite3.Cursor'> - create cursor for DB navigation
    # SQLiteDB: empty
    cursor = connection.cursor()

    '''
    # Executing SQL DDL Command
    # SQLiteDB: SQLite 3.x database
    cursor.execute("""CREATE TABLE data (id INTEGER PRIMARY KEY, fName TEXT, lName TEXT, phoneNum INTEGER);""")
    '''

    '''
    # DDL commands are committed immediately; however, DML commands are not
    # commit - commit changes to DB (Disk)
    cursor.execute("""INSERT INTO data VALUES (1, 'Mohamed', 'Alansary', 01207395400);""")
    connection.commit()
    '''

    # Close the connection (DB) and releases any resources associated with the connection
    cursor.close()

    '''
    help(dbapi2)
        connect(...)
        connect(database[, timeout, detect_types, isolation_level,
                check_same_thread, factory, cached_statements, uri])

        Opens a connection to the SQLite database file *database*. You can use
        ":memory:" to open a database connection to a database that resides in
        RAM instead of on disk.

    class Connection(builtins.object)
     |  SQLite database connection object.
     |
     |  Methods defined here:
     |
     |  cursor(...)
     |      Return a cursor for the connection.
     |  commit(...)
     |      Commit the current transaction.
     |  close(...)
     |      Closes the connection.
    class Cursor(builtins.object)
     |  SQLite database cursor class.
     |
     |  Methods defined here:
     |
     |  execute(...)
     |      Executes a SQL statement.
     |  close(...)
     |      Closes the cursor.
    '''
if __name__ == "__main__": main()