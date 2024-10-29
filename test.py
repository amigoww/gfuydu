import sqlite3


conn = sqlite3.connect('hw.db')
cursor = conn.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS store(
        store_id INTEGER PRIMARY KEY,
        title VARCHAR(100) NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS categories(
        code VARCHAR(2) PRIMARY KEY,
        title VARCHAR(150) NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS products(
        id INTEGER PRIMARY KEY,
        title VARCHAR(250) NOT NULL,
        category_code VARCHAR(2) REFERENCES categories(code),
        unit_price FLOAT,
        stock_quantity INTEGER,
        store_id INTEGER REFERENCES store(store_id)
    )
''')


cursor.execute('DELETE FROM categories')
cursor.execute('DELETE FROM store')
cursor.execute('DELETE FROM products')


cursor.executemany('INSERT OR IGNORE INTO categories VALUES (?, ?)', [
    ('FD', 'Food products'),
    ('EL', 'Electronics'),
    ('CL', 'Clothes')
])

cursor.executemany('INSERT OR IGNORE INTO store VALUES (?, ?)', [
    (1, 'Asia'),
    (2, 'Globus'),
    (3, 'Spar')
])

cursor.executemany('INSERT OR IGNORE INTO products VALUES (?, ?, ?, ?, ?, ?)', [
    (1, 'Chocolate', 'FD', 10.5, 129, 1),
    (2, 'Jeans', 'CL', 120.0, 55, 2),
    (3, 'T-Shirt', 'CL', 0.0, 0, 1)
])


conn.commit()


def show_stores():
    cursor.execute('SELECT store_id, title FROM store')
    stores = cursor.fetchall()
    for store in stores:
        print(f"{store[0]}. {store[1]}")

def show_products(store_id):
    cursor.execute('''SELECT products.title, categories.title, products.unit_price, products.stock_quantity
                      FROM products
                      JOIN categories ON products.category_code = categories.code
                      WHERE products.store_id = ?''', (store_id,))
    products = cursor.fetchall()
    if products:
        for product in products:
            print(f"\nНазвание продукта: {product[0]}")
            print(f"Категория: {product[1]}")
            print(f"Цена: {product[2]}")
            print(f"Количество на складе: {product[3]}\n")
    else:
        print("Продукты для выбранного магазина отсутствуют.")


while True:
    print("Вы можете отобразить список продуктов по выбранному id магазина из перечня магазинов ниже, для выхода из программы введите цифру 0:")
    show_stores()
    store_id = input("Введите id магазина: ")
    if store_id == '0':
        break
    show_products(int(store_id))


conn.close()