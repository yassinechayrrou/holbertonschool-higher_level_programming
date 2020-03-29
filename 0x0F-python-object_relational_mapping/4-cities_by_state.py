#!/usr/bin/python3
"""lists all cities from database"""
if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    db = MySQLdb.connect(host="localhost",
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cursor = db.cursor()
    cursor.execute("""SELECT cities.id, cities.name, states.name
                      From states
                      INNER JOIN cities ON states.id = cities.state_id
                      ORDER BY cities.id""")
    states = cursor.fetchall()
    for i in states:
        print(i)
    db.close()
