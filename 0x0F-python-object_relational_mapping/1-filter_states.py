#!/usr/bin/python3
""" script that lists all states filtered according to name starting with N"""
if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    db = MySQLdb.connect(host="localhost",
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cursor = db.cursor()
    cursor.execute("""SELECT id, name
                      From states
                      WHERE name LIKE 'N%'
                      ORDER BY id ASC""")
    states = cursor.fetchall()
    for i in states:
        print(i)
    db.close()
