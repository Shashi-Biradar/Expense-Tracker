import mysql.connector

DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Shashi@123',
    'database': 'expenses_db'
}

def get_connection():
    return mysql.connector.connect(host = DB_CONFIG['host'], user = DB_CONFIG['user'], password = DB_CONFIG['password'], database = DB_CONFIG['database'])

def init_expense_table():
    connection = get_connection()
    cur = connection.cursor()
    cur.execute("SHOW TABLES LIKE 'expenses'")
    result = cur.fetchone()
    if result == None:        
        cur.execute("""
            CREATE TABLE expenses (
                id INT AUTO_INCREMENT PRIMARY KEY,
                user_id INT,
                amount FLOAT NOT NULL,
                category VARCHAR(100) NOT NULL,
                description VARCHAR(100) NOT NULL,
                date DATE NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users(id)   
            )
        """)
        connection.commit()
        connection.close()
        print('Created expenses table successfully')
    else:
        print('Expenses table already exist')


def insert_expense(user_id, amount, category, description, date):
    connection = get_connection()
    cur = connection.cursor()
    try:
        cur.execute("INSERT INTO expenses (user_id, amount, category, description, date) VALUES (%s, %s, %s, %s, %s)", (user_id, amount, category, description, date))
        connection.commit()
        print('Inserted the expense successfully')
    except Exception as e:
        print('Error while inserting expense', e)
    finally:
        connection.close()

def view_all_expenses(user_id):
    connection = get_connection()
    cur = connection.cursor()
    try:
        cur.execute("SELECT * FROM expenses WHERE user_id = %s ORDER BY date DESC", (user_id, ))
        expenses = cur.fetchall()
        return expenses
    except Exception as e:
        print('Error while retrieving expenses', e)
    finally:
        connection.close()

def search_by_category(user_id, category):
    connection = get_connection()
    cur = connection.cursor()
    try:
        cur.execute("SELECT * FROM expenses WHERE user_id = %s AND category = %s ORDER BY date DESC", (user_id, category, ))
        expenses = cur.fetchall()
        return expenses
    except Exception as e:
        print('Error while retrieving expenses', e)
    finally:
        connection.close()

def delete_expense(id):
    connection = get_connection()
    cur = connection.cursor()
    try:
        cur.execute("DELETE FROM expenses WHERE id = %s ", (id,))
        connection.commit()
        return cur.rowcount
    except Exception as e:
        print('Error while retrieving expenses', e)
    
    finally:
        connection.close()

def updated_expense(id):
    connection = get_connection()
    cur = connection.cursor()
    try:
        cur.execute(
            "UPDATE expenses SET amount = %s, description = %s WHERE id = %s",
            (50, 'one rool note book', id)
        )
        connection.commit()
        return cur.rowcount  # returns number of rows updated
    except Exception as e:
        print('Error while updating expense:', e)
        
    finally:
        connection.close()      
