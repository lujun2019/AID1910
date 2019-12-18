# with 测试
# 啦啦啦
import pymysql

db = pymysql.connect(host="localhost",
                     port=3306,
                     user="root",
                     password="123456",
                     database="stu",
                     charset="utf8")
cur = db.cursor()
try:
    # sql = "insert into class_1 values (9,'losad',18,'w','81')"
    # cur.execute(sql)
    # sql = "insert into class_1 values (%s,%s,%s,%s,%s)"
    # cur.execute(sql, [11, "hala", 22, "w", 97])
    # sql = "update class_1 set score = 84 where id = 3"
    # cur.execute(sql)
    # sql = "delete from class_1 where id = 11"
    # cur.execute(sql)
    list_ = [(19, 8), (16, 9), (14, 10)]
    sql = "update class_1 set score = score -5,age = %s where id=%s"
    # for i in list_:
    #     cur.execute(sql,i)
    cur.executemany(sql, list_)
    db.commit()
except Exception as e:
    print(e)
    db.rollback()
cur.close()
db.close()
