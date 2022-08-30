from utils.LogUtil import my_log
import pymysql


# 1.创建封装类
class Mysql:
    # 2.初始化数据，连接数据库，光标对象
    def __init__(self, host, user, password, database, charset="utf8", port=3306):
        self.log = my_log()
        self.conn = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            charset=charset,
            port=port
        )
        self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    # 3.创建查询，执行方法
    def fetchone(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchone()

    def fetchall(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def exec(self, sql):
        try:
            if self.conn and self.cursor:
                self.cursor.execute(sql)
                self.conn.commit()
        except Exception as ex:
            self.conn.rollback()
            self.log.error("Mysql 执行失败")
            self.log.error(ex)
            return False
        return True

    # 4.关闭对象

    def __del__(self):
        # 关闭光标对象
        if self.cursor is not None:
            self.cursor.close()
        # 关闭连接对象
        if self.conn is not None:
            self.cursor.close()


if __name__ == '__main__':
    mysql = Mysql("127.0.0.1", "root", "199751", "students", charset="utf8", port=3306)

    # r = mysql.fetchall("select name,gender from student")查询多个数据
    r = mysql.exec("update student set address = '苑寨市' where id=3 ")
    print(r)
# # 1.导入pymysql
# import pymysql
#
# # 2.连接database
# conn = pymysql.connect(
#     host="127.0.0.1",
#     user="root",
#     password="199751",
#     database="students",
#     charset="utf8",
#     port=3306
# )
# # 3.获取执行sql的光标对象
# cursor = conn.cursor()
# # 4.执行sql
# sql = "select name,gender from student"
# cursor.execute(sql)  # 执行sql语句
# r = cursor.fetchone()  # fetchone获取一条数据，fetchall获取符合sql查询语句的所有数据
# print(r)
# # 5.关闭对象
# cursor.close()
# conn.close()
