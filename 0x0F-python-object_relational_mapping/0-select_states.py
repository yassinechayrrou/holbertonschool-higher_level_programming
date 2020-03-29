#!/usr/bin/python3
""" lists all states from database and print them ordered """
""" didn't use port = 3306 since it is default in MySQL._mysql """
if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    db = MySQLdb.connect(host="localhost",
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cursor = db.cursor()
    cursor.execute("""SELECT id, name From states ORDER BY id ASC""")
    states = cursor.fetchall()
    for i in states:
        print(i)
    db.close()
