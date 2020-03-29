#!/usr/bin/python3
"""script that takes an argument and displays all values maching with name"""
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
                      WHERE name='{}'
                      ORDER BY id ASC""".format(argv[4]))
    states = cursor.fetchall()
    for i in states:
        if i[1] == argv[4]:
                print(i)
    db.close()
