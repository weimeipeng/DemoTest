import pymysql
import random

if __name__ == '__main__':
    print("访问mysql 数据库")
    host ="localhost"

    conn = pymysql.connect(
    port =3306,
    user = "root",
    password ="root",
    db = "test",
    charset ="utf8"
    )

    try:
        cursor = conn.cursor()

        sql ="select * from category"

        cursor.execute(sql)
        all_data = cursor.fetchall()

        for data in all_data:
            print("id:%d name: %s" %(data[0],data[1]) )

    finally:
        conn.close()