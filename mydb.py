import mysql.connector

dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    password='123456'  # 更正参数名为 'password'
)

cursorObject = dataBase.cursor()

cursorObject.execute('CREATE DATABASE elderco')

print('all done')
