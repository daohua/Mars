# -*- coding: utf-8 -*-
#!/usr/bin/env python2

import pymysql.cursors

class BaseFactory(object):

    def __init__(self, dbname, username, passwd):
        self.connection = pymysql.connect(
            host='localhost',
            user=username,passwd=passwd, 
            db=dbname,charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor)

    def create(self):
        pass

    def insert(self):
        with self.connection.cursor() as cursor:
            # Create a new record
            sql = """INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"""
            cursor.execute(sql, ('webmaster@python.org', 'very-secret'))

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        self.connection.commit()

    def select(self):
        pass

    def __del__(self):
        if self.connection:
            self.connection.close()


class CalendarFactory(BaseFactory):

    def __init__(self):
        super(CalendarFactory, self).__init__("socialcalendar","nous","buyitnow")

    def bulk_create(self):
        pass


if __name__ == '__main__':
    cf = CalendarFactory()
    cf.create()

