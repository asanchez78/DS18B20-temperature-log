#!/usr/bin/python3
#import MySQLdb
import cymysql as MySQLdb
class Database:

    host = ''
    user = ''
    password = ''
    db = ''

    def __init__(self):
        self.connection = MySQLdb.connect(self.host, self.user, self.password, self.db)
        self.cursor = self.connection.cursor()

    def insert(self, query):
        try:
            self.cursor.execute(query)
            self.connection.commit()
        except:
            self.connection.rollback()



    def query(self, query):
        cursor = self.connection.cursor( MySQLdb.cursors.DictCursor )
        cursor.execute(query)

        return cursor.fetchall()

    def __del__(self):
        self.connection.close()


if __name__ == "__main__":

    db = Database()

    #CleanUp Operation
    del_query = "DELETE FROM office"
    db.insert(del_query)

    # Data Insert into the table
    query = """
        INSERT INTO office
        (`temperature`)
        VALUES
        (71)
        """

    # db.query(query)
    db.insert(query)

    # Data retrieved from the table
    select_query = """
        SELECT * FROM office
        WHERE temperature = 71
        """

    people = db.query(select_query)

    for person in people:
        #print("Found %s " % person['temperature'])
        print(str(person['temperature']) + ' ' + str(person['timestamp']))
