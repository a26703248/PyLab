import pymysql.cursors
# 連線配置資訊
config = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': 'a0909007892',
    'db': 'java',
    'charset': 'utf8',
}
# 建立連線
connection = pymysql.connect(**config)

# 建立遊標方法1
cursor = connection.cursor()

# 建立遊標方法2 取別名為 cursor
with connection.cursor() as cursor:
    # 執行sql語句，插入記錄
    sql = 'select * from empolyee'
    cursor.execute(sql)  # 插入一條資料
    data = cursor.fetchall()
    # data為多條資料，放在一個元組或者列表中
    print(data)
# 沒有設定預設自動提交，需要主動提交，以儲存所執行的語句
connection.commit()  # 連線提交事務
cursor.close()  # 關閉遊標連線
connection.close();  # 關閉連線，釋放記憶體