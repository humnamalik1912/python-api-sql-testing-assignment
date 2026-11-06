
import sqlite3

# Connect to library database
connection = sqlite3.connect("library.db")

# Create cursor
cursor = connection.cursor()

# Read SQL file
with open("library.sql", "r") as file:
    sql_queries = file.read()

# Execute SQL queries
cursor.executescript(sql_queries)

# Save changes
connection.commit()

# Display books priced above 500
print("\nBooks priced above 500:")
cursor.execute("SELECT * FROM books WHERE price > 500")
for book in cursor.fetchall():
    print(book)

# Display all books sorted by price
print("\nBooks sorted by highest price:")
cursor.execute("SELECT * FROM books ORDER BY price DESC")
for book in cursor.fetchall():
    print(book)

# Count total books
cursor.execute("SELECT COUNT(*) FROM books")
print("\nTotal Books:", cursor.fetchone()[0])

# Close connection
connection.close()