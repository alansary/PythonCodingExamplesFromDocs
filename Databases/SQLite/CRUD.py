#!/usr/bin/env python3

import sqlite3

'''
CRUD
    Create - Read - Update - Delete
'''


def main():
    db = sqlite3.connect('CRUD.db')
    db.row_factory = sqlite3.Row

    print('=' * len('Create table data'))
    print('Create table data')
    print('=' * len('Create table data'))
    db.execute('DROP TABLE IF EXISTS data')
    db.execute('CREATE TABLE data(id INTEGER PRIMARY KEY, fName TEXT, lName TEXT, phoneNum INTEGER)')

    display(db)

    # Create
    print("=" * len('Create rows'))
    print('Create rows')
    print("=" * len('Create rows'))
    db.execute("""INSERT INTO data VALUES(1, 'Mohamed', 'Alansary', 120)""")
    db.execute('INSERT INTO data (id, fName, lName, phoneNum) VALUES (?, ?, ?, ?)', (2, 'Mahmoud', 'Taha', 121))
    db.commit()
    insert(db, dict(id = 3, fName = "Mohamed", lName = "Salah", phoneNum = 122))
    insert(db, dict(id = 4, fName = "Ahmed", lName = "Geda", phoneNum = 123))
    insert(db, dict(fName = "Omar", lName = "Kamaron", phoneNum = 124))

    # Read
    print("=" * len('Display rows'))
    print('Display rows')
    print("=" * len('Display rows'))
    display(db)

    # Retrieve
    print("=" * len('Retrieve rows'))
    print('Retrieve rows')
    print("=" * len('Retrieve rows'))
    retrieve(db, ('id', 1))
    retrieve(db, ('id', 5))
    retrieve(db, ('fName', 'Mohamed'))
    retrieve(db, ('lName', 'Taha'))
    retrieve(db, ('phoneNum', 123))
    retrieve(db, ('id', 6))

    # Update
    print('=' * len('Upadte columns'))
    print('Update columns')
    print('=' * len('Update columns'))
    update(db, ('fName', 'Hussein'), ('phoneNum', 124))
    update(db, ('fName', 'x', 'y'), ('phoneNum', 124))
    update(db, ('fName', 'Hussein'), ('phoneNum', 'x', 'y'))
    update(db, ('x', 'Hussien'), ('phoneNum', 124))
    update(db, ('fName', 'Hussien'), ('x', 124))
    print("=" * len('Display rows after updating data'))
    print('Display rows after updating data')
    print("=" * len('Display rows after updating data'))
    display(db)

    # Update row
    print('=' * len('Update row'))
    print('Update row')
    print('=' * len('Update row'))
    update_row(db, 2, dict(fName = 'Ali', lName = 'Hashem'))
    update_row(db, 6, dict(fName = 'New', lName = 'User', phoneNum = 123))
    print("=" * len('Display rows after updating data'))
    print('Display rows after updating data')
    print("=" * len('Display rows after updating data'))
    display(db)

    # Delete
    print('=' * len('Delete'))
    print('Delete')
    print('=' * len('Delete'))
    delete(db, 2)
    delete(db, 7)
    delete(db, 0)
    print("=" * len('Display rows after deleting data'))
    print('Display rows after deleting data')
    print("=" * len('Display rows after deleting data'))
    display(db)

    db.close()


# Create
def insert(db, d):
    if 'id' in d:
        db.execute('INSERT INTO data VALUES (?, ?, ?, ?)', (d['id'], d['fName'], d['lName'], d['phoneNum']))
    else:
        db.execute('INSERT INTO data (fName, lName, phoneNum) VALUES (?, ?, ?)', (d['fName'], d['lName'], d['phoneNum']))
    db.commit()


# Read
def display(db):
    cursor = db.execute('SELECT * FROM data order by id')
    test_cursor = db.execute('SELECT * FROM data order by id')

    for row in cursor:
        print('ID: {}\nFirst Name: {}\nLast Name: {}\nPhone Number: {}'.format(
            dict(row)['id'],
            dict(row)['fName'],
            dict(row)['lName'],
            dict(row)['phoneNum']
        ))
        print('=' * 50)

    if len(list(test_cursor)) == 0:
        print("No records in the database")
        print("=" * 50)


# Retrieve
def retrieve(db, cond):
    if len(cond) == 2:
        if cond[0] == 'id':
            col = 'id'
            val = cond[1]
        elif cond[0] == 'fName':
            col = 'fName'
            val = cond[1]
        elif cond[0] == 'lName':
            col = 'lName'
            val = cond[1]
        elif cond[0] == 'phoneNum':
            col = 'phoneNum'
            val = cond[1]
        else:
            col = None
            val = None
            print("Please, enter valid column name")
            return
    else:
        print("Please, enter valid (column, value) pair")
        return

    if col and val:
        cursor = db.execute('SELECT * FROM data WHERE {} = ?'.format(col), (val,))
        test_cursor = db.execute('SELECT * FROM data WHERE {} = ?'.format(col), (val,))

    for row in cursor:
        print('ID: {}\nFirst Name: {}\nLast Name: {}\nPhone Number: {}'.format(
            dict(row)['id'],
            dict(row)['fName'],
            dict(row)['lName'],
            dict(row)['phoneNum']
        ))
        print('=' * 50)

    if len(list(test_cursor)) == 0:
        print('No match found')
        print('=' * 50)


# Update
def update(db, upd, cond):
    if len(upd) == 2:
        if upd[0] == 'id':
            col = 'id'
            val = upd[1]
        elif upd[0] == 'fName':
            col = 'fName'
            val = upd[1]
        elif upd[0] == 'lName':
            col = 'lName'
            val = upd[1]
        elif upd[0] == 'phoneNum':
            col = 'phoneNum'
            val = upd[1]
        else:
            col, val = None, None
            print("Please, enter valid column name")
            return
    else:
        print("Please, enter valid (column, value) pair")
        return

    if col and val:
        if len(cond) == 2:
            if cond[0] == 'id':
                col2 = 'id'
                val2 = cond[1]
            elif cond[0] == 'fName':
                col2 = 'fName'
                val2 = cond[1]
            elif cond[0] == 'lName':
                col2 = 'lName'
                val2 = cond[1]
            elif cond[0] == 'phoneNum':
                col2 = 'phoneNum'
                val2 = cond[1]
            else:
                col2, val2 = None, None
                print("Please, enter valid column name")
                return
        else:
            print("Please, enter valid (column, value) pair")
            return

        if col2 and val2:
            db.execute('UPDATE data SET {} = ? WHERE {} = ?'.format(col, col2), (val, val2))
            db.commit()


# Update row
def update_row(db, rowid, d):
    test_cursor = db.execute('SELECT * FROM data WHERE id = ?', (rowid,))
    length = len(list(test_cursor))
    if length == 0:
        print('No such id in the database')
        return
    else:
        db.execute('UPDATE data SET fName = ?, lName = ?, phoneNum = ? WHERE id = ?', (
            d.get('fName', None),
            d.get('lName', None),
            d.get('phoneNum', None),
            rowid
        ))
        db.commit()


# Delete
def delete(db, rowid):
    test_cursor = db.execute('SELECT * FROM data WHERE id = ?', (rowid,))
    length = len(list(test_cursor))
    if length == 0:
        print('No such id in the database')
        return
    else:
        db.execute('DELETE FROM data WHERE id = ?', (rowid,))
        db.commit()

if __name__ == "__main__": main()