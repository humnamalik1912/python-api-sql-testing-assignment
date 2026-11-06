
-- Create books table
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    year INTEGER,
    price REAL
);

-- Insert 8 book records
INSERT OR REPLACE INTO books VALUES
(1, 'Python Basics', 'John Smith', 2022, 650),
(2, 'Clean Code', 'Robert Martin', 2008, 900),
(3, 'Atomic Habits', 'James Clear', 2018, 750),
(4, 'The Alchemist', 'Paulo Coelho', 1988, 450),
(5, 'Deep Work', 'Cal Newport', 2016, 550),
(6, 'Rich Dad Poor Dad', 'Robert Kiyosaki', 1997, 400),
(7, 'Introduction to SQL', 'Mark Allen', 2021, 800),
(8, 'Artificial Intelligence', 'Stuart Russell', 2020, 1200);

-- Display books priced above 500
SELECT * FROM books
WHERE price > 500;

-- Display all books: highest price first
SELECT * FROM books
ORDER BY price DESC;

-- Count total books
SELECT COUNT(*) AS total_books FROM books;

-- Update one book price using WHERE
UPDATE books
SET price = 700
WHERE id = 1;
