import sqlite3

def create_connection(db_file):
    connection = None
    try:
        connection = sqlite3.connect(db_file)
    except sqlite3.Error as error:
        print(error)
    return connection

def create_table(connection, sql):
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
    except sqlite3.Error as error:
        print(error)


def add_product(connection, product):
    try:
        sql = '''
        INSERT INTO products(
        product_title, price, quantity)
        VALUES(?, ?, ?)'''
        cursor = connection.cursor()
        cursor.execute(sql, product)
        connection.commit()
    except sqlite3.Error as error:
        print(error)


def set_product_quantity(connection, product):
    try:
        sql = '''
       UPDATE products SET quantity = ? WHERE id = ?'''
        cursor = connection.cursor()
        cursor.execute(sql, product)
        connection.commit()
    except sqlite3.Error as error:
        print(error)

def set_product_price(connection, product):
    try:
        sql = '''
       UPDATE products SET price = ? WHERE id = ?'''
        cursor = connection.cursor()
        cursor.execute(sql, product)
        connection.commit()
    except sqlite3.Error as error:
        print(error)


def delete_product_by_id(connection, id):
    try:
        sql = '''
       DELETE FROM products WHERE id = ?'''
        cursor = connection.cursor()
        cursor.execute(sql, (id ,))
        connection.commit()
    except sqlite3.Error as error:
        print(error)


def select_products(connection):
    try:
        sql = '''
       SELECT * FROM products'''
        cursor = connection.cursor()
        cursor.execute(sql,)
        all_products = cursor.fetchall()
        for i in all_products:
            print(i)
    except sqlite3.Error as error:
        print(error)



def select_products_by_price_and_quantity(connection, limit):
    try:
        sql = '''
       SELECT * FROM products
       WHERE price <= ? AND quantity >= ?'''
        cursor = connection.cursor()
        cursor.execute(sql,limit)
        all_products = cursor.fetchall()
        for i in all_products:
            print(i)
    except sqlite3.Error as error:
        print(error)


def find_products(connection):
    try:
        sql = '''
       SELECT * FROM products
       WHERE product_title LIKE "%Shirt%"'''
        cursor = connection.cursor()
        cursor.execute(sql,)
        all_products = cursor.fetchall()
        for i in all_products:
            print(i)
    except sqlite3.Error as error:
        print(error)


sql_to_create_employees_table='''
CREATE TABLE products 
    (id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_title  VARCHAR(200) NOT NULL,
   price FLOAT(10,2) NOT NULL DEFAULT 0.0,
    quantity INTEGER NOT NULL DEFAULT 0
     )'''


if __name__ == '__main__':

    db_name = 'hw.db'
    my_connection = create_connection(db_name)
    if my_connection:
        print('Connected to database')
        create_table(my_connection, sql_to_create_employees_table)
        add_product(my_connection, ('Shirt', 1200, 4))
        add_product(my_connection, ('Short', 800, 6))
        add_product(my_connection, ('Throusers', 2500, 3))
        add_product(my_connection, ('Skirt', 1700, 7))
        add_product(my_connection, ('Socks', 500, 5))
        add_product(my_connection, ('T-shirt', 1100, 8))
        add_product(my_connection, ('Boots', 6000, 3))
        add_product(my_connection, ('Coat',3450, 2))
        add_product(my_connection, ('Watches', 10000, 1))
        add_product(my_connection, ('Jeans', 2500, 5))
        add_product(my_connection, ('Sneakers', 4600, 4))
        add_product(my_connection, ('Hoodie', 1800, 6))
        add_product(my_connection, ('Jacket', 3250, 9))
        add_product(my_connection, ('Glasses', 700, 7 ))
        add_product(my_connection, ('Joggers', 2000, 4))

        set_product_quantity(my_connection, (4, 6))
        set_product_price(my_connection, (2100, 10))
        delete_product_by_id(my_connection, 13)
        select_products(my_connection)
        select_products_by_price_and_quantity(my_connection, (1000, 5))
        find_products(my_connection)
        my_connection.close()