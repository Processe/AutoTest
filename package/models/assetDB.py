# coding=utf-8
# --author='fangfang'

import pymysql
import readConfig
from models.logger import Logger

logger = Logger(logger="assetDataBase").getlog()


class AssetDB:
    def __init__(self):
        rc = readConfig.ReadConfig()
        self.host = rc.get_value("assetSqlInfo", "host")
        self.username = rc.get_value("assetSqlInfo", "user")
        self.password = rc.get_value("assetSqlInfo", "passwd")
        self.port = int(rc.get_value("assetSqlInfo", "port"))
        self.database = rc.get_value("assetSqlInfo", "db")
        self.db = None
        self.cursor = None

    def connectDB(self):
        """
        connect to database
        :return:
        """
        try:
            # connect to DB
            self.db = pymysql.connect(host=self.host, port=self.port, user=self.username, passwd=self.password, db=self.database, charset='utf8')
            # create cursor
            self.cursor = self.db.cursor()
            print("Connect DB successfully!")
        except ConnectionError as ex:
            logger(str(ex))

    def executeSQL(self, sql):
        """
        execute sql
        :param sql:
        :return:
        """
        self.connectDB()
        # executing sql
        self.cursor.execute(sql)
        # executing by committing to DB
        self.db.commit()
        return self.cursor

    def closeDB(self):
        """
        close database
        :return:
        """
        self.db.close()
        print("Database closed!")

    def get_all(self, sql):
        """
        get all result after execute sql
        :param cursor:
        :return:
        """
        cursor = self.executeSQL(sql)
        value = cursor.fetchall()
        self.closeDB()
        return value

    def get_one(self, sql):
        """
        get one result after execute sql
        :param cursor:
        :return:
        """
        cursor = self.executeSQL(sql)
        value = cursor.fetchone()
        self.closeDB()
        return value

