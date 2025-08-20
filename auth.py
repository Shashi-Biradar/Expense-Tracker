# Users - Registration, Login
import mysql.connector
import bcrypt

DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Shashi@123',
    'database': 'expenses_db'
}

def get_connection():
    return mysql.connector.connect(host = DB_CONFIG['host'], user = DB_CONFIG['user'], password = DB_CONFIG['password'], database = DB_CONFIG['database'])


def init_user_table():
    connection = get_connection()
    cur = connection.cursor()
    cur.execute("SHOW TABLES LIKE 'users'")
    result = cur.fetchone()
    if result == None:        
        cur.execute("""
            CREATE TABLE users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100),
                email VARCHAR(100),
                username VARCHAR(100) UNIQUE NOT NULL,
                password VARCHAR(100) NOT NULL
            )
        """)
        connection.commit()
        connection.close()
        print('Created users table successfully')
    else:
        print('Users table already exist')

def hash_password(password):
    password_bytes = password.encode('utf-8')
    # Generate a salt
    salt = bcrypt.gensalt()
    # Hash the password
    hashed_password = bcrypt.hashpw(password_bytes, salt)
    return hashed_password

def register(name, email, username, password):
    connection = get_connection()
    cur = connection.cursor()
    try:
        hashed_password = hash_password(password)
        cur.execute("INSERT INTO users (name, email, username, password) VALUES (%s, %s, %s, %s)", (name, email, username, hashed_password))
        connection.commit()
        print('Registered the user successfully')
    except:
        print('Username already exist')
    finally:
        connection.close()

def login(username, password):
    print(username, password)
    connection = get_connection()
    cur = connection.cursor()
    try:
        cur.execute("SELECT id, name, password FROM users WHERE username = %s", (username,))
        result = cur.fetchone()
        entered_password_bytes = password.encode('utf-8')
        stored_password = result[2].encode('utf-8')
        if bcrypt.checkpw(entered_password_bytes, stored_password):
            return result[0]
    except Exception as e:
        print('Username doesnot exist', e)
    finally:
        connection.close()

# init_user_table()

# register('abhi', 'abhi@digitaledify.ai', 'abhi01', 'abhi!23')
# register('mahi', 'mahi@digitaledify.ai', 'mahi01', 'mahi!23')
# register('shivu', 'shivu@digitaledify.ai', 'shivu01', 'shivu!23')
# register('sharanu', 'sharanu@digitaledify.ai', 'sharanu01', 'sharanu!23')

# login('Satish26', 'satish@123')