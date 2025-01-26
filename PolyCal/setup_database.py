import sqlite3

def create_database():
    # Connect to the SQLite database
    conn = sqlite3.connect('archive.db')
    cursor = conn.cursor()
    
    # Create the archive table with a deleted column
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS archive (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            date TEXT NOT NULL,
            deleted INTEGER DEFAULT 0
        )
    ''')
    
    # Insert some sample data into the archive table
    cursor.execute('''
        INSERT INTO archive (title, content, date)
        VALUES
        ('Sample Title 1', 'Sample Content 1', '2023-01-01'),
        ('Sample Title 2', 'Sample Content 2', '2023-02-01')
    ''')
    
    # Create the events table with a deleted column
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            date TEXT NOT NULL,
            description TEXT,
            highlight_color TEXT,
            deleted INTEGER DEFAULT 0
        )
    ''')
    
    # Insert some sample data into the events table
    cursor.execute('''
        INSERT INTO events (title, date, description)
        VALUES
        ('Event 1', '2023-03-01', 'Description for Event 1'),
        ('Event 2', '2023-04-01', 'Description for Event 2')
    ''')
    
    # Commit the changes and close the connection
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database()