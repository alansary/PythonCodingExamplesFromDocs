#!/usr/bin/env python3

import sqlite3


def main():
    db = sqlite3.connect('test.db')
    db.row_factory = sqlite3.Row
    # Allows you to specify how rows will be returned from the cursor (row object can be converted to any type)
    db.execute('drop table if exists test')
    db.execute('create table test(t1 text, i1 int)')
    db.execute('insert into test (t1, i1) values (?, ?)', ('one', 1))
    db.execute('insert into test (t1, i1) values (?, ?)', ('two', 2))
    db.execute('insert into test (t1, i1) values (?, ?)', ('three', 3))
    db.execute('insert into test (t1, i1) values (?, ?)', ('four', 4))
    db.commit()
    cursor = db.execute('select i1, t1 from test order by i1')

    for row in cursor:
        print(dict(row))
        print(dict(row)['i1'], dict(row)['t1'])
        print(row)
        print(list(row))
        print(tuple(row))
        print(row['i1'], row['t1'])
        print('=' * 40)

if __name__ == "__main__": main()