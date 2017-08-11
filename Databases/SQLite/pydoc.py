#!/usr/bin/env python3


def main():
    pass
'''
### Python Integration ###
Requires: 'python-pysqlite2' package - SQLite3 interface
  a. Install Prerequisites
    'dpkg -l | grep pysqlite2'
    'sudo aptitude search pysqlite2'
    'sudo aptitude install python-pysqlite2'
    'which python'
   b. Use interactive interface to talk to SQLite
   c. 'import sqlite3' 'help(sqlite3)'
      'from sqlite3 import dbapi2

help(sqlite3)

PACKAGE CONTENTS
    dbapi2
    dump

    class Connection(builtins.object)
     |  SQLite database connection object.
     |
     |  Methods defined here:
     |
     |  __call__(self, /, *args, **kwargs)
     |      Call self as a function.
     |
     |  __enter__(...)
     |      For context manager. Non-standard.
     |
     |  __exit__(...)
     |      For context manager. Non-standard.
     |
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |
     |  close(...)
     |      Closes the connection.
     |
     |  commit(...)
     |      Commit the current transaction.
     |
     |  create_aggregate(...)
     |      Creates a new aggregate. Non-standard.
     |
     |  create_collation(...)
     |      Creates a collation function. Non-standard.
     |
     |  create_function(...)
     |      Creates a new function. Non-standard.
     |
     |  cursor(...)
     |      Return a cursor for the connection.
     |
     |  execute(...)
     |      Executes a SQL statement. Non-standard.
     |
     |  executemany(...)
     |      Repeatedly executes a SQL statement. Non-standard.
     |
     |  executescript(...)
     |      Executes a multiple SQL statements at once. Non-standard.
     |
     |  interrupt(...)
     |      Abort any pending database operation. Non-standard.
     |
     |  iterdump(...)
     |      Returns iterator to the dump of the database in an SQL text format. Non-standard.
     |
     |  rollback(...)
     |      Roll back the current transaction.
     |
     |  set_authorizer(...)
     |      Sets authorizer callback. Non-standard.
     |
     |  set_progress_handler(...)
     |      Sets progress handler callback. Non-standard.
     |
     |  set_trace_callback(...)
     |      Sets a trace callback called for each SQL statement (passed as unicode). Non-standard.
     |
     |
     |  ----------------------------------------------------------------------
    class Cursor(builtins.object)
     |  SQLite database cursor class.
     |
     |  Methods defined here:
     |
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  __iter__(self, /)
     |      Implement iter(self).
     |
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |
     |  __next__(self, /)
     |      Implement next(self).
     |
     |  close(...)
     |      Closes the cursor.
     |
     |  execute(...)
     |      Executes a SQL statement.
     |
     |  executemany(...)
     |      Repeatedly executes a SQL statement.
     |
     |  executescript(...)
     |      Executes a multiple SQL statements at once. Non-standard.
     |
     |  fetchall(...)
     |      Fetches all rows from the resultset.
     |
     |  fetchmany(...)
     |      Fetches several rows from the resultset.
     |
     |  fetchone(...)
     |      Fetches one row from the resultset.
     |
     |  setinputsizes(...)
     |      Required by DB-API. Does nothing in pysqlite.
     |
     |  setoutputsize(...)
     |      Required by DB-API. Does nothing in pysqlite.
     |
     |  ----------------------------------------------------------------------


   d. 'from sqlite3 import dbapi2'
      'help(dbapi2)'

help(dbapi2)

FUNCTIONS
    DateFromTicks(ticks)

    TimeFromTicks(ticks)

    TimestampFromTicks(ticks)

    adapt(...)
        adapt(obj, protocol, alternate) -> adapt obj to given protocol. Non-standard.

    complete_statement(...)
        complete_statement(sql)

        Checks if a string contains a complete SQL statement. Non-standard.

    connect(...)
        connect(database[, timeout, detect_types, isolation_level,
                check_same_thread, factory, cached_statements, uri])

        Opens a connection to the SQLite database file *database*. You can use
        ":memory:" to open a database connection to a database that resides in
        RAM instead of on disk.

    enable_callback_tracebacks(...)
        enable_callback_tracebacks(flag)

        Enable or disable callback functions throwing errors to stderr.

    enable_shared_cache(...)
        enable_shared_cache(do_enable)

        Enable or disable shared cache mode for the calling thread.
        Experimental/Non-standard.

    register_adapter(...)
        register_adapter(type, callable)

        Registers an adapter with pysqlite's adapter registry. Non-standard.

    register_converter(...)
        register_converter(typename, callable)

        Registers a converter with pysqlite. Non-standard.

DATA
    PARSE_COLNAMES = 2
    PARSE_DECLTYPES = 1
    SQLITE_ALTER_TABLE = 26
    SQLITE_ANALYZE = 28
    SQLITE_ATTACH = 24
    SQLITE_CREATE_INDEX = 1
    SQLITE_CREATE_TABLE = 2
    SQLITE_CREATE_TEMP_INDEX = 3
    SQLITE_CREATE_TEMP_TABLE = 4
    SQLITE_CREATE_TEMP_TRIGGER = 5
    SQLITE_CREATE_TEMP_VIEW = 6
    SQLITE_CREATE_TRIGGER = 7
    SQLITE_CREATE_VIEW = 8
    SQLITE_DELETE = 9
    SQLITE_DENY = 1
    SQLITE_DETACH = 25
    SQLITE_DROP_INDEX = 10
    SQLITE_DROP_TABLE = 11
    SQLITE_DROP_TEMP_INDEX = 12
    SQLITE_DROP_TEMP_TABLE = 13
    SQLITE_DROP_TEMP_TRIGGER = 14
    SQLITE_DROP_TEMP_VIEW = 15
    SQLITE_DROP_TRIGGER = 16
    SQLITE_DROP_VIEW = 17
    SQLITE_IGNORE = 2
    SQLITE_INSERT = 18
    SQLITE_OK = 0
    SQLITE_PRAGMA = 19
    SQLITE_READ = 20
    SQLITE_REINDEX = 27
    SQLITE_SELECT = 21
    SQLITE_TRANSACTION = 22
    SQLITE_UPDATE = 23
    adapters = {(<class 'datetime.datetime'>, <class 'sqlite3.PrepareProto...
    apilevel = '2.0'
    converters = {'DATE': <function register_adapters_and_converters.<loca...
    paramstyle = 'qmark'
    sqlite_version = '3.13.0'
    sqlite_version_info = (3, 13, 0)
    threadsafety = 1
    version_info = (2, 6, 0)


    'connection1.commit()' - commit changes to DB (Disk)
Note: DDL commands are commited immediately; however, inserts, updates and deletes don't
    'c.close()' - Closes the connection (DB) and releases any resources associated with the connection
    'quit()' - quits python
'''
if __name__ == "__main__": main()