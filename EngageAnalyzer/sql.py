import mysql.connector
connection = mysql.connector.connect(
    host='127.0.0.1',
    user='sungmkim',
    password='Password1234!',
    database='sandora'
)

def get_nickname(memberId):
    owner_query = f"SELECT name FROM space where member_id = {memberId}"
    cursor.execute(owner_query)
    nickname = cursor.fetchall()[0]
    return nickname
    
try:
    cursor = connection.cursor()
    count = 100
    owner_ids = [12077, 2]
    with open("theusdata.txt", "w", encoding='utf8') as file: 
        for owner_id in owner_ids:
            query = f"SELECT id, owner_id, writer_id, title, content FROM board where owner_id = {owner_id} ORDER BY id DESC LIMIT {count}"    
            cursor.execute(query)
            rows = cursor.fetchall()
            for row in rows:
                id = row[0]
                owner_nickname = get_nickname(row[1])
                writer_nickname = get_nickname(row[2])
                new_content = row[4].replace('\n', ' ')
                file.write(f"{id}|{owner_nickname[0]}|{writer_nickname[0]}|{row[3]}|{new_content}|")
                file.write("\n")

finally:
    # 커서와 연결 종료
    cursor.close()
    connection.close()