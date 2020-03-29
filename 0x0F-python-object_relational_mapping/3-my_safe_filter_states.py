#!/usr/bin/python3
"""script that escapes sql injection from task 2"""
if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    db = MySQLdb.connect(host="localhost",
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    injection_check = MySQLdb.escape_string(argv[4]).decode()
    cursor = db.cursor()
    cursor.execute("""SELECT id, name
                      From states
                      WHERE name REGEXP BINARY '{}'
                      ORDER BY id ASC""".format(injection_check))
    states = cursor.fetchall()
    for i in states:
        print(i)
    db.close()
