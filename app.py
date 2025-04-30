import sqlite3
import os
import random
from datetime import datetime, timedelta

DB_FILE = "sale.db"

def create_dataset():
    if os.path.exists(DB_FILE):
        print("Database already exists.")
        return

    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    
    # Create the sales table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sales (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_name TEXT,
            region TEXT,
            amount TEXT,
            date TEXT
        )
    """)

    names = ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank", "Grace", "Hannah", "Isaac", "Jeeva"]
    regions = ["North", "South", "East", "West"]

    for _ in range(100):
        name = random.choice(names)

        # Simulate slight inconsistencies
        if random.random() < 0.15:
            name = name + "  "
        if random.random() < 0.1:
            name = name.upper()

        region = random.choice(regions)

        amount = f"₹{random.randint(1000, 5000)}"

        # Consistent date format for clarity (DD-MM-YYYY)
        days_ago = random.randint(0, 180)
        date_obj = datetime.now() - timedelta(days=days_ago)
        date = date_obj.strftime("%d-%m-%Y")

        # Insert a few known duplicate rows
        if random.random() < 0.08:
            cursor.execute("INSERT INTO sales (customer_name, region, amount, date) VALUES (?, ?, ?, ?)",
                           ("Bob", "South", "₹1000", "01-12-2024"))
        else:
            cursor.execute("INSERT INTO sales (customer_name, region, amount, date) VALUES (?, ?, ?, ?)",
                           (name, region, amount, date))

    conn.commit()
    conn.close()
    print("Sales dataset created.")

if __name__ == "__main__":
    create_dataset()
