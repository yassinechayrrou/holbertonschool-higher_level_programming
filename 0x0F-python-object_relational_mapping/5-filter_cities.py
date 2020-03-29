#!/usr/bin/python3
"""lists all cities in state"""
if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    db = MySQLdb.connect(host="localhost",
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    injection_check = MySQLdb.escape_string(argv[4]).decode()
    cursor = db.cursor()
    cursor.execute("""SELECT cities.name
                      From states
                      INNER JOIN cities ON states.id = cities.state_id
                      WHERE states.name='{}'
                      ORDER BY cities.id""".format(injection_check))
    cities = cursor.fetchall()
    for i in cities:
        if i[0] is cities[len(cities) - 1][0]:
            print(i[0])
        else:
            print("{}, ".format(i[0]), end="")
    cursor.close()
    db.close()
