# migrate_mysql_to_sqlite.py
# SmartCart Data Migration Script: Porting MySQL data to SQLite (smartcart.db)
# Preserves all Primary Keys, Foreign Keys, password hashes, cart items, addresses, orders, order items.
# Does NOT modify or delete any data in MySQL (MySQL is READ-ONLY).

import os
import sqlite3
import decimal
import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE = os.path.join(BASE_DIR, "smartcart.db")
SCHEMA_FILE = os.path.join(BASE_DIR, "schema.sql")

# MySQL Configuration Details
MYSQL_HOST = os.environ.get("MYSQL_HOST", "localhost")
MYSQL_USER = os.environ.get("MYSQL_USER", "root")
MYSQL_PASSWORD = os.environ.get("MYSQL_PASSWORD", "anuhya")
MYSQL_DB = os.environ.get("MYSQL_DB", "smartcart_db")

def clean_val(val):
    if isinstance(val, decimal.Decimal):
        return float(val)
    if isinstance(val, (datetime.datetime, datetime.date)):
        return str(val)
    if isinstance(val, bytes):
        return val.decode('utf-8', errors='ignore')
    return val

def run_migration():
    print("=" * 60)
    print("Starting SmartCart MySQL -> SQLite Data Migration")
    print("=" * 60)

    # 1. Connect to MySQL (Source - READ-ONLY)
    try:
        import mysql.connector
        mysql_conn = mysql.connector.connect(
            host=MYSQL_HOST,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD,
            database=MYSQL_DB
        )
        mysql_cursor = mysql_conn.cursor(dictionary=True)
        print(" Successfully connected to MySQL source database.")
    except Exception as e:
        print(f" Failed to connect to MySQL database ({MYSQL_DB}): {e}")
        return False

    # 2. Ensure SQLite database schema exists
    if not os.path.exists(DATABASE):
        print("SQLite database does not exist. Initializing schema...")
        if os.path.exists(SCHEMA_FILE):
            with open(SCHEMA_FILE, "r", encoding="utf-8") as f:
                schema_sql = f.read()
            s_conn = sqlite3.connect(DATABASE)
            s_conn.executescript(schema_sql)
            s_conn.close()

    # 3. Connect to SQLite (Target)
    sqlite_conn = sqlite3.connect(DATABASE)
    sqlite_cursor = sqlite_conn.cursor()
    sqlite_cursor.execute("PRAGMA foreign_keys = OFF;")

    stats = {}

    # --- MIGRATE TABLE: admin ---
    mysql_cursor.execute("SELECT * FROM admin")
    admins = mysql_cursor.fetchall()
    for row in admins:
        sqlite_cursor.execute("""
            INSERT OR REPLACE INTO admin (admin_id, name, email, password, profile_image)
            VALUES (?, ?, ?, ?, ?)
        """, (
            row['admin_id'],
            row['name'],
            row['email'],
            clean_val(row['password']),
            row.get('profile_image')
        ))
    stats['admin'] = len(admins)

    # --- MIGRATE TABLE: products ---
    mysql_cursor.execute("SELECT * FROM products")
    products = mysql_cursor.fetchall()
    for row in products:
        sqlite_cursor.execute("""
            INSERT OR REPLACE INTO products (product_id, name, description, category, price, image)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            row['product_id'],
            row['name'],
            row.get('description'),
            row['category'],
            clean_val(row['price']),
            row['image']
        ))
    stats['products'] = len(products)

    # --- MIGRATE TABLE: user_addresses ---
    mysql_cursor.execute("SELECT * FROM user_addresses")
    addresses = mysql_cursor.fetchall()
    for row in addresses:
        sqlite_cursor.execute("""
            INSERT OR REPLACE INTO user_addresses (address_id, user_id, full_name, mobile, house_number, area, landmark, city, state, pincode, created_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            row['address_id'],
            row['user_id'],
            row['full_name'],
            row['mobile'],
            row['house_number'],
            row['area'],
            row.get('landmark'),
            row['city'],
            row['state'],
            row['pincode'],
            clean_val(row.get('created_at'))
        ))
    stats['user_addresses'] = len(addresses)

    # --- MIGRATE TABLE: orders ---
    mysql_cursor.execute("SELECT * FROM orders")
    orders = mysql_cursor.fetchall()
    for row in orders:
        sqlite_cursor.execute("""
            INSERT OR REPLACE INTO orders (order_id, user_id, address_id, razorpay_order_id, razorpay_payment_id, amount, payment_status, created_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            row['order_id'],
            row['user_id'],
            row.get('address_id'),
            row['razorpay_order_id'],
            row['razorpay_payment_id'],
            clean_val(row['amount']),
            row['payment_status'],
            clean_val(row.get('created_at'))
        ))
    stats['orders'] = len(orders)

    # --- MIGRATE TABLE: order_items ---
    mysql_cursor.execute("SELECT * FROM order_items")
    order_items = mysql_cursor.fetchall()
    for row in order_items:
        sqlite_cursor.execute("""
            INSERT OR REPLACE INTO order_items (id, order_id, product_id, product_name, quantity, price)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            row['id'],
            row['order_id'],
            row['product_id'],
            row['product_name'],
            row['quantity'],
            clean_val(row['price'])
        ))
    stats['order_items'] = len(order_items)

    # --- MIGRATE TABLE: cart_items ---
    mysql_cursor.execute("SELECT * FROM cart_items")
    cart_items = mysql_cursor.fetchall()
    for row in cart_items:
        cart_id = row.get('cart_id') or row.get('id')
        sqlite_cursor.execute("""
            INSERT OR REPLACE INTO cart_items (id, user_id, product_id, quantity)
            VALUES (?, ?, ?, ?)
        """, (
            cart_id,
            row['user_id'],
            row['product_id'],
            row['quantity']
        ))
    stats['cart_items'] = len(cart_items)

    # Commit SQLite changes
    sqlite_conn.commit()

    # Enable and check Foreign Key Integrity
    sqlite_cursor.execute("PRAGMA foreign_keys = ON;")
    sqlite_cursor.execute("PRAGMA foreign_key_check;")
    fk_errors = sqlite_cursor.fetchall()

    sqlite_conn.close()
    mysql_cursor.close()
    mysql_conn.close()

    print("=" * 60)
    print("Migration Statistics:")
    for tbl, count in stats.items():
        print(f"  - {tbl}: {count} records migrated")
    
    if fk_errors:
        print(f" Foreign Key Check: {len(fk_errors)} violation(s) found: {fk_errors}")
    else:
        print(" Foreign Key Integrity: PASSED (0 violations)")
    print("=" * 60)

    return True

if __name__ == "__main__":
    run_migration()
