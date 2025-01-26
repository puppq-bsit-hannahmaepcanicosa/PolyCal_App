import sqlite3

def view_database_contents():
    conn = sqlite3.connect('events.db')
    cursor = conn.cursor()
    
    print("\nEVENTS:")
    cursor.execute("SELECT * FROM events")
    for row in cursor.fetchall():
        print(row)
        
    print("\nNOTES:")
    cursor.execute("SELECT * FROM notes")
    for row in cursor.fetchall():
        print(row)
        
    conn.close()

if __name__ == "__main__":
    view_database_contents()