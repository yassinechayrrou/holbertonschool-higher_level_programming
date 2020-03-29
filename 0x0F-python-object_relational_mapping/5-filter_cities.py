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
                 WHERE states.name = %s"""
    cursor.execute(command, (argv[4], ))
    cities = cursor.fetchall()
    for i in range(len(cities) - 1):
       print("{:s}, ".format(cities[i][0]), end="")
    print(cities[len(cities) - 1][0])
    cursor.close()
    db.close()
