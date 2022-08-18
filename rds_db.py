import pymysql
conn = pymysql.connect(
        host= '',
        port = 3306,
        user = '',
        password = '',
        db = ''
        )
def insert_details(name,email,comment,gender):
    cur=conn.cursor()
    cur.execute("INSERT INTO Details (name,email,comment,gender) VALUES (%s,%s,%s,%s)", (name,email,comment,gender))
    conn.commit()

def get_details():
    cur=conn.cursor()
    cur.execute("SELECT *  FROM Details")
    details = cur.fetchall()
    return details
