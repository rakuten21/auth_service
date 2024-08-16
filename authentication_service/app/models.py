from app.database import mysql

def create_user(username, password_hash):
    cursor = mysql.connection.cursor()
    cursor.execute('INSERT INTO users (username, password_hash) VALUE (%s, %s)', (username, password_hash))
    mysql.connection.commit()
    cursor.close()

def get_user_by_username(username):
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM users WHERE username = %s', (username,))
    user = cursor.fetchone()
    cursor.close()
    return user