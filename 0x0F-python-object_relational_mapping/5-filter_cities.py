#!/usr/bin/python3
"""lists all cities in state"""
if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    db = MySQLdb.connect(host="localhost",
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cursor = db.cursor()
    command = """SELECT cities.name From states
                 INNER JOIN cities ON states.id = cities.state_id
                 WHERE states.name=%(injection)s
                 ORDER BY cities.id ASC"""
    cursor.execute(command, {'injection': argv[4]})
    cities = cursor.fetchall()
    print(", ".join([i[0] for i in cities]))
    db.close()
