import pymysql

class Database:
    def __init__(self):
        self.connection = pymysql.connect(host='localhost',
                                          user='root',
                                          password='123456',
                                          db='admins')
        self.cursor = self.connection.cursor()

    def get_all(self):
        sql = "SELECT * FROM `users`"
        self.cursor.execute(sql)